from flask import Blueprint, render_template, request, redirect
from flask import Blueprint, redirect, url_for, render_template, request, session
import psycopg2
from werkzeug.security import check_password_hash, generate_password_hash

lab5 = Blueprint('lab5', __name__)

def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="petrovichev_base",
        user="petrovichev_base",
        password="123")
    
    return conn;
    
def dbClose(cur, conn):
    cur.close()
    conn.close()

@lab5.route('/lab5/')
def main():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")
    result = cur.fetchall()
    
    print(result)

    cur.close()
    conn.close()
    return "go to console"

@lab5.route('/lab5/users')
def show_users():
    connection = dbConnect()
    cursor = connection.cursor()
    # Выполните SQL-запрос для выбора имен пользователей
    cursor.execute("SELECT username FROM users;")
    # Получите результаты запроса
    results = cursor.fetchall()
    # Закройте соединение
    cursor.close()
    connection.close()
    # Отобразите результаты в HTML
    return render_template('lab5.html', users=results)

@lab5.route('/lab5/glavnaia')
def lab5_glav():
    username = session.get('username')
    return render_template('glavnaia.html', username=username)

@lab5.route('/lab5/register', methods=["GET", "POST"])
def registerPage():
    errors = []

    if request.method == "GET":
        return render_template("register.html", errors=errors)
    
    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста, заполните поля")
        print(errors)
        return render_template("register.html", errors=errors)
    
    HashPassword = generate_password_hash(password)
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")
    
    if cur.fetchone() is not None:
        errors.append("Пользователь с таким именем уже существует")
        
        conn.close()
        cur.close()

        return render_template("register.html", errors=errors)
    
    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{HashPassword}');")

    conn.commit()
    conn.close()
    cur.close()

    return redirect("/lab5/login5")

@lab5.route('/lab5/login5', methods=["GET", "POST"])
def login5():
    errors = []

    if request.method == "GET":
        return render_template("login5.html", errors=errors)
    
    username = request.form.get("username")
    password = request.form.get('password')

    if not (username or password):
        errors.append('Пожалуйста, заполните все поля')
        return render_template('login5.html', errors=errors)
    
    conn=dbConnect()
    cur=conn.cursor()

    cur.execute(f"SELECT id, password FROM users WHERE username = '{username}'")

    result = cur.fetchone()

    if result is None:
        errors.append('Неправильный логин или пороль')
        dbClose(cur, conn)
        return render_template("login5.html", errors=errors)

    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        dbClose(cur,conn)
        return redirect("/lab5/glavnaia")
    
    else:
        errors.append("Неправильный логин или пороль")
        return render_template("login5.html", errors=errors)
    
@lab5.route('/lab5/create_zametki', methods=["GET", "POST"])
def createArticle():
    errors = []

    userID = session.get("id")

    if userID is not None:
        if request.method == "GET":
            return render_template("create_zametki.html")
        
        if request.method == "POST":
            text_article = request.form.get("text_article")
            title = request.form.get("title_article")

            if len(text_article) == 0:
                errors.append("Заполните текст")
                return render_template("create_zametki.html", errors=errors)
            
            
            conn = dbConnect()
            cur = conn.cursor()

            cur.execute(f"INSERT INTO articles(user_id, title, article_text) VALUES ({userID}, '{title}', '{text_article}') RETURNING id")

            new_article_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur, conn)

            return redirect(f"/lab5/articles/{new_article_id}")
        
    return redirect("/lab5/login5")

    

@lab5.route("/lab5/articles/<int:article_id>")
def getArticle(article_id):
    userID = session.get('id')

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT title, article_text FROM articles WHERE id = %s AND user_id = %s", (article_id, userID))

        articleBody = cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            return "АХПАВХПВАХПВХВРКУЦВАХ НЕ ПОЛУЧИЛОСЬ"
        
        text = articleBody[1].splitlines()

    return render_template("articleN.html", article_text=text, article_title=articleBody[0], user_name=session.get("user_name"))
    
@lab5.route('/lab5/articles')
def list_articles():
    userID = session.get('id')
    username = session.get("username")
    show_all_articles = request.args.get('show_all') == '1'

    connection = dbConnect()
    cursor = connection.cursor()

    if not userID:
        return redirect("/lab5/login5")

    if userID and not show_all_articles:
        # Если пользователь авторизован и не выбрал "Все статьи"
        cursor.execute("SELECT id, title FROM articles WHERE user_id = %s", (userID,))
    elif userID and show_all_articles:
        # Если пользователь авторизован и выбрал "Все статьи",
        cursor.execute("SELECT id, title FROM articles")

    articles_data = cursor.fetchall()
    articles = [{'id': row[0], 'title': row[1]} for row in articles_data]

    cursor.close()
    connection.close()

    return render_template('articles.html', articles=articles, username=username)

@lab5.route('/lab5/logout', methods = ["GET", "POST"])
def logout():
    # Очищаем данные сессии
    session.clear()
   
    return redirect("/lab5/glavnaia")
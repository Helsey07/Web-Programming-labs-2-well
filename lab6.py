from flask import Blueprint, render_template, request, redirect
from Db import db
from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user

from flask import Blueprint, redirect, url_for, render_template, request, session
import psycopg2

lab6 = Blueprint('lab6', __name__)

@lab6.route('/lab6/check')
def main():
    # SELECT * FROME users
    my_users = users.query.all()
    print(my_users)
    return 'result in console!'

@lab6.route('/lab6/checkarticles')
def checkarticles():
    my_articles = articles.query.all()
    print(my_articles)
    return 'console'

@lab6.route('/lab6/register6', methods=["GET", "POST"])
def register():
    errors = []

    if request.method == "GET":
        return render_template('register6.html', errors=errors)
     
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    isUserExit = users.query.filter_by(username=username_form).first()
    if isUserExit is not None:
        errors.append("Пользователь уже существует")
        return render_template('register6.html', errors=errors)
    
    if username_form is None or password_form is None or username_form.strip() == '' or password_form.strip() == '':
        errors.append("Пожалуйста, заполните все поля")
        print(errors)
        return render_template('register6.html', errors=errors)
    
    if len(password_form) < 5:
            errors.append("Пароль должен содержать не менее 5 символов")
            print(errors)
            return render_template('register6.html', errors=errors)
    
    hashedPswd = generate_password_hash(password_form, method='pbkdf2')
    newUser = users(username=username_form, password=hashedPswd)

    db.session.add(newUser)
    db.session.commit()

    return redirect("/lab6/login6")

@lab6.route('/lab6/login6', methods=["GET", "POST"])
def login():
    errors = []

    if request.method == "GET":
         return render_template('login6.html')

    username_form = request.form.get("username")
    password_form = request.form.get("password")

    my_user = users.query.filter_by(username=username_form).first()

    if my_user is not None:
         if check_password_hash(my_user.password, password_form):
              login_user(my_user, remember=False)
              return redirect('/lab6/glav6')
         else: 
            errors.append("Неправильный пароль")
            return render_template('login6.html', errors=errors)
         
    if not (username_form or password_form):
        errors.append("Пожалуйста заполните все поля")
        return render_template("login6.html", errors=errors)
    if username_form == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('login6.html', errors=errors)
    if password_form == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('login6.html', errors=errors)
    
    else: 
        errors.append('Пользователя не существует')
        return render_template('login6.html', errors=errors) 
    
@lab6.route('/lab6/glav6', methods = ["GET", "POST"])
def lab6_glav():
    username_form = session.get('username')
    return render_template('glav6.html', username = username_form)

@lab6.route('/lab6/logout6', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/lab6/glav6')

@lab6.route('/lab6/list_articles', methods=["GET", "POST"])
@login_required
def article_list():
    my_articles = articles.query.filter_by(user_id=current_user.id).all()
    return render_template('list_articles.html', articles=my_articles)

@lab6.route("/lab6/newtitle6", methods=["GET", "POST"])
@login_required
def createArticle():
    if request.method == "GET":
        return render_template("newtitle6.html")

    article_text = request.form.get("article_text")
    title = request.form.get("article_title")

    if len(article_text) == 0:
        errors = ["Заполните текст"]
        return render_template("newtitle6.html", errors=errors)

    new_article = articles(user_id=current_user.id, title=title, article_text=article_text)
        

    db.session.add(new_article)
    db.session.commit()
    
    return redirect("/lab6/list_articles")

@lab6.route("/lab6/articles6/<int:article_id>")
@login_required
def viewArticle(article_id):
    article = articles.query.get(article_id)
    if article and article.user_id == current_user.id:  # добавляем проверку на соответствие user_id статьи текущему пользователю
        return render_template('articles6NOW.html', title=article.title, content=article.article_text)
    else:
        return "Статья не найдена или не принадлежит вам"


from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/index")

def start():
    return redirect("/menu", code=302)
    

@app.route("/menu")
def menu():
    return """
<!DOCTYPE html>
    <html>
        <head>
            <title>
                Петровичев Егор Васильевич, Лабораторная 1
            </title>
        </head>

        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>

            <h1>
                НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
            </h1>
            <h2>Меню</h2>

            <a href="lab1">Лабораторная работа №1</a>

            <footer>
                &copy; Петровичев Егор, ФБИ-13, 3 курс, 2023
            </footer>
        </body>
    </html>
    """
      

@app.route("/lab1")
def lab1():
       return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>
                Петровичев Егор Васильевич, Лабораторная 112121
            </title>
        </head>

        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>

            <h1>
                web-сервер на flask
            </h1>

            <div>
                Flask — фреймворк для создания веб-приложений на языке
                программирования Python, использующий набор инструментов
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                называемых микрофреймворков — минималистичных каркасов
                веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
            </div>

            <footer>
                &copy; Петровичев Егор, ФБИ-13, 3 курс, 2023
            </footer>
        </body>
    </html>
    """
    

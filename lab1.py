from flask import Blueprint, redirect, url_for, render_template

lab1 = Blueprint('lab1', __name__)

@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)
    

@lab1.route("/menu")    
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

            <a href="lab1">Лабораторная работа №1</a> <br>
            <a href="lab2">Лабораторная работа №2</a>

            <footer>
                &copy; Петровичев Егор, ФБИ-13, 3 курс, 2023
            </footer>
        </body>
    </html>
    """


@lab1.route("/lab1")
def lab():
       return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>
                Петровичев Егор Васильевич, Лабораторная 112121
            </title>
            <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css') + '''">
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

            <a href="/menu">Меню</a>

            <h1>Реализованные роуты</h1>
            
            <li><a href="/lab1/oak">Тюлень</a></li>
            <li><a href="/lab1/student">Студент</a></li>
            <li><a href="/lab1/python">Python</a></li>
            <li><a href="/lab1/tulen">Описание Тюленя</a></li>
            

            <footer>
                &copy; Петровичев Егор, ФБИ-13, 3 курс, 2023
            </footer>
        </body>
    </html>
    '''


@lab1.route("/lab1/oak")
def oak():
     return '''
<!DOCTYPE html>
    <html>
        <head>
            <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css') + '''"">
        </head>

        <body>
            <h1>Тюленьчик</h1>
            <img class="image_one", src="''' +url_for('static', filename='oak.jpg') + '''">
        </body>
    </html>
'''


@lab1.route("/lab1/student")
def student():
     return '''
<!DOCTYPE html>
    <html>
        <head>
            <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css') + '''"">
        </head>

        <body>
            <h1>Петровичев Егор Васильевич</h1>
            <img class="image_two", src="''' +url_for('static', filename='nstu.jpg') + '''">
        </body>
    </html>
'''


@lab1.route("/lab1/python")
def python():
     return '''
<!DOCTYPE html>
    <html>
        <head>
            <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css') + '''"">
        </head>

        <body>
            <h1>Язык программирования python</h1>

            <div>
                Python высокоуровневый язык программирования общего назначения
                с динамической строгой типизацией и автоматическим управлением памятью, 
                ориентированный на повышение производительности разработчика, читаемости
                кода и его качества, а также на обеспечение переносимости написанных
                на нём программ. Язык является полностью объектно-ориентированным в том плане,
                что всё является объектами. Необычной особенностью языка является выделение блоков кода пробельными отступами.
            </div>

            <div>
                Синтаксис ядра языка минималистичен, за счёт чего на практике
                редко возникает необходимость обращаться к документации[28]. 
                Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов[26]. 
                Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление
                памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых
                языках, таких как C или C++.
            </div>

            <img class="image_two", src="''' +url_for('static', filename='python.jpg') + '''">
        </body>
    </html>
'''


@lab1.route("/lab1/tulen")
def tulen():
     return '''
<!DOCTYPE html>
    <html>
        <head>
            <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css') + '''"">
        </head>

        <body>
            <h1>Тюлени - милашки!</h1>

            <div>
                Такому месту в классификации видов и подвидов животных
                тюлени обязаны своему эволюционному происхождению.
                Согласно молекулярно-генетическим исследованиям,
                установлено, что предки этого ластоногого хищника
                жили на суше, а самым древним из них является медведь,
                который, в свою очередь, произошел от собакоподобного предка.
            </div>

            <div>
                При нырянии в воду температура мозга тюленей снижается на 3 градуса,
                а сердцебиение замедляется со 120 до 15-20 ударов в минуту.
                Так предусмотрено природой в целях экономии потребления кислорода,
                чтобы тюлени могли как можно дольше находиться под водой.
            </div>

            <img class="image_two", src="''' +url_for('static', filename='tulen.jpg') + '''">
        </body>
    </html>
'''


@lab1.route('/lab2/example')
def example():
    name = 'Петровичев Егор Василич'
    number_lab = 'Лабораторная работа №2'
    group = 'ФБИ-13'
    course = '3 курс'

    fruits = [
        {'name': 'яблоки','price': 100},
        {'name':'груши', 'price': 100},
        {'name':'апельсины', 'price': 100},
        {'name':'мандарины', 'price': 100},
        {'name':'манго', 'price': 100}
    ]

    books = [
         {'name':'Название 1', 'autor': 'Автор 1', 'genre': 'жанр 1', 'pages': 228},
         {'name':'Название 2', 'autor': 'Автор 2', 'genre': 'жанр 2', 'pages': 2238},
         {'name':'Название 3', 'autor': 'Автор 3', 'genre': 'жанр 3', 'pages': 228},
         {'name':'Название 4', 'autor': 'Автор 4', 'genre': 'жанр 4', 'pages': 2128},
         {'name':'Название 5', 'autor': 'Автор 5', 'genre': 'жанр 5', 'pages': 2428},
         {'name':'Название 6', 'autor': 'Автор 6', 'genre': 'жанр 6', 'pages': 228},
         {'name':'Название 7', 'autor': 'Автор 7', 'genre': 'жанр 7', 'pages': 2528},
         {'name':'Название 8', 'autor': 'Автор 8', 'genre': 'жанр 8', 'pages': 2628},
         {'name':'Название 9', 'autor': 'Автор 9', 'genre': 'жанр 9', 'pages': 2128},
         {'name':'Название 10', 'autor': 'Автор 10', 'genre': 'жанр 10', 'pages': 2218}
    ]
    return render_template('example.html', name=name, number_lab=number_lab, group=group, course=course,
                           fruits=fruits, books=books)


@lab1.route('/lab2/')
def lab2():
    return render_template('lab2.html')


@lab1.route('/lab2/shoos/')
def shoos():
    return render_template('shoos.html')
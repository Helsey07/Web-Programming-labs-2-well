from flask import Blueprint, render_template, request

lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    password = request.form.get('password')
    error = 'Неверный логин и/или пороль'
    error_2 = 'Не введено поле логин'
    error_3 = 'Не введено поле Пороль'
    

    if username == 'alex' and password == '123':
       return render_template('success_login.html', username=username)
    if not username:
        return render_template('login.html', error_2=error_2, username=username, password=password)
    elif not password:
        return render_template('login.html', error_3=error_3, username=username, password=password)
    elif request.method == 'POST':
        return render_template('login.html', error=error, username=username, password=password)
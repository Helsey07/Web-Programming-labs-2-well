from flask import Blueprint, redirect, url_for, render_template, request

lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')

    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')

    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')

    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')

    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('pay.html', price=price)

@lab3.route('/lab3/success')
def success():
    return render_template('success.html')

@lab3.route('/lab3/bilet')
def bilet():
    return render_template('bilet.html')


@lab3.route('/lab3/pay_billet')
def pay_billet():

    surname = request.args.get('surname')
    name = request.args.get('name')
    patronymic = request.args.get('patronymic')

    age = request.args.get('age')
    sickle = request.args.get('sickle')
    number = request.args.get('number')

    type_bilet = request.args.get('type_bilet')
    type_shelf = request.args.get('type_shelf')

    departure_point = request.args.get('departure_point')
    piece_of_luggage = request.args.get('piece_of_luggage')
    place_of_arrival = request.args.get('place_of_arrival')

    date_start = request.args.get('date_start')
    date_finish = request.args.get('date_finish')

    return render_template('pay_billet.html', surname=surname, name=name, patronymic=patronymic,
                           age=age, sickle=sickle, number=number, type_bilet=type_bilet,
                           type_shelf=type_shelf,departure_point=departure_point, place_of_arrival=place_of_arrival,
                           date_start=date_start, date_finish=date_finish,
                           piece_of_luggage=piece_of_luggage)



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
    elif not username:
        return render_template('login.html', error_2=error_2, username=username, password=password)
    elif not password:
        return render_template('login.html', error_3=error_3, username=username, password=password)
    elif request.method == 'POST':
        return render_template('login.html', error=error, username=username, password=password)
    
@lab4.route('/lab4/fridge', methods = ['GET', 'POST'])
def fridge():
    temperature = request.form.get('temperature')
    conrs = request.form.get('corns')
    message = ""

    if request.method == 'POST':
        if not temperature:
            message = "Ошибка: не задана температура"
        else:
            temperature = int(temperature)
            if temperature < -12:
                message = "Не удалось установить температуру — слишком низкое значение"
            elif temperature > -1:
                message = "Не удалось установить температуру — слишком высокое значение"
            elif -12 <= temperature <= -9:
                message = f"Установлена температура: {temperature}°С"
            elif -8 <= temperature <= -5:
                message = f"Установлена температура: {temperature}°С"
            elif -4 <= temperature <= -1:
                message = f"Установлена температура: {temperature}°С"

    return render_template('fridge.html', message=message, temperature=temperature)

@lab4.route('/lab4/corn', methods = ['GET', 'POST'])
def order_grain():
    if request.method == 'POST':
        grain = request.form.get('grain')
        weight = request.form.get('weight')

        if not weight:
            error = 'Ошибка: не введен вес'
            return render_template('corn.html', error=error)

        weight = float(weight)
        price_per_ton = {
            'ячмень': 12000,
            'овёс': 8500,
            'пшеница': 8700,
            'рожь': 14000
        }


        price = price_per_ton[grain] * weight

        if weight > 50:
            discount = 0.1 * price
            price -= discount
            discount_message = 'Применена скидка за большой объем.'
        else:
            discount_message = ''


        if weight > 500:
            error = 'Извините, такого объема сейчас нет в наличии.'
            return render_template('corn.html', error=error)
        
        if weight <= 0:
            error = 'Ошибка: введен недопустимый вес'
            return render_template('corn.html', error=error)

        message = f'Заказ успешно сформирован. Вы заказали {grain}. Вес: {weight} т. Сумма к оплате: {price} руб. {discount_message}'


        return render_template('corn.html', message=message)

    return render_template('corn.html')


    

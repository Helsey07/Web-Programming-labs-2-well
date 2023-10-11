from flask import Blueprint, redirect, url_for, render_template
from lab1 import lab1

lab2 = Blueprint('lab2', __name__)
lab2.register_blueprint(lab1)

@lab2.route('/lab2/example')
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


@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/shoos/')
def shoos():
    return render_template('shoos.html')
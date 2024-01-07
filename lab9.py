from flask import Blueprint, abort, render_template, request, jsonify

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def main():
    return render_template('lab9/index.html')


@lab9.app_errorhandler(404)
def not_found(e):
    return render_template('lab9/error.html'), 404

@lab9.route("/lab9/er")
def index():
    raise Exception("Произошла ошибка!")


@lab9.app_errorhandler(500)
def not_found(e):
    return render_template('lab9/error500.html'), 500
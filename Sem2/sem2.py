
"""Создать страницу, на которой будет кнопка "Нажми меня", при нажатии на которую будет переход на другую страницу
с приветствием пользователя по имени. Пример решения"""



from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from pathlib import Path

app = Flask(__name__)

#
# @app.route('/')
# def index():
#     return render_template('task1.html')
#
#
# @app.route('/submit', methods = ['GET', 'POST'])
# def submit():
#     name = request.form.get('name')
#     return f'Hello {name}'
#     if request.method == 'POST':
#         req






"""Создать страницу, на которой будет изображение и ссылка на другую страницу, на которой будет отображаться 
форма для загрузки изображений."""


# @app.route('/')
# def index():
#     return render_template('task2.html')
#
# @app.route('/task21', methods = ['GET', 'POST'])
# def task21():
#     if request.method == 'GET':
#         return render_template('task21.html')
#     file = request.files.get('file')
#     filename = secure_filename(file.name)
#     file.save(Path('uploads',filename))
#     return 'File uploaded'


"""Создать страницу, на которой будет форма для ввода логина и пароля, при нажатии на кнопку "Отправить" 
будет произведена проверка соответствия логина и пароля и переход на страницу приветствия пользователя 
или страницу с ошибкой."""

@app.route('/')
def index():
    return render_template('task3_login.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    login = 'a'
    password = '1'
    get_log = request.form.get('name')
    get_password = request.form.get('password')
    if request.method == 'POST':
        if login == get_log and password == get_password:
            return 'Good'
        else:
            return 'Bad'


if __name__ == '__main__':
    app.run(debug=True)
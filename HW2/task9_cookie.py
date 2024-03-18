"""
Задание №9
Создать страницу, на которой будет форма для ввода имени и электронной почты
При отправке которой будет создан cookie файл с данными пользователя
Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка "Выйти"
При нажатии на кнопку будет удален cookie файл с данными пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.

"""
from flask import Flask, request, render_template, make_response, redirect, url_for, session

app9 = Flask(__name__)
app9.secret_key = 'gsfdgsfdsaf68989fsdfsdjngf'
@app9.route('/')
def task9():
    return render_template('task9.html')

@app9.route('/cookie', methods=['GET', 'POST'])
def task9_cookie():
    if request.method == 'POST':
        answer = request.form
        session['login'] = answer.get('login')
        session['email'] = answer.get('email')


    return render_template('task9.1.html', cont=session)


@app9.route('/logout', methods=['GET', 'POST'])
def task9_logout():
   session.pop('login', None)
   session.pop('email', None)
   return redirect(url_for('task9'))


if __name__ == '__main__':
    app9.run(debug=True)

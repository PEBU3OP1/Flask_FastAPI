from flask import Flask, request, render_template

"""
Задание №5
Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"
При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом.

"""

app1 = Flask(__name__)


@app1.route('/')
def task5():
    return render_template('task5.1.html')


@app1.post('/calculate')
def calculate():
    from_form = request.form
    try:
        result = eval(str(from_form.get("num1") + from_form.get("selection") + from_form.get("num2")))
        return f'{from_form.get("num1")}{from_form.get("selection")}{from_form.get("num2")} = {result}'
    except:
        return 'Ошибка'


if __name__ == '__main__':
    app1.run(debug=True)

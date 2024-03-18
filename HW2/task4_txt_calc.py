from flask import Flask, request, render_template


"""
Задание №4
Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.
"""

def calc_text(txt:str):
    return len(txt.split(' '))

app1 = Flask(__name__)

@app1.route('/')
def task4():
    return render_template('task4.html')


@app1.post('/calc')
def calculate():
    txt = request.form.get("text_to_calc")
    return f'Вы ввели {calc_text(txt)} слов(о)'



if __name__ == '__main__':
    app1.run(debug=True)
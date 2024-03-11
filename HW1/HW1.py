from flask import Flask, render_template


app = Flask(__name__)

conts = {
    'title': 'Контакты',
    'mail':'xxx@mail,ru',
    'phone': '1111332',
    'fax' : '3df35',
    'address': 'msk, sadovaya str, b 112'

}
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/contacts/')
def contacts():
    return render_template('contacts.html', conts = conts)
@app.route('/about/')
def about():
    return render_template('about.html')




@app.route('/jackets/')
def jackets():
    return render_template('jackets.html')
@app.route('/trousers/')
def trousers():
    return render_template('trousers.html')
@app.route('/boots/')
def boots():
    return render_template('boots.html')


if __name__ == '__main__':
    app.run(debug=True)
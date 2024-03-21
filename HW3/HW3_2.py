"""
Задание №7
Создайте форму регистрации пользователей в приложении Flask. Форма должна
содержать поля: имя, фамилия, email, пароль и подтверждение пароля. При отправке
формы данные должны валидироваться на следующие условия:
○ Все поля обязательны для заполнения.
○ Поле email должно быть валидным email адресом.
○ Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и
одну цифру.
○ Поле подтверждения пароля должно совпадать с полем пароля.
○ Если данные формы не прошли валидацию, на странице должна быть выведена
соответствующая ошибка.
○ Если данные формы прошли валидацию, на странице должно быть выведено
сообщение об успешной регистрации.

Задание №8
Создать форму для регистрации пользователей на сайте.
Форма должна содержать поля "Имя", "Фамилия", "Email",
"Пароль" и кнопку "Зарегистрироваться".
При отправке формы данные должны сохраняться в базе
данных, а пароль должен быть зашифрован.

"""

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm, CSRFProtect
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_sqlalchemy import SQLAlchemy




class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', choices = [('male', 'Муж'), ('female', 'Жен')])

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

class HomeworkForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=1)])
    confirm_password = PasswordField('Confirm Password',  validators=[DataRequired(), EqualTo('password')])


app9 = Flask(__name__)
app9.config['SECRET_KEY'] = b'dsadasdf4r4ojhoiphyfairu98'
app9.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db9 = SQLAlchemy(app9)
class User(db9.Model):
    id = db9.Column(db9.Integer, primary_key=True)
    name = db9.Column(db9.String(80), nullable=False)
    last_name = db9.Column(db9.String(80), nullable=False)
    email = db9.Column(db9.String(80), nullable=False)
    password = db9.Column(db9.String(8), nullable=False)





@app9.cli.command('init_db9')
def init_db9():
    db9.create_all()
@app9.cli.command('create_user')
def create_user(name, last_name, email, password):
    new_user = User(name=name, last_name=last_name, email=email, password=password)
    db9.session.add(new_user)
    db9.session.commit()

@app9.route('/')
def index():
    return 'Hello World'

@app9.route('/login/', methods=['GET', 'POST'])
def login_page():
    form = HomeworkForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data

        new_user = User(name=name, last_name=last_name, email=email, password=password)
        db9.session.add(new_user)
        db9.session.commit()

        return 'Вы успешно зарегистрированы'

    return render_template('login.html', form = form)




"""
Задание №2
Создать базу данных для хранения информации о книгах в библиотеке.
База данных должна содержать две таблицы: "Книги" и "Авторы".
В таблице "Книги" должны быть следующие поля: id, название, год издания,
количество экземпляров и id автора.
В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
Необходимо создать связь между таблицами "Книги" и "Авторы".
Написать функцию-обработчик, которая будет выводить список всех книг с
указанием их авторов.
"""
import datetime

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app3 = Flask(__name__)
app3.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app3)
class Writer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    books = db.Relationship('Book', backref='writer', lazy=True)

    def __repr__(self):
        return f' {self.name}, {self.last_name}'

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80),nullable=False)
    year_of_producing = db.Column(db.Date, nullable=False)
    q_ty = db.Column(db.Integer, nullable=False)
    writer_id = db.Column(db.Integer, db.ForeignKey('writer.id'))

    def __repr__(self):
        return f'Book {self.book_name}, {self.writer_id}'





@app3.cli.command('init_db')
def init_db():
    db.create_all()

@app3.cli.command('fill_db')
def fill_db():
    count = 5
    for author in range(1,count + 1):
        new_author = Writer(name=f'author_name{author}', last_name=f'last_name{author}')
        db.session.add(new_author)
    db.session.commit()

    for book in range(1, count**2):

        new_book = Book(book_name=f'Book{book}', q_ty=book, year_of_producing =datetime.datetime.utcnow() - datetime.timedelta(days=book), writer_id= book % count + 1)
        db.session.add(new_book)
    db.session.commit()


@app3.route('/book')
def book_list():
    books = Book.query.all()
    cont = {'books': books}
    return render_template('hw3.html', **cont)



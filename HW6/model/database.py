import  sqlalchemy
import databases


DATABASE_URL = "sqlite:///./hw6.db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users', metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(length=32)),
    sqlalchemy.Column('last_name', sqlalchemy.String(length=32)),
    sqlalchemy.Column('bday', sqlalchemy.Date()),
    sqlalchemy.Column('email', sqlalchemy.String(length=32)),
    sqlalchemy.Column('address', sqlalchemy.String(length=256)),


)
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
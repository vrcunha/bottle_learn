from peewee import SqliteDatabase, Model, TextField

db = SqliteDatabase('database/api_bottle.db')

class Products(Model):
    name = TextField()
    price = TextField()
    stock = TextField()

    class Meta:
        database = db

Products.create_table()
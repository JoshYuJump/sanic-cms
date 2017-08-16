from config import DATABASE
from peewee import *

db = SqliteDatabase(DATABASE.get('DB_NAME'))


class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)

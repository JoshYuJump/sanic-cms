from datetime import datetime
from peewee import *
from playhouse.db_url import connect
from config import Engine, DATABASE


db_engine = DATABASE.get('DB_ENGINE')
db_name = DATABASE.get('DB_NAME')
db_user = DATABASE.get('DB_USER')
db_password = DATABASE.get('DB_PASSWORD')
db_host = DATABASE.get('DB_HOST')
db_port = DATABASE.get('DB_PORT')

print('db_engine: %s\nEngine.SQLITE: %s\n' % (db_engine, Engine.SQLITE))

if db_engine == Engine.SQLITE:
    db = connect('%s:///%s' % (db_engine.value, db_name))
elif db_engine in (Engine.MYSQL, Engine.POSTGRESQL):
    db = connect('%s:///%s:%s@%s:%d/%d' % (
        db_engine.value, db_user, db_password,
        db_host, db_port, db_name))


class BaseModel(Model):

    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)


class Category(BaseModel):
    name = CharField(unique=True)
    slug = CharField(unique=True)


class Content(BaseModel):
    title = CharField()
    channel = CharField()
    author = CharField()
    text = TextField()
    images = CharField()
    slug = CharField(index=True)
    push_time = DateTimeField(default=datetime.now)


class PageView(BaseModel):
    content = CharField()
    slug = CharField(index=True)


def create_tables():
    tables = [User, Category, Content]
    db.create_tables(tables, safe=True)


if __name__ == '__main__':
    pass

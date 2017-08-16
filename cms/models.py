from config import Engine, DATABASE
from peewee import *
from playhouse.db_url import connect

db_engine = DATABASE.get('DB_ENGINE')
db_name = DATABASE.get('DB_NAME')
db_user = DATABASE.get('DB_USER')
db_password = DATABASE.get('DB_PASSWORD')
db_host = DATABASE.get('DB_HOST')
db_port = DATABASE.get('DB_PORT')

print (db_engine == Engine.SQLITE)

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

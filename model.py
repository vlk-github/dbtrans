from peewee import *


def _callback(database: MySQLDatabase):
    database.field_overrides['text'] = 'TEXT'
    pass

database_proxy = Proxy()
database_proxy.attach_callback(_callback)


class BaseModel(Model):

    class Meta:
        database = database_proxy


class Task(BaseModel):
    id = IntegerField(primary_key=True)
    source = TextField()
    result = TextField()
    status = IntegerField()

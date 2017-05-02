from peewee import *

database_proxy = Proxy()

cc = TextField()

print(cc)

class Task(Model):
    id = IntegerField(primary_key=True)
    source = TextField()
    result = TextField()
    status = IntegerField()


    class Meta:
        database = database_proxy


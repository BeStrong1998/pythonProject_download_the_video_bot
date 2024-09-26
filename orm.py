from peewee import *



db = SqliteDatabase('data.db')

class Links(Model):
    lin = CharField()

    class Meta:
        database = db

Links.create_table()

new_links = []
for i in Links.select():
    new_links.append(i.lin)

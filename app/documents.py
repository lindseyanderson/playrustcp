import datetime

from app import db

class Server(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    owner = db.StringField(max_length=32, required=True)
    ip = db.StringField(max_length=15, required=True)
    port = db.IntField(required=True)

class Admin(db.Document):  
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    username = db.StringField(max_length=32, required=True)
    password = db.StringField(max_length=255, required=True)

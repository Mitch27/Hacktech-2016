from tumblelog import db

class Post(db.Document):
    name = db.StringField(max_length=100, required=True)
    age = db.IntField(min_value=0, max_value=120, required=True)
    school = db.StringField(max_length=100, required=True)
    location = db.StringField(max_length=100, required=True)
    hack_ideas = db.StringField(max_length=1000, required=True)
    experience = db.StringField(max_length=1000, required=True)
    meta = {'strict': False}

# import datetime
# from flask import url_for
from tumblelog import db


# class Comment(db.EmbeddedDocument):
#     created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
#     body = db.StringField(verbose_name="Comment", required=True)
#     author = db.StringField(verbose_name="Name", max_length=255, required=True)
    
class Post(db.Document):
    name = db.StringField(max_length=255, required=True)
    age = db.StringField(max_length=255, required=True)
    school = db.StringField(max_length=255, required=True)

    # def get_absolute_url(self):
    #     return url_for('post', kwargs={"slug": self.slug})

    # def __unicode__(self):
    #     return self.title

    # meta = {
    #     'allow_inheritance': True,
    #     'indexes': ['-created_at', 'slug'],
    #     'ordering': ['-created_at']
    # }



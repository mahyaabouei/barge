from mongoengine import Document, StringField, IntField, ListField, DateTimeField, ObjectIdField, BooleanField
from bson import ObjectId

#  است و برای ورود کاربر است NAME , MOBILE این ماژول بر اساس 

class Notifications(Document):
    _id = ObjectIdField()
    mobile = StringField()
    title = StringField()
    description = StringField()
    avatar = StringField()
    type = StringField()
    createAt = DateTimeField()
    isUnRead = DateTimeField()

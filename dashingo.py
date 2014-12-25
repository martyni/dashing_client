import datetime
from os import environ
from pymongo import MongoClient
import client

connect = MongoClient()
db = connect.dashboard
posts = db.posts
host = environ['DASHING']
my_dashboard = client.Dashing_Client(host)

class Post(object):
    '''A simple Class that will update a local mongo instance with information sent to a dashing server.\n Checs OS environment variable DASHING for a host name'''
    def __init__(self, widget, field_name, content):
        self.widget = widget
        self.field_name = field_name
        self.content = content
        self.date = datetime.datetime.utcnow()
        self.post = {
                  "widget" : self.widget,
                  "field_name" : self.field_name,
                  "content" : self.content,
                  "date" : self.date
                    }
        my_dashboard.update_widget(self.widget, self.field_name, self.content)
        post_id = posts.insert(self.post)
        print post_id
    


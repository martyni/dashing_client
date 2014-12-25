import datetime
from pymongo import MongoClient
import client

connect = MongoClient()
db = connect.dashboard
posts = db.posts
my_dashboard = client.dashing_client('162.209.75.138')

class Post(object):
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
    


from pymongo import MongoClient
from bottle import route, run, template

connect = MongoClient()
db = connect.dashboard
posts = db.posts

@route('/posts')
def all_posts():
    '''Webserver currently does nothing more than check all the posts on a local mongo db installation and display them on port 8080'''
    posts_list = []
    for post in posts.find():
        posts_list.append('<h1>' + post['widget'] + '</h1>')
        posts_list.append('<h2>' + post['field_name'] + '</h2>')
        posts_list.append('<p>' + post['content'] + '</p>')
        posts_list.append('<p>' + str(post['date']) + '</p>')
    return posts_list

run(host='localhost', port=8080)

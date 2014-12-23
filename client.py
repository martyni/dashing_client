import requests

class dashing_client(object):
    def __init__(self, host, port, token, secure=False):
        self.host = host
        self.port = port
        self.token = token
        self.secure = secure
        if secure:
            self.url = 'https://%s:%s/widgets/' % (host, port)
        else:
            self.url = 'http://%s:%s/widgets/' % (host, port)
        

    def update_widget(self, widget, field_name, content):
        data = {"auth_token": self.token, 
                 field_name : content}
        widget_url = self.url + widget
        r = requests.post(widget_url, data=data)
        print r
        return r


 
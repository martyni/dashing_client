import requests
import json

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
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        widget_url = self.url + widget
        r = requests.post(widget_url,headers=headers, data=json.dumps(data))
        return r


 

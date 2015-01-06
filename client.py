import requests
import json

class Dashing_Client(object):
    '''Extendable simple class for connecting with a dashings instace.\nBy default you just need to provide the hostname/ip address to connect on default 3030 port with no configured authentication'''
    def __init__(self, host, dashboard='sample', port='3030', token='YOUR_AUTH_TOKEN', secure=False):
        self.host = host
        self.port = port
        self.token = token
        self.secure = secure
        self.dashboard = dashboard
        if secure:
            self.url = 'https://%s:%s/widgets/' % (host, port)
        else:
            self.url = 'http://%s:%s/widgets/' % (host, port)
        

    def update_widget(self, widget, field_name, content):
        '''Update widget at the dashing server you've connected to.\nUpdate single field name with content of your choice. Requests object is returned, no tests are carried out to ensure success'''
        data = {"auth_token": self.token, 
                 field_name : content}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        widget_url = self.url + widget
        r = requests.post(widget_url,headers=headers, data=json.dumps(data))
        return r


 

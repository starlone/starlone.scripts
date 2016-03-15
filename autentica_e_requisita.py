#!/opt/intranet/core/vpython2.4/bin/python
#-*- coding: utf-8 -*-

# We need URL encode method
from urllib import urlencode
# We need URL encode method
from urllib2 import HTTPCookieProcessor
from urllib2 import HTTPRedirectHandler
from urllib2 import build_opener

class Backend(object):
    def __init__(self):
        cookie_handler= HTTPCookieProcessor()
        redirect_handler= HTTPRedirectHandler()
        self._opener = build_opener(redirect_handler, cookie_handler)
        self.last_page = None

    def get(self, url):
        self.last_page = self._opener.open(url).read()
        return self.last_page

    def post(self, url, parameters):
        self.last_page = self._opener.open(url, urlencode(parameters)).read()
        return self.last_page

backend = Backend()

url_login = 'http://www.example.com/login'

backend.get(url_login)
backend.post(url_login, {
    'login': 'usuario',
    'password': 'senha'
})

url = 'http://www.example.com'
r = backend.get(url)
print r

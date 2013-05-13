# -*- coding: utf-8 -*-

import requests
import time,hashlib
import urllib, base64

api_url = "http://api.allocine.fr/rest/v3/showtimelist"

user_agent = {"User-agent":"Dalvik/1.6.0 (Linux; U; Android 4.0.3; GT-P3100 Build/IML74K)"}

partner_key = "100043982026"

secret_key = "29d185d98c984a359e6e6f26a0474269"

theater = "B2619"

export_format = "json"

url_parameters = []
url_parameters.append(('partner', partner_key))
url_parameters.append(('format',export_format)) 
url_parameters.append(('theaters', theater))
url_parameters.append(('sed', time.strftime("%Y%m%d")))
url_parameters.append(( 'sig' ,base64.b64encode(hashlib.sha1(secret_key+urllib.urlencode(url_parameters)).digest()).rstrip("=")+"="))

req = requests.get(api_url,params=url_parameters, headers = user_agent )

print req.url

print req.text

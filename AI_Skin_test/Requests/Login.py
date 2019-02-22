import httplib
import json


user_email = 'c@163.com'
user_password = '123'
user_form = {'email': user_email, 'password': user_password}

user_form_json = json.dumps(user_form)

conn = httplib.HTTPConnection("127.0.0.1:5000")
conn.request(method="POST",body=user_form_json,url='/login')

response = conn.getresponse()

print response.read()
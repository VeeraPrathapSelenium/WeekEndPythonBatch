import requests

baseuri="https://reqres.in/api/users?page=2"
response=requests.get(baseuri)

respcode=response.status_code

assert respcode==200,"Falure in connecting"

print(response.content)






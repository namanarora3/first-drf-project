import requests

endpoint = "http://localhost:8000/api/"
get_response = requests.post(endpoint,params = {'abc':'xyz'},json = {"title": "serializer.save testing"})

# print(get_response.text)
# print(get_response.status_code)
# print(get_response.json()['message'])
print(get_response.json())
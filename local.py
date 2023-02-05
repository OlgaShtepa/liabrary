import requests


headers = {'Content-Type': 'application/json'}
response = requests.put("http://127.0.0.1:5000/api/courses/4", json={"name": "SCC", "videos": 5}, headers=headers)

print(response.json())

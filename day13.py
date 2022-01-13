import requests
import json
import os

reponame = input("enter repo name what you want to create")
GITHUB_API_URL =  "https://api.github.com/"
token = os.environ.get("token")
headers = {"Authorization": "token {}".format(token)}
data = {"name": "{}".format(reponame)}

r = requests.post(GITHUB_API_URL +"user/repos" + "", data=json.dumps(data), headers=headers)
print(token)
print(r)
import requests



data = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
print (data)
print(data.content)

import requests

g = requests.get("https://2314.tk/api")
p = requests.post("https://2314.tk/api")

print(g.text)
print(p.text)
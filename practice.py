import requests

api_key = "d7b692f0-9569-48c8-9205-cef3b55b29ee"
word = "potato"
url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"

res = requests.get(url)

definations = res.json()

print(definations)

for defination in definations:
    print(defination)

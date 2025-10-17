import requests
city = input("Введите название вашей попмйки в которой вы живете:")
url = f"https://wttr.in//{city}"
settings = {"n": "","lang": "ru"
    }

response = requests.get(url, params = settings)
response.raise_for_status()
print(response.text)
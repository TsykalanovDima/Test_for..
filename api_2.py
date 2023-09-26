import requests

url = "https://themeforest.net/"

response = requests.get(url)

if response.status_code == 200:
    with open("webpage.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("Сохранено в  'webpage.html'.")
else:
    print(f"Ошибка: {response.status_code}")

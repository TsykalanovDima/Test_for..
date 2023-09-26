import requests

url = "https://themeforest.net/"

response = requests.get(url)
if response.status_code == 200:
    print("Страница успешно загружена (код 200)")
else:
    print(f"Произошла ошибка. Код состояния: {response.status_code}")

headers = response.headers
print("\nЗаголовки ответа:")
for key, value in headers.items():
    print(f"{key}: {value}")






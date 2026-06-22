import requests


url = "https://www.programathor.com.br/jobs"

response = requests.get(url, timeout=20)

print("Status da página:", response.status_code)
print("Tamanho do HTML:", len(response.text))
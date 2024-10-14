print("\nImportação e uso de um módulo de terceiro")
import requests

url = "http://www.example.com"
response = requests.get(url)
print(f"Solicitação HTTP para {url} retornou o status {response.status_code}")
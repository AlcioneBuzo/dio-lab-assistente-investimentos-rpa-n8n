
import requests
from bs4 import BeautifulSoup

url = "https://digitalinnovationone.github.io/dio-lab-assistente-investimentos-rpa-n8n/"

resposta = requests.get(url, timeout=20)
resposta.raise_for_status()

soup = BeautifulSoup(resposta.text, "html.parser")
linhas = soup.select("#clientes tbody tr")

clientes = []

for linha in linhas:
    colunas = linha.find_all("td")

    cliente = {
        "nome": colunas[0].get_text(strip=True),
        "email": colunas[1].get_text(strip=True),
        "saldo": colunas[2].get_text(strip=True),
        "perfil": colunas[3].get_text(strip=True)
    }

    clientes.append(cliente)

print("Clientes encontrados:", len(clientes))

for cliente in clientes:
    print(cliente)


webhook_url = "http://localhost:5678/webhook-test/Clientes"

envio = requests.post(
    webhook_url,
    json={"clientes": clientes},
    timeout=20
)

print("Status do envio:", envio.status_code)
print("Resposta:", envio.text)

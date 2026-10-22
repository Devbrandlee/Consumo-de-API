import os
import pprint

import requests

api_key = os.getenv("WEATHER_API_KEY")
link_api = "https://api.weatherapi.com/v1/current.json"


#Meu dicionário informações que a API precisa pra rodar 
parametros = {
    "key": api_key,
    "q": "Rio de Janeiro",
    "lang": "pt"
}


#forecast é o clima atual

if not api_key:
    raise RuntimeError("Defina a variável de ambiente WEATHER_API_KEY antes de executar.")

resposta = requests.get(link_api, params=parametros, timeout=10)

print(resposta)
print(resposta.content) #saber o motivo do erro

if resposta.status_code == 200:
    dados_requisicao = resposta.json()
    pprint.pprint(dados_requisicao)
    temp = dados_requisicao["current"]["temp_c"]
    descricao = dados_requisicao["current" ]["condition"]["text"]
    print(temp)
    print(descricao)


# 200 deu certo a requisição
# 300 redirecionada
# 400 não conseguiu fazer a requisição
# 500 deu erro no sistema 


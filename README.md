# Estudo de consumo de API de clima

Este projeto é um exercício de estudos sobre consumo de APIs em Python. O script faz uma requisição à [WeatherAPI](https://www.weatherapi.com/) para consultar o clima atual do Rio de Janeiro e exibe:

- o status da resposta HTTP;
- o conteúdo retornado pela API;
- a temperatura em graus Celsius;
- a descrição das condições climáticas em português.

## Como funciona

1. A biblioteca `requests` envia uma requisição `GET` para o endpoint de clima atual.
2. Os parâmetros informam a chave da API, a cidade e o idioma da resposta.
3. O JSON retornado é convertido para um dicionário Python.
4. O programa acessa os campos de temperatura e condição climática.
5. O status HTTP `200` indica que a requisição foi concluída com sucesso.

## Como executar

### 1. Instale a dependência

```bash
pip install -r requirements.txt
```

### 2. Configure sua chave da WeatherAPI

No PowerShell:

```powershell
$env:WEATHER_API_KEY = "sua-chave-aqui"
```

No Linux ou macOS:

```bash
export WEATHER_API_KEY="sua-chave-aqui"
```

### 3. Execute o script

```bash
python Clima.py
```

A chave fica em uma variável de ambiente para não ser publicada no GitHub junto com o código.

## Conceitos praticados

- requisições HTTP com `requests`;
- parâmetros de consulta (`query parameters`);
- leitura de respostas JSON;
- códigos de status HTTP;
- acesso a dados aninhados em dicionários;
- uso de variáveis de ambiente para configuração sensível.
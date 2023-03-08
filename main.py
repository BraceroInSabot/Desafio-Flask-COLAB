import uvicorn
import nest_asyncio
import pandas as pd
import json
from pyngrok import ngrok
from fastapi import FastAPI
from pprint import pprint

app = FastAPI()

dados = pd.read_excel("dados.xlsx")
print("         ARQUIVO dados.xlsx\n")
print(dados, "\n")

dados_json = dados.to_json(orient="records")
parsed = json.loads(dados_json)
json.dumps(parsed, indent=4)
pprint(parsed)


@app.get("/index")
async def index():
    return parsed


ngrok_tunnel = ngrok.connect(8000)
print("PUBLIC URL: ", ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)

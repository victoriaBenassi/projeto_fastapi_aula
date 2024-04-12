import uvicorn #rodar o servidor
from fastapi import FastAPI

app = FastAPI() # criando objeto

@app.get("/exemplo")
def example() -> str: #função
    return "Olá Mundo"

if __name__ == "__main__":
    uvicorn.run(app, port=8087)
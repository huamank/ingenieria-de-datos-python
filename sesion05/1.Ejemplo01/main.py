from fastapi import FastAPI

# Cracion de la aplicacion FastAPI

app = FastAPI(title="Mi primera API")


@app.get("/")
def home() -> dict:
    return {"mensaje": "Hola desde FastAPI"}


@app.get("/saludar/{nombre}")
def saludo(nombre: str) -> dict:
    return {"mensaje": f"Hola {nombre}, Bienvenido a mi primera API"}
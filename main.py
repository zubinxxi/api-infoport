from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes.home import router as router_home
from routes.movies import router as movies_router

# 1. Desactivar docs predeterminados al crear la app
#app = FastAPI(docs_url=None, redoc_url=None)
app = FastAPI()

# Montar carpeta estática
app.mount("/static", StaticFiles(directory="static"), name="static")
app.title = "API - INFOPORT"
app.version = "1.0.0"
app.description = "Esta es una API de ejemplo creada con FastAPI"


app.openapi_tags = [
    {
        "name": "Home",
        "description": "Rutas de inicio y bienvenida",
    },
    {
        "name": "Movies",
        "description": "Rutas relacionadas con películas",
    },                                  
]

app.swagger_ui_parameters = {
    "syntaxHighlight": {"theme": "obsidian",}
}

#@app.get("/docs", include_in_schema=False)
#async def custom_swagger_ui_html():
#    return get_swagger_ui_html(
#        openapi_url=app.openapi_url,
#        title="Mi API con FastAPI",
#        # 3. Define aquí la URL de tu icono (relativa o absoluta)
#        swagger_favicon_url="/static/favicon.jpg", 
#        # Si usas local: swagger_favicon_url="/static/favicon.png"
#    )

app.include_router(router_home)
app.include_router(movies_router)
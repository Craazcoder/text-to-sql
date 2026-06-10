from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import query, schema, health

app = FastAPI(title="Text-to-SQL API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query.router)
app.include_router(schema.router)
app.include_router(health.router)
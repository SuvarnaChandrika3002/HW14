from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import engine, Base
from app.routers.users import router as users_router
from app.routers.calculations import router as calculations_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(users_router)
app.include_router(calculations_router)

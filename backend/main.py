from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import users, calculations

Base.metadata.create_all(bind=engine)

app = FastAPI()

# ----------------------------
# CORS FIX (must be added)
# ----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          
    allow_credentials=True,
    allow_methods=["*"],          
    allow_headers=["*"],          
)

# ----------------------------
# Routers
# ----------------------------
app.include_router(users.router)
app.include_router(calculations.router)

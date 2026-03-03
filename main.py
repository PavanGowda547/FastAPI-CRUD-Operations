from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database import engine, Base
from routers import users

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
def root():
    return RedirectResponse(url="/users")
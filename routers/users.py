from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import session, get_db
import models


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
def read_users(
    request : Request,
    db : Session = Depends(get_db)
):
    users = db.query(models.User).all()
    return templates.TemplateResponse(
        "Index.html",
        {
            "request":request,
            "users":users
        }
    )

# Create User form
@router.get("/create")
def create_user_form(request : Request):
    return templates.TemplateResponse(
        "create.html",
        {
            "request":request
        }
    )

@router.post("/create")
def create_user(
    name : str = Form(...),
    email : str = Form(...),
    db : Session = Depends(get_db)
):
    user = models.User(name=name, email=email)
    db.add(user)
    db.commit()
    return RedirectResponse(url="/users",status_code=303)


#Update user Form
@router.get("/update/{user_id}")
def update_user_form(
    user_id : int,
    request : Request,
    db : Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, details="User not found")
    return templates.TemplateResponse(
        "update.html",
        {
            "request":request,
            "user": user
        }
    )

@router.post("/update/{user_id}")
def update_user(
    user_id : int,
    name : str = Form(...),
    email : str = Form(...),
    db : Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, details="User not found")
    user.name = name
    user.email = email
    db.commit()
    return RedirectResponse(url="/users",status_code=303)

@router.get("/delete/{user_id}")
def delete_user(
    user_id : int,
    db : Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    db.delete(user)
    db.commit()
    return RedirectResponse(url="/users",status_code=303)



    
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, Users
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="web_app"), name="static")

@app.get('/')
def autoriz_win():
    return FileResponse('web_app/autoriz.html')

@app.post('/autorizatoin/')
def autorizaton(login: str, password: str, db: Session=Depends(get_db)):
    user = db.query(Users).filter((Users.email_phone==login)&(Users.password==password)).first()
    if user is None:
        return JSONResponse(status_code=404, content='Пользователь не найден')
    else:
        return user
    
@app.get('/registration')
def registration():
    return FileResponse('web_app/registration.html')

@app.get('/account')
def account():
    return FileResponse('web_app/main_win.html')

@app.get('/automats')
def automats():
    return FileResponse('web_app/automats.html')

@app.get('/documents')
def documents():
    return FileResponse('web_app/documents.html')
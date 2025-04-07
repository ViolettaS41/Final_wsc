from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, Users
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/autorizatoin/')
def autorizaton(login: str, password: str, db: Session=Depends(get_db)):
    user = db.query(Users).filter((Users.email_phone==login)&(Users.password==password)).first()
    if user is None:
        return JSONResponse(status_code=404, content='Пользователь не найден')
    else:
        return user
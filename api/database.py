from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL='mysql://root:1397Sql2486!@localhost/automat'
engine = create_engine(URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

class Users(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(200))
    email_phone = Column(String(100))
    role = Column(String(100))
    password = Column(String(45))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
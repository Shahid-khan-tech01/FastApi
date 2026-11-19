# SQL Alchemy is a python lib used to connect py apps with db and perfroms db opertions :

from sqlalchemy import Integer, create_engine, Column, String
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from fastapi import FastAPI, Depends
app = FastAPI()

Database_url = "sqlite:///./test.db"

engine = create_engine(
    Database_url,
    connect_args={"check_same_thread": False}
)
sessionlocal = sessionmaker(bind=engine)
Base = declarative_base()

class Todos(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionlocal()
    try:
        yield
    finally:
        db.close()

@app.get("/")
def home(db: Session = Depends(get_db)):
    return {
          "message": "DB connected fine"
    }
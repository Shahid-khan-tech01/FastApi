from sqlalchemy import Integer, create_engine, Column, String
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

# Database URL :
Database_url = "sqlite:///./test.db"

# Engine Creation (DB Connection) :
engine = create_engine(
    Database_url,
    connect_args={"check_same_thread": False}
)

# Session for DB opertions :
sessionlocal = sessionmaker(bind=engine)

# Base Model :
Base = declarative_base()

# Table Model :
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)

Base.metadata.create_all(bind=engine)

# Dependency session creation :
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

# CREATE API :
@app.post("/todos")
def create_todo(title:str, db: Session=Depends(get_db)):
    todo = Todo(title=title, completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message": "Todo is Created",
        "data": todo 
    }

# READ All Data:
@app.get("/todos")
def get_todos(db: Session=Depends(get_db)):
    todos = db.query(Todo).all()
    return {
        "Total": len(todos),
        "data": todos
    }

# Read data Based on ID :
@app.get("/todos/{todo_id}")
def get_todo(todo_id=int, db: Session=Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo Not Found")
    return todo

# Update Data Based on id :
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,title:str, db: Session=Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo Not Found")
    
    todo.title = title
    db.commit()
    db.refresh(todo)
    return {"message": "Todo Updated Succesfully",
            "data": todo
    }

# Delete API:
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:str, db: Session=Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo Not Found") 
    
    db.delete(todo)
    db.commit()
    return {"message": "Todo Deleted Succesfully",
                "data": todo
        }
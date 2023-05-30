from fastapi import FastAPI
from Database.getEngine import SessionLocal, db_engine;
from Database.Models import models
app = FastAPI();

models.Base.metadata.create_all(bind=db_engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




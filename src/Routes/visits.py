from pydantic import Json;
from Database.getEngine import SessionLocal;
from fastapi import APIRouter, Depends, HTTPException;
from sqlalchemy.orm import Session;
from Database.Queries import crud;

router = APIRouter(prefix = "/Users");

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close();
from pydantic import Json;
from Database.getEngine import SessionLocal;
from fastapi import APIRouter, Depends, HTTPException;
from sqlalchemy.orm import Session;
from Database.Schemas import schema;
from Database.Queries import crud;

router = APIRouter(prefix = "/Users");

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close();


@router.post("/Create", response_model= schema.User)
async def create(user: schema.UserCreate, db: Session = Depends(get_db)):

    if crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered");
    return crud.create_user(db, user);


@router.post("/setVisit", response_model= schema.Visit)
async def reserve(visitDesc: schema.VisitCreate, db: Session = Depends(get_db)):
    return crud.set_visit(db, visitDesc);


@router.get("/Visits/{userID}", response_model= list[schema.Visit])
async def get_user_visits(userID: str, db: Session = Depends(get_db)):
    return crud.get_user_visits(db, userID);


@router.post("/VisitComment", response_model= schema.Visit)
async def set_comment_for_visit(visitDesc: schema.VisitSetComment, db: Session = Depends(get_db)):
    return crud.set_comment_for_visit(db, visitDesc);


@router.get("/All", response_model= list[schema.User])
async def get_all_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db);
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


@router.post("/Create")
async def create(user: Json, db: Session = Depends(get_db)):

    if crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered");
    createdUser = crud.create_user(db, user);
    return {"Status": 200, "payload": createdUser};


@router.post("/setVisit")
async def reserve(visitDesc: Json, db: Session = Depends(get_db)):
    reserved = crud.set_visit(db, visitDesc);
    return {"Status": 200, "Payload": reserved};


@router.get("/Visits/{userID}")
async def get_user_visits(userID, db: Session = Depends(get_db)):
    visits = crud.get_user_visits(db, userID);
    return {"Status": 200, "Payload": visits};


@router.post("/VisitComment")
async def set_comment_for_visit(visitDesc, db: Session = Depends(get_db)):
    visit = crud.set_comment_for_visit(db, visitDesc);
    return {"Status": 200, "Payload": visit};


@router.get("/All")
async def get_all_users(db: Session = Depends(get_db)):
    allUsers = crud.get_all_users(db);
    return {"Status": 200, "Payload": allUsers};
from pydantic import Json;
from Database.getEngine import SessionLocal;
from Database.Schemas import schema;
from fastapi import APIRouter, Depends, HTTPException;
from sqlalchemy.orm import Session;
from Database.Queries import crud;

router = APIRouter(prefix= "/Doctors");

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close();


@router.post("/Create", response_model=  schema.Doctor)
async def create(doctor: schema.DoctorCreate, db: Session = Depends(get_db)):
    if crud.get_doctor_by_email(db, doctor.email):
        raise HTTPException(status_code=400, detail="Email already registered");
    return crud.create_doctor(db, doctor);


@router.get("/Patients/{doctorID}", response_model= list[schema.User])
async def get_doctor_patients(doctorID: str, db: Session = Depends(get_db)):
    return crud.get_doctor_patients(db, doctorID);


@router.get("/All", response_model= list[schema.Doctor])
async def get_all_doctors(db: Session = Depends(get_db)):
    return crud.get_all_doctors(db);


@router.get("/Visits/{doctorID}", response_model= list[schema.Visit])
async def get_doctor_visits(doctorID: str, db: Session = Depends(get_db)):
    return crud.get_doctor_visits(db, doctorID);


@router.get("/AllinCity/{cityName}", response_model= list[schema.Doctor])
async def get_doctors_by_city(cityName: str, db: Session = Depends(get_db)):
    return crud.get_doctors_by_city(db, cityName);

from pydantic import Json;
from Database.getEngine import SessionLocal;
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


@router.post("/Create")
async def create(doctor: Json, db: Session = Depends(get_db)):
    if crud.get_doctor_by_email(db, doctor.email):
        raise HTTPException(status_code=400, detail="Email already registered");
    createdUser = crud.create_doctor(db, doctor);
    return {"Status": 200, "payload": createdUser};


@router.get("/Patients/{doctorID}")
async def get_doctor_patients(doctorID, db: Session = Depends(get_db)):
    pationts = crud.get_doctor_patients(db, doctorID);
    return {"Status": 200, "Payload": pationts};


@router.get("/All")
async def get_all_doctors(db: Session = Depends(get_db)):
    allDoctors = crud.get_all_doctors(db);
    return {"Status": 200, "Payload": allDoctors};


@router.get("/Visits/{doctorID}")
async def get_doctor_visits(doctorID, db: Session = Depends(get_db)):
    allVisits = crud.get_doctor_visits(db, doctorID);
    return {"Status": 200, "Payload": allVisits};


@router.get("/AllinCity/{cityName}")
async def get_doctors_by_city(cityName, db: Session = Depends(get_db)):
    allDoctorsInCity = crud.get_doctors_by_city(db, cityName);
    return {"Status": 200, "Payload": allDoctorsInCity};

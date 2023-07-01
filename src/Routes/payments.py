from pydantic import Json;
from Database.getEngine import SessionLocal;
from fastapi import APIRouter, Depends, HTTPException;
from sqlalchemy.orm import Session;
from Database.Queries import crud;
from Database.Schemas import schema;
router = APIRouter(prefix = "/Payments");

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close();


@router.get('/All', response_model= list[schema.Payments])
async def getAllPayments(db: Session = Depends(get_db)):
    return crud.get_all_payments(db);


@router.post('/PayVisit', response_model= schema.Payments)
async def payVisit(payment: schema.PaymentsCreate, db: Session = Depends(get_db)):
    visit = crud.get_visit_byID(db, payment.visitID);
    if(not visit):
        raise HTTPException(status_code=404, detail="There is no visit with this ID");
    else:
        return crud.pay_visit(db, payment);





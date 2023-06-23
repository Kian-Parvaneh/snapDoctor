from pydantic import Json;
from ..Schemas import schema;
from ..Models import models;
from sqlalchemy.orm import Session;

def get_user_by_email(db: Session, email: str):
    return db.query(models.Users).filter(models.Users.email == email).first();    

def get_doctor_by_email(db: Session, email: str):
    return db.query(models.Doctors).filter(models.Doctors.email == email).first();

def get_all_doctors(db: Session):
    return db.query(models.Doctors).all();

def get_doctors_by_city(db: Session, cityName: str):
    return db.query(models.Doctors).filter(models.Doctors.city.name == cityName);

def get_all_users(db: Session):
    return db.query(models.Users).all();

############Problem############
def get_doctor_patients(db: Session, doctorID: str):
    return db.query(models.Users).filter(models.Visits.doctorID == doctorID).filter(models.Users.id == models.Visits.userID).all();

def get_doctor_visits(db: Session, doctorID: str):
    return db.query(models.Visits).filter(models.Visits.doctorID == doctorID).all();


def get_user_visits(db: Session, userID: str):
    return db.query(models.Visits).filter(models.Visits.userID == userID).all();

def create_user(db: Session, user: schema.UserCreate):
    userModel = models.Users(name = user.name, age = user.age, email = user.email ,
                    password = user.password, address = user.address, phonenumber = user.phonenumber, city = get_cityID(db, user.city));
    db.add(userModel);
    db.commit();
    db.refresh(userModel);
    return userModel;

def create_doctor(db: Session, doctor: schema.DoctorCreate):
    print(doctor);
    doctorModel = models.Doctors(name = doctor.name, email = doctor.email , specialization = doctor.specialization,
                    password = doctor.password, city = get_cityID(db, doctor.city), address = doctor.address);
    db.add(doctorModel);
    db.commit();
    db.refresh(doctorModel);
    return doctorModel;


def set_visit(db: Session, visitDesc: schema.VisitCreate):
    visitModel = models.Visits(userID = visitDesc.userID, doctorID = visitDesc.doctorID,
                                date = visitDesc.date, price = visitDesc.price);
    db.add(visitModel);
    db.commit();
    db.refresh(visitModel);
    return visitModel;

def set_comment_for_visit(db: Session, visitDesc: Json):
    db.query(models.Visits).filter(models.Visits.id == visitDesc.id).update({"comment": visitDesc.comment});
    db.commit();
    return db.query(models.Visits).filter(models.Visits.id == visitDesc.id).first();


def add_city(db: Session, city: schema.CityCreate):
    cityModel = models.City(province = city.province, name = city.name);
    db.add(cityModel);
    db.commit();
    db.refresh(cityModel);
    return cityModel;

def get_cityID(db: Session, cityName: str):
    dbCity = db.query(models.City).filter(models.City.name == cityName).first();
    if(dbCity):
        return dbCity.id;
    return None;

def get_citys(db: Session):
    citys = db.query(models.City).all();
    return citys;

from pydantic import BaseModel;


class VisitsBase(BaseModel):
    userID: int;
    doctorID: int;
    price: str;
    date: str;
class VisitCreate(VisitsBase):
    pass;
class VisitSetComment(BaseModel):
    userID: int;
    comment: str;
class Visit(VisitsBase):
    id : int;
    comment: str | None = None;
    class Config:
        orm_mode = True;


class UsersBase(BaseModel):
    email: str;
    phonenumber: str;
    name: str | None = None;
    age: int | None = None;
    address: str | None = None;
    city: int | None = None;
class UserCreate(UsersBase):
    password: str;
class User(UsersBase):
    id: int;
    reserved: list[Visit] = [];
    class Config:
        orm_mode = True;


class DoctorsBase(BaseModel):
    email: str;
    name: str | None = None;
    specialization: str | None = None;
    address: str | None = None;
    city: int | None = None;
class DoctorCreate(DoctorsBase):
    password: str;
class Doctor(DoctorsBase):
    id: int;
    patients: list[Visit] = [];
    class Config:
        orm_mode = True;


class CityBase(BaseModel):
    province: str;
    name: str;
class CityCreate(CityBase):
    pass;
class City(CityBase):
    id: int;
    class Config:
        orm_mode = True;



class PaymentsBase(BaseModel):
    visitID: int;
    date: str;
    price: str;
class PaymentsCreate(PaymentsBase):
    pass;
class Payments(PaymentsBase):
    id: int;
    bankName: str | None = None;
    class Config:
        orm_mode = True;
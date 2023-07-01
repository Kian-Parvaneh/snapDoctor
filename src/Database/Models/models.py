from ..getEngine import Base;
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Doctors(Base):
    __tablename__ = "Doctors";
    id = Column(Integer, primary_key=True, index=True, autoincrement = "auto");
    name = Column(String(100));
    specialization = Column(String(100), default= "PublicHealth");
    email = Column(String(100), unique=True, nullable=False);
    password = Column(String(250), nullable=False);
    address = Column(String(300));
    patients = relationship("Visits", back_populates="doctor");
    city = Column(Integer, ForeignKey("City.id"));
    


class Users(Base):
    __tablename__= "Users";
    id = Column(Integer, primary_key=True, index=True);
    name = Column(String(100));
    age = Column(String(3));
    email = Column(String(100), unique=True, nullable=False);
    password = Column(String(250),nullable=False);
    phonenumber = Column(String(15), nullable=False)
    address = Column(String(300));
    reserved = relationship("Visits", back_populates="user");
    city = Column(Integer, ForeignKey("City.id"));


class Visits(Base):
    __tablename__ = "Visits";
    id = Column(Integer, primary_key=True, index=True);
    comment = Column(String(300));
    date = Column(String(100), nullable=False);
    price = Column(String(10), nullable=False);
    userID = Column(Integer, ForeignKey("Users.id"), nullable=False);
    user = relationship("Users", back_populates="reserved");
    doctorID = Column(Integer, ForeignKey("Doctors.id"), nullable=False);
    doctor = relationship("Doctors", back_populates="patients");


class City(Base):
    __tablename__ = "City";
    id = Column(Integer, primary_key=True, index=True);
    province = Column(String(20), nullable=False)
    name = Column(String(20), unique=True, nullable=False);


class Payments(Base):
    __tablename__ = "Payments";
    id = Column(Integer, primary_key=True, index=True);
    paymentsDate = Column(String(100),nullable=False);
    bankName = Column(String(15));
    # paid = Column(Boolean, default=False);
    visitID = Column(Integer, ForeignKey("Visits.id"));
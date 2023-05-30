from ..getEngine import Base;
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Doctors(Base):
    __tablename__ = "Doctors";
    id = Column(Integer, primary_key=True, index=True);
    name = Column(String(100));
    specialization = Column(String(100));
    email = Column(String(100), unique=True);
    password = Column(String(250));
    address = Column(String(300));
    patients = relationship("Visits", back_populates="doctor")


class Users(Base):
    __tablename__= "Users";
    id = Column(Integer, primary_key=True, index=True);
    name = Column(String(100));
    email = Column(String(100), unique=True);
    password = Column(String(250));
    address = Column(String(300));
    reserved = relationship("Visits", back_populates="user")


class Visits(Base):
    __tablename__="Vists";
    id = Column(Integer, primary_key=True, index=True);
    description = Column(String(300));
    userID = Column(Integer, ForeignKey("Users.id"));
    user = relationship("Users", );
    doctorID = Column(Integer,ForeignKey("Doctors.id"));
    doctor = relationship("Doctors",back_populates="patients");





from ..getEngine import Base;
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Doctors(Base):
    __tablename__ = "Doctors";
    id = Column(Integer, primary_key=True, index=True);
    name = Column(String);
    specialization = Column(String);
    email = Column(String, unique=True);
    password = Column(String);
    address = Column(String);
    patients = relationship("Visits", back_populates="doctor")


class Users(Base):
    __tablename__= "Users";
    id = Column(Integer, primary_key=True, index=True);
    name = Column(String);
    email = Column(String, unique=True);
    password = Column(String);
    address = Column(String);
    reserved = relationship("Visits", back_populates="user")


class Visits(Base):
    __tablename__="Vists";
    id = Column(Integer, primary_key=True, index=True);
    description = Column(String);
    userID = Column(Integer, ForeignKey("Users.id"));
    user = relationship("Users", );
    doctorID = Column(Integer,ForeignKey("Doctors.id"));
    doctor = relationship("Doctors",back_populates="patients");





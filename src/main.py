from fastapi import FastAPI;
from Database.getEngine import  db_engine;
from Database.Models import models;
from Routes.MainRoutes import DoctorRoutes, UserRoutes, VisitRoutes;
app = FastAPI();

models.Base.metadata.create_all(bind=db_engine);


app.include_router(DoctorRoutes);
app.include_router(UserRoutes);
app.include_router(VisitRoutes);
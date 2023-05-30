import os;
from sqlalchemy import create_engine;
from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy.orm import sessionmaker;


MYSQL_HOSTNAME = os.getenv("MYSQL_HOSTNAME");
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD");
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE");
db_engine = create_engine(f"mysql+mysqlconnector://<root>:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:3306/{MYSQL_DATABASE}",echo=True);


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine);

Base = declarative_base();







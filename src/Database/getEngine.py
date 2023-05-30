from dotenv import dotenv_values;
from sqlalchemy import create_engine;
from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy.orm import sessionmaker;
env = dotenv_values('../.env');
db_engine = create_engine(f"mysql+mysqlconnector://root:{env['MYSQL_PASSWORD']}@{env['MYSQL_HOSTNAME']}:3306/{env['MYSQL_DATABASE']}",echo=True);


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine);

Base = declarative_base();







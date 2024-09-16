from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://shravan_projectpart3_user:FDJRnByrUKz3YOP4Pqg8labgpegwg7jb@dpg-crdh2fd6l47c73aumjk0-a.oregon-postgres.render.com/shravan_projectpart3" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

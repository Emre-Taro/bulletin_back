from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "https://gfsgurkfbtbnlgyfrynh.supabase.co"

engine = create_engine(DATABASE_URL, connect_args={"Check_same_thread":False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 
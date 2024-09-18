from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import SQLALCHEMY_DATABASE_URL

# Create the engine for an sqlalchemy high level conection to the postgresql database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creates a session maker reference to the engine
SessionLocal = sessionmaker(bind=engine)

# function to create a session to the database
def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
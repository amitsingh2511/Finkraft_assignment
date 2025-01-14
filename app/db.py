# Required imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Database URL for connecting to PostgreSQL
DATABASE_URL = "postgresql://postgres:8969037429@localhost/booking_db"

# SQLAlchemy engine for database interaction
engine = create_engine(DATABASE_URL)

# SessionLocal provides scoped sessions for database operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is used to define ORM models
Base = declarative_base()

def get_db():
    """
    Provides a database session for API endpoints.
    Ensures the session is properly closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

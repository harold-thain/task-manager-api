from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# This is the one line that changes when we switch to MySQL later.
# SQLite just needs a file path. The file gets created automatically.
DATABASE_URL = "sqlite:///./taskapi.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # SQLite-specific setting, not needed for MySQL
)

# A SessionLocal is a "factory" for database sessions
# Each request gets its own session — its own conversation with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class that all our database models will inherit from
class Base(DeclarativeBase):
    pass

# Base = declarative_base()
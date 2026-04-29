import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# load_dotenv()

# DB_URL = (
#     f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
#     f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
# )

# engine = create_engine(DB_URL, pool_pre_ping=True)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# Base = declarative_base()

# SQLite database file (will be created automatically)
DB_URL = "sqlite:///./test.db"

engine = create_engine(
    DB_URL,
    echo=True,  # shows SQL in terminal (great for learning)
    connect_args={"check_same_thread": False}  # needed for SQLite + FastAPI
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()
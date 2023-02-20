from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URL = "sqlite:///./sql.db"
engine = create_engine(
    DB_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

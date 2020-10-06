import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    os.getenv("SQLALCHEMY_DATABASE_URI"),
    echo=bool(os.getenv("SQLALCHEMY_DATABASE_ECHO")),
)
Base = declarative_base()
Session = sessionmaker(bind=engine)


def create_session():
    Base.metadata.create_all(engine)
    return Session()

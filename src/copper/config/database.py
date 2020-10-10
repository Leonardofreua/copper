from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .settings_extractor import settings_parser

settings = settings_parser()["database"]

engine = create_engine(
    settings["sqlalchemy_database_uri"], echo=settings["sqlalchemy_database_echo"],
)
Base = declarative_base()
Session = sessionmaker(bind=engine)


def create_session():
    Base.metadata.create_all(engine)
    return Session()

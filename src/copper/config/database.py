from scrapy.utils import project
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


settings = project.get_project_settings()

database_path = settings.attributes["SQLALCHEMY_DATABASE_URI"].value
is_echo = settings.attributes["SQLALCHEMY_DATABASE_ECHO"].value

engine = create_engine(database_path, echo=is_echo)
Base = declarative_base()
Session = sessionmaker(bind=engine)


def create_session():
    Base.metadata.create_all(engine)
    return Session()

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///./database.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class MovieDB(Base):
    __tablename__ = 'movies'
    movieId = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    genres = Column(String)

class LinkDB(Base):
    __tablename__ = 'links'
    movieId = Column(Integer, primary_key=True, index=True)
    imdbId = Column(String)
    tmdbId = Column(String)

class RatingDB(Base):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, index=True)
    movieId = Column(Integer, index=True)
    rating = Column(Float)
    timestamp = Column(Integer)

class TagDB(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, index=True)
    movieId = Column(Integer, index=True)
    tag = Column(String)
    timestamp = Column(Integer)

Base.metadata.create_all(bind=engine)


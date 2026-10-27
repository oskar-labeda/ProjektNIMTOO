from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, MovieDB

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/movies")
def read_movies(db: Session = Depends(get_db)):
    movies = db.query(MovieDB).all()
    return movies
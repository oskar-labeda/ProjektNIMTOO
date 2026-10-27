import csv
from database import SessionLocal, MovieDB, LinkDB, RatingDB, TagDB


def load_data():
    db = SessionLocal()

    try:
        print("Ładowanie movies.csv...")
        with open('movies.csv', encoding='utf-8') as f:
            movies = [MovieDB(movieId=int(row['movieId']), title=row['title'], genres=row['genres'])
                      for row in csv.DictReader(f)]
            db.bulk_save_objects(movies)
            db.commit()

        print("Ładowanie links.csv...")
        with open('links.csv', encoding='utf-8') as f:
            links = [LinkDB(movieId=int(row['movieId']), imdbId=row['imdbId'], tmdbId=row['tmdbId'])
                     for row in csv.DictReader(f)]
            db.bulk_save_objects(links)
            db.commit()

        print("Ładowanie ratings.csv...")
        with open('ratings.csv', encoding='utf-8') as f:
            ratings = [RatingDB(userId=int(row['userId']), movieId=int(row['movieId']),
                                rating=float(row['rating']), timestamp=int(row['timestamp']))
                       for row in csv.DictReader(f)]
            db.bulk_save_objects(ratings)
            db.commit()

        print("Ładowanie tags.csv...")
        with open('tags.csv', encoding='utf-8') as f:
            tags = [TagDB(userId=int(row['userId']), movieId=int(row['movieId']),
                          tag=row['tag'], timestamp=int(row['timestamp']))
                    for row in csv.DictReader(f)]
            db.bulk_save_objects(tags)
            db.commit()

        print("Wszystkie dane zostały pomyślnie załadowane do bazy danych!")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    load_data()
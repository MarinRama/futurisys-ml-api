from app.db.session import engine, Base
from app.db import models  # noqa: F401


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")


if __name__ == "__main__":
    create_tables()
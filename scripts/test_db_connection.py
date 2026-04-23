from sqlalchemy import text
from app.db.session import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT current_database(), current_user;"))
        row = result.fetchone()
        print(f"Connected to database: {row[0]}")
        print(f"Connected as user: {row[1]}")
except Exception as e:
    print(f"Database connection failed: {e}")
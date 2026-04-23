import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

CSV_PATH = "data/employees.csv"


def load_dataset():
    df = pd.read_csv(CSV_PATH)

    print("Dataset loaded, shape:", df.shape)

    engine = create_engine(DATABASE_URL)

    df.to_sql(
        "employees_dataset",
        engine,
        if_exists="append",  # important : append et pas replace
        index=False
    )

    print("Dataset inserted into PostgreSQL successfully.")


if __name__ == "__main__":
    load_dataset()
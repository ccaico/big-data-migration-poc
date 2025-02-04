import csv
from sqlalchemy.orm import Session
from src.database.connector import get_db
from src.api.models import  Transaction, Customer, Product

def load_csv_to_db(file_path: str, table_model):
    db = next(get_db())
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            db_record = table_model(**row)
            db.add(db_record)
        db.commit()
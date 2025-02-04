from fastapi import FastAPI, HTTPException, Path
from src.database.connector import get_db
from src.api.models import Transaction, Customer, Product
from src.api.schemas import TransactionSchema, CustomerSchema, ProductSchema
from typing import Union, List

app = FastAPI()

@app.post("/insert/{table_name}")
async def insert_data(
    table_name: str 
):
    # Validate the number of rows (1 to 100)
    if len(data) < 1 or len(data) > 100:
        raise HTTPException(status_code=400, detail="Number of rows must be between 1 and 100")

    db = next(get_db())
    try:
        # Determine the SQLAlchemy model based on the table name
        if table_name == "transactions":
            db_model = Transaction
        elif table_name == "customers":
            db_model = Customer
        elif table_name == "products":
            db_model = Product
        else:
            raise HTTPException(status_code=400, detail="Invalid table name")

        # Insert each item in the list
        for item in data:
            db_record = db_model(**item.dict())
            db.add(db_record)
        db.commit()

        return {"message": f"{len(data)} rows inserted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
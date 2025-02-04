import avro.schema
import avro.datafile
import avro.io
import os
from src.database.connector import get_db
from src.api.models import YourTableModel

def backup_table(table_name: str, backup_path: str):
    db = next(get_db())
    records = db.query(YourTableModel).all()
    schema = avro.schema.parse(open(f"schemas/{table_name}.avsc").read())
    with open(backup_path, 'wb') as f:
        writer = avro.datafile.DataFileWriter(f, avro.io.DatumWriter(), schema)
        for record in records:
            writer.append(record.__dict__)
        writer.close()
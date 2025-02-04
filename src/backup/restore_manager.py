import avro.datafile
import avro.io
from src.database.connector import get_db
from src.api.models import YourTableModel

def restore_table(backup_path: str):
    db = next(get_db())
    with open(backup_path, 'rb') as f:
        reader = avro.datafile.DataFileReader(f, avro.io.DatumReader())
        for record in reader:
            db_record = YourTableModel(**record)
            db.add(db_record)
        db.commit()
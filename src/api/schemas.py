from pydantic import BaseModel, constr, validator
from datetime import datetime

class EmployeeSchema(BaseModel):
    name: constr(max_length=100) 
    datetime: constr(max_length=25)  
    department_id: int
    job_id: int 

    @validator("datetime")
    def validate_datetime(cls, value):
        """
        Validate that the datetime string is in ISO format.
        Example: "2023-10-01T12:34:56"
        """
        try:
            datetime.fromisoformat(value)
        except ValueError:
            raise ValueError("Invalid ISO format for datetime. Expected format: YYYY-MM-DDTHH:MM:SS")
        return value

    class Config:
        orm_mode = True

class DepartamentSchema(BaseModel):
    id: int
    departament: constr(max_length=50)

    @validator("email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email format")
        return value

    class Config:
        orm_mode = True


class JobSchema(BaseModel):
    id: int
    departament: constr(max_length=50)

    @validator("stock_quantity")
    def validate_stock_quantity(cls, value):
        if value < 0:
            raise ValueError("Stock quantity must be non-negative")
        return value

    class Config:
        orm_mode = True
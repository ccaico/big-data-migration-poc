from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    datetime = Column(String(25), nullable=False)
    department_id = Column(Integer, nullable=False)
    job_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Employee(id={self.id}, name={self.name}, department_id={self.department_id}, job_id={self.job_id})>"

class Departament(Base):
    __tablename__ = "departaments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    departament = Column(String, nullable=False)
    
class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    job = Column(String, nullable=False)
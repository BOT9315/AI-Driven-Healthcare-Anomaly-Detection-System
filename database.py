from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:Ankush123@localhost/healthcare"

engine = create_engine(DATABASE_URL)
Base = declarative_base()

class PatientData(Base):
    __tablename__ = "patient_data"

    id = Column(Integer, primary_key=True)
    heart_rate = Column(Float)
    spo2 = Column(Float)
    temperature = Column(Float)
    blood_pressure = Column(Float)
    severity = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
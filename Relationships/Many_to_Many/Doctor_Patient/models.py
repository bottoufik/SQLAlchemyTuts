from datetime import datetime
from sqlalchemy import create_engine,Date, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url= "sqlite:///doctorpatient.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    patient_id = Column(Integer, ForeignKey("patients.id"))
    appointment_date = Column(Date, default=datetime.now)
    notes = Column(String)

    doctor = relationship('Doctor', backref='appointments')
    patient = relationship('Patient', backref='appointments')


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    speciality = Column(String)


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_of_birth = Column(Date)

Base.metadata.create_all(engine)
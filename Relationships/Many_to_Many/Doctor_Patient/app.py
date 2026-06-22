from models import session, Doctor, Patient, Appointment, datetime

if session.query(Appointment).count() < 1:
    dr_smith = Doctor(name='Dr. Smith', speciality='Cardiology')
    john_doe = Patient(name='John Doe', date_of_birth=datetime(1990, 1, 1))
    appointment = Appointment(
        doctor=dr_smith, patient=john_doe, notes='Routine check-up'
    )

    session.add_all([dr_smith, john_doe, appointment])
    session.commit()
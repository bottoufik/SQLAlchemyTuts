from models import session,Appointment

# Find all appointments for Dr. Smith
appointments_for_dr_smith = (
    session.query(Appointment).filter(Appointment.doctor.has(name='Dr. Smith')).all()
)
print("Dr. Smith's appointments")
print(appointments_for_dr_smith)

# Find all appointments for John Doe
appointments_for_john_doe = (
    session.query(Appointment).filter(Appointment.patient.has(name='John Doe')).all()
)

print("John Doe's appointments")
print(appointments_for_john_doe)
from sqlalchemy.orm import sessionmaker
from models import User,engine

Session = sessionmaker(bind=engine)
session = Session()

# Ascending Order
users = session.query(User).order_by(User.age).all()
for user in users:
    print(f"User Id: {user.id}, name: {user.name}, age: {user.age}")

print("---------------------------------------------------------------------")
# Descending Order
users = session.query(User).order_by(User.age.desc()).all()
for user in users:
    print(f"User Id: {user.id}, name: {user.name}, age: {user.age}")

print("---------------------------------------------------------------------")
# Multiple Orders
# Sorted by age  and for each sorted age (same age) sorted names by alphabetical order
users = session.query(User).order_by(User.age, User.name).all()
for user in users:
    print(f"User Id: {user.id}, name: {user.name}, age: {user.age}")
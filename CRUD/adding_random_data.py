import random
from sqlalchemy.orm import sessionmaker
from models import User,engine

Session = sessionmaker(bind=engine)
session = Session()

names = [
    "Rahul Sharma",
    "Rohan Mehta",
    "Ayesha Khan",
    "Priya Verma",
    "David Miller",
    "Sara Ahmed"
]
ages = [24, 31, 19, 27, 35, 22]

for i in range(6):
    user = User(name= random.choice(names), age= random.choice(ages))
    session.add(user)

session.commit()
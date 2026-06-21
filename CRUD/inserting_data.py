from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
#Create a session
session  = Session()
#Create an User
user = User(name="Md Toufik",age=30)
user_2 = User(name="Ramiz Raja", age =32)
user_3 =User(name="Richa Ghosh", age =33)
user_4 = User(name="Kin Wesler", age = 39)
# adding a single user
session.add(user)
#adding multiple users
# Note: add_all accepts a list
session.add_all([user_2,user_3,user_4])

session.commit()
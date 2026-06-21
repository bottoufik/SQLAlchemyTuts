from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

users = session.query(User).all()
# accessing users. The users will be objects
print(users)
# Accessing single user
print(users[0])

# Accessing users properties
print(users[0].id, users[0].name, users[0].age) # 1 Md Toufik 30

print(users[1].id, users[1].name, users[1].age) # 2 Ramiz Raja 32

for user in users:
    print(f"User Id: {user.id}, name: {user.name}, age: {user.age}")


# Filtering data
user = session.query(User).filter_by(id=1).all()
print(user) #Returning a list of objects

#Returning a single user object
user = session.query(User).filter_by(id=1).one_or_none()
#print(user)
print(user.id, user.name, user.age)

#Returning names starting with R
users = session.query(User).filter(User.name.like("R%")).all()
# print(users)
for user in users:
    print(user.name) # Ramiz Raja Richa Ghosh

# Returing only the first user sorted by id
user = session.query(User).filter(User.name.like("R%")).first()
print(user.name) # Ramiz Raja
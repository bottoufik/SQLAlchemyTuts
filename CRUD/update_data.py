from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

users = session.query(User).filter_by(id=1).all() # returns a single user
user = users[0]
print(user.name)
user.name = "A different name"
print(user.name)

session.commit() # Changes will be visible in the database table
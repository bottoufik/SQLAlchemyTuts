from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

users = session.query(User).filter_by(id=1).all() # returns a single user
print(users)

# deleting the entire object means deleting an entire row of data
session.delete(users[0])
session.commit()
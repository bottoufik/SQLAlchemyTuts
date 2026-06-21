from sqlalchemy.orm import sessionmaker
from models import User, engine
from sqlalchemy import func

Session = sessionmaker(bind=engine)
session = Session()

# Grouping
users = session.query(User).group_by(User.age).all()
print(users)
users_age_group = session.query(User.age).group_by(User.age).all()
print(users_age_group)
# SQL Equivalent: SELECT age FROM users GROUP BY age
users_age_count = session.query(User.age, func.count(User.id)).group_by(User.age).all()
print(users_age_count)

#Chaining

users = session.query(User).filter(User.age>30).filter(User.age<40).all()
print(users)
users_tuple = (
    session.query(User.age, func.count(User.id))
    .filter(User.age>30)
    .order_by(User.age)
    .filter(User.age<40)
    .group_by(User.age)
    .all()
)
print(users_tuple)

for age,count in users_tuple:
    print(f"Age:{age},Count:{count}")
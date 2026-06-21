from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

users_all = session.query(User).all()

# query all users with age gerater than 30
users_filtered = session.query(User).filter(User.age>=30).all()

users_above_or_just_30 = [user.name for user in users_filtered]
print(users_above_or_just_30)

selected_users = session.query(User).filter(User.age>=30,User.name.like("R%")).all()
print(len(selected_users))
selected_users_names = [user.name for user in selected_users]
print(selected_users_names)

#Using filter_by

users_with_age_nin = session.query(User).filter_by(age=19).all()
users_with_age_nin_names = [user.name for user in users_with_age_nin]
print(users_with_age_nin_names)

users_with_name_Sara = session.query(User).filter_by(name="Sara Ahmed").all()
print(len(users_with_name_Sara))
extracted_ids = [user.id for user in users_with_name_Sara]
print(extracted_ids)

#.where
users_greater_than_thirty = session.query(User).where(User.age>30)
for user in users_greater_than_thirty:
    print(f"User Id: {user.id}, name: {user.name}, age: {user.age}")

#or_
# Using or_ where either one from many conditions needs to be true

from sqlalchemy import or_

selected_users = session.query(User).filter(or_(User.age>=30,User.name.like("R%"))).all()
print(len(selected_users))
selected_users_names = [user.name for user in selected_users]
print(selected_users_names)

#Similar working using where
selected_users = session.query(User).where((User.age>=30)|(User.name.like("R%"))).all()
print(len(selected_users))
selected_users_names = [user.name for user in selected_users]
print(selected_users_names)


# using and_

from sqlalchemy import and_
selected_users = session.query(User).filter(and_(User.age>=30,User.name.like("R%"))).all()
print(len(selected_users))
selected_users_names = [user.name for user in selected_users]
print(selected_users_names)

selected_users = session.query(User).where(and_(User.age>=30,User.name.like("R%"))).all()
print(len(selected_users))
selected_users_names = [user.name for user in selected_users]
print(selected_users_names)

selected_users = session.query(User).filter((User.age>=30) &(User.name.like("R%"))).all()
print(len(selected_users))
selected_users_names = [user.name for user in selected_users]
print(selected_users_names)

# Using not_ 
from sqlalchemy import not_
selected_users = session.query(User).where(not_(User.name.like("R%"))).all()
print(len(selected_users))
selected_users_names = [user.name for user in selected_users]
print(selected_users_names)

# Combining all
combined_result = (
    session.query(User).where(
        or_(
            not_(User.name.like("R%")),
            and_(
                User.age > 20,
                User.age < 30
            )
        )
    )
).all()
for user in combined_result:
    print(f"User Id: {user.id}, name: {user.name}, age: {user.age}")
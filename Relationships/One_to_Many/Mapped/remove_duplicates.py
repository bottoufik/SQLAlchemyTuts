# When app.py is run more than once it adds duplicate entries in the database.

from sqlalchemy import func
from models import session, User, Address

duplicate_users = (
    session.query(
        User.name,
        User.age,
        func.count(User.id)
    )
    .group_by(User.name, User.age)
    .having(func.count(User.id) > 1)
    .all()
)

for name, age, _ in duplicate_users:
    users = (
        session.query(User)
        .filter(
            User.name == name,
            User.age == age
        )
        .order_by(User.id)
        .all()
    )


    # Keep the first one
    for user in users[1:]:
        session.delete(user)

session.commit()

print("Duplicate users removed.")

duplicate_addresses = (
    session.query(
        Address.city,
        Address.state,
        Address.zip_code,
        func.count(Address.id)
    )
    .group_by(
        Address.city,
        Address.state,
        Address.zip_code
    )
    .having(func.count(Address.id)>1)
    .all()
)

for city, state, zip_code, _ in duplicate_addresses:
    addresses = (
        session.query(Address)
        .filter(
            Address.city == city,
            Address.state == state,
            Address.zip_code == zip_code
        )
        .order_by(Address.id)
        .all()
    )

    for address in addresses[1:]:
        session.delete(address)

session.commit()

print("Duplicate addresses removed.")
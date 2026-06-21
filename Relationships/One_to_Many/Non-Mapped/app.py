from models import Address, session, User

# Creating User
names = [ "John Doe", "Jane Smith", "Michael Johnson", "Emily Davis", "David Wilson", "Sarah Brown", "Daniel Taylor", "Olivia Martinez", "James Anderson", "Sophia Thomas" ]
ages = [22, 31, 27, 24, 45, 29, 38, 26, 33, 21]

users = [
    User(name=name, age=age)
    for name, age in zip(names, ages)
]

# streets = ["123 Main St","456 Oak Ave","789 Pine Rd","321 Maple Dr","654 Cedar Ln","987 Elm St","147 Birch Blvd","258 Walnut Ct","369 Cherry Ave","741 Spruce Way"]
cities = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Phoenix",
    "Philadelphia",
    "San Antonio",
    "San Diego",
    "Dallas",
    "San Jose"
]

states = ["NY","CA","IL","TX","AZ","PA","TX","CA","TX","CA"]
zip_codes = ["10001","90001","60601","77001","85001","19101","78201","92101","75201","95101"]

addresses = [
    Address(
        city = city,
        state = state,
        zip_code = zip_code
    )
    for city, state, zip_code in zip(
        cities,
        states,
        zip_codes
    )
]

import random

random.shuffle(addresses)

for user, address in zip(users, addresses):
    user.addresses.append(address)


for user in users:
    session.add(user)

session.commit()

print(f"{users[0].addresses = }")

# Created 10 users with 10 address
# Now creating 11th user with and two addresses to map it to two address

user11 = User(name="Linus Torvald",age=49)

address11 = Address(city="Denver", state="CO", zip_code=80203)
address12 = Address(city="Seattle",state="WA", zip_code=98116)

user11.addresses.extend([address11,address12])

session.add(user11)
session.commit()

print(f"{user11.addresses = }")
print(f"{address11.user = }")
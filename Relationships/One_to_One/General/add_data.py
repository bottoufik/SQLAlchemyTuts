from models import User, Address, session

new_user = User(name="John Doe", age=25)
new_address = Address(street = "123 Maple Street", city="Toronto", state="ON", zip_code="112341", user=new_user)
session.add(new_user)
session.add(new_address)
session.commit()

print(new_user.name)
print(new_user.age)
print(new_user.address.street)
print(new_user.address.city)
print(new_user.address.state)
print(new_user.address.zip_code)
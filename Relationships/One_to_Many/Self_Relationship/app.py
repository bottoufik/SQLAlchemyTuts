from models import session, User

# creating users
user1 = User(username="User 1")
user2 = User(username="User 2")
user3 = User(username="User 3")

user1.following.append(user2)
user2.following.append(user3)

#Adding users to the session
session.add_all([user1,user2,user3])
session.commit()

print(f"{user1.following = }")
print(f"{user2.following = }")
print(f"{user3.following = }")
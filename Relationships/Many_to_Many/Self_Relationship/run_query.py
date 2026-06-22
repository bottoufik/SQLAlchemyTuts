from models import session, User

user_1 = session.query(User).first()

print(f"{user_1} is following: {user_1.following}")
print(f"{user_1} is being followed by: {user_1.followers}")
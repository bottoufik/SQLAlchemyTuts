from models import session, User

if session.query(User).count() < 1:
    user_1 = User(name="John")
    user_2 = User(name="Rob")
    user_3 = User(name="Kyle")

    user_1.following.append(user_2)
    user_2.following.append(user_1)
    user_3.following.append(user_1)

    session.add_all([user_1, user_2, user_3])
    session.commit()
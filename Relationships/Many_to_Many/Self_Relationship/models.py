from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///selfrelationshipinmanytomany.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class UserAssociation(Base):
    __tablename__ = "user_associations"
    id = Column(Integer, primary_key=True)

    follower_id = Column(Integer, ForeignKey("users.id"))
    following_id = Column(Integer, ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    following = relationship(
        "User",
        secondary="user_associations",
        primaryjoin="UserAssociation.follower_id==User.id",
        secondaryjoin="UserAssociation.following_id==User.id",
        backref="followers"
    )

    def __repr__(self):
        return f"<User: {self.name}>"


Base.metadata.create_all(engine)
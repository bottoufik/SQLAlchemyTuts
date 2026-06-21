from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

db_url = "sqlite:///onedatabase.db"
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    address = relationship("Address", back_populates="user", uselist=False)

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(Integer, unique=True)
    user_id =  Column(ForeignKey("users.id"))
    user = relationship("User",back_populates="address")

Base.metadata.create_all(engine)
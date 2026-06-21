from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship, sessionmaker

db_url = "sqlite:///mappeddatabase.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Mapped method

class BaseModel(Base):
    __abstract__ = True        #Making it an abstract class so that others can inherit
    __allow_unmapped__ = True  # Allow unmapped

    id = Column(Integer, primary_key=True)



class Address(BaseModel):
    __tablename__ = "addresses"

    city = Column(String)
    state = Column(String)
    zip_code = Column(Integer)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self):
        return f"<Address(id={self.id}, city='{self.city}')>"


class User(BaseModel):
    __tablename__ = "users"
    # __table_args__ = (
    #     UniqueConstraint("name", "age")
    # )

    name = Column(String)
    age = Column(Integer)
    addresses: Mapped[list["Address"]] = relationship() # User can have a list of addresses

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.name}')>"


Base.metadata.create_all(engine)
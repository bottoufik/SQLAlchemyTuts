from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///selfdatabase.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True)

    username = Column(String)
    
    following_id = Column(Integer, ForeignKey("users.id"))
    following = relationship("User", remote_side=[id], uselist=True)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}, following={self.folllowing}')>"


Base.metadata.create_all(engine)
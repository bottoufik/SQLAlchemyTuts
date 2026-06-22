from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///nodedatabase.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable= True)

    node_id = Column(Integer, ForeignKey("nodes.id"))
    next_node = relationship("Node", remote_side=[id], uselist=False)

    def __repr__(self):
        return f"<Node value={self.value}, next nodes={self.next_node}>"


Base.metadata.create_all(engine)
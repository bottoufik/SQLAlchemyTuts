from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///nodedatabase.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class NodeAssociation(Base):
    __tablename__ = "node_associations"
    id = Column(Integer, primary_key=True)

    current_node_id = Column(Integer, ForeignKey("nodes.id"))
    next_node_id = Column(Integer, ForeignKey("nodes.id"))


class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable= True)

    node_id = Column(Integer, ForeignKey("nodes.id"))
    next_node = relationship("Node",
                            secondary= "node_associations",
                            primaryjoin= ("NodeAssociation.current_node_id == Node.id"),
                            secondaryjoin=("NodeAssociation.next_node_id == Node.id"),
                            uselist=False)

    def __repr__(self):
        return f"<Node value={self.value}>"


Base.metadata.create_all(engine)
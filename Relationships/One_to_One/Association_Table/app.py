from models import session, Node

node1 = Node(value=10)
node2 = Node(value=20)
node3 = Node(value=30)

node1.next_node = node2
node2.next_node = node3
node3.next_node = node1

session.add_all([node1, node2, node3])
session.commit()


print(node1)
print(node2)
print(node3)
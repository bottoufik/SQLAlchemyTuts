from models import session, Student, Course

Math = Course(title="Mathematics")
Physics = Course(title="Physics")
Bill = Student(name="Bill", courses=[Math,Physics])
Rob = Student(name="Rob", courses=[Math])

session.add_all([Math, Physics, Bill, Rob])
session.commit()
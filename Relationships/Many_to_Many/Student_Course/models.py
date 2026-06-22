from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

db_url = "sqlite:///studcourse.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# student_course_link = Table(
#     'student_course',
#     Base.metadata,
#     Column('student_id', Integer, ForeignKey('students.id')),
#     Column('course_id', Integer, ForeignKey('courses.id')),
# )

class StudentCourse(Base):
    __tablename__ = "student_course"
    id = Column(Integer, primary_key=True)
    student_id = Column("student_id",Integer, ForeignKey("students.id"))
    course_id = Column("course_id",Integer, ForeignKey("courses.id"))

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course",secondary="student_course", back_populates="students")

class Course(Base):
    __tablename__= "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    students =  relationship("Student",secondary="student_course", back_populates="courses")

Base.metadata.create_all(engine)
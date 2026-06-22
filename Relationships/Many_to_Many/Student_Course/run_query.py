from models import session, Student

rob = session.query(Student).filter_by(name='Rob').first()
courses = [course.title for course in rob.courses]
print(f"Rob's Courses: {', '.join(courses)}")

bill = session.query(Student).filter_by(name='Bill').first()
courses = [course.title for course in bill.courses]
print(f"Bill's Courses: {', '.join(courses)}")
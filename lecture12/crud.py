from main import app, db, Student

# Now, run the database operations within the Flask application context
with app.app_context():
    new_student = Student('John', 90)
    db.session.add(new_student)
    db.session.commit()

    # List all students
    all_students = Student.query.all()
    print(all_students)

    # Select the student by id
    first_student = Student.query.get(1)
    print(first_student.name)

    # filters
    student_pass = Student.query.filter(Student.grade>=85)
    print(student_pass.all())

    # Update
    first_student = Student.query.get(1)
    first_student.grade = 105
    db.session.add(first_student)
    db.session.commit()

    # delete
    second_student = Student.query.get(2)
    db.session.delete(second_student)
    db.session.commit()

    # List all students
    all_students = Student.query.all()
    print(all_students)
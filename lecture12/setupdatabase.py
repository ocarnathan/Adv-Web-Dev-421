from main import app, db, Student

# Now, run the database operations within the Flask application context
with app.app_context():
    # Create the tables (if not already created)
    db.create_all()

    Obie = Student('Obie', 100)
    Carlos = Student('Carlos', 105)

    # Initially, they will print None because they are not inserted into the table,
    # and the auto-incrementing primary key (id) will be set by the database upon commit.
    print(Obie.id)
    print(Carlos.id)

    # Add the instances to the session
    db.session.add_all([Obie, Carlos])

    # Commit the changes to the database, which will insert the records and set the auto-incrementing primary key (id).
    db.session.commit()

    # After committing, they should now have their respective auto-generated ids.
    print(Obie.id)
    print(Carlos.id)

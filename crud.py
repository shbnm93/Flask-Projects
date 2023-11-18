from base import db, Puppy, app

with app.app_context():
    # Create
    puppy_name = 'Rufus'
    existing_puppy = db.session.query(Puppy).filter_by(name=puppy_name).first()

    if not existing_puppy:
        my_puppy = Puppy(puppy_name, 5)
        db.session.add(my_puppy)
        db.session.commit()

    # Read
    all_puppies = Puppy.query.all()
    print(all_puppies)

    # Select by id
    puppy_one = db.session.query(Puppy).get(1)
    print(puppy_one.name)

    # Filters
    puppy_frankie = Puppy.query.filter_by(name='Frankie')
    print(puppy_frankie.all())

    # Update
    first_puppy = db.session.query(Puppy).get(1)
    first_puppy.age = 10
    db.session.add(first_puppy)
    db.session.commit()

    # Delete
    second_pup = db.session.query(Puppy).get(2)
    if second_pup:
        db.session.delete(second_pup)
        db.session.commit()

    # Print all puppies after modifications
    all_puppies = Puppy.query.all()
    print(all_puppies)

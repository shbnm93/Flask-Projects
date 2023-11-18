from base import db, Puppy, app

#creates all the tables model --> db table
with app.app_context():
    db.create_all()


    sam = Puppy('Sammy', 3)
    frank = Puppy('Frankie', 4)


    # None
    # None
    print(sam.id)
    print(frank.id)

    db.session.add_all([sam, frank])

    db.session.commit()


    print(sam.id)
    print(frank.id)



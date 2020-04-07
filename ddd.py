db1 = input()


def main(db):
    global_init(db)
    session = create_session()
    for jobs in session.query(User).filter(User.age < 21, User.address == "module_1"):
        jobs.address = "module_3"
    session.commit()


if __name__ == '__main__':
    main(db1)

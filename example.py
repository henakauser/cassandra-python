#!/usr/bin/env python

from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.execute('USE users')

INSERT_USERS = session.prepare("""
    INSERT INTO users (
        name,
        age,
        email)
    VALUES (?,?,?)
    """)

SELECT_USERS = session.prepare("""
    SELECT
        name,
        age,
        email
    FROM users
    """)

SELECT_USER_BY_NAME = session.prepare("""
    SELECT
        name,
        age,
        email
    FROM users
    WHERE name = ?
    """)


def create_user(name, age, email):
    """Insert a user into the users table"""
    session.execute(INSERT_USERS, [name, age, email])


def get_users():
    """Select all users from the users table"""
    return session.execute(SELECT_USERS)


def get_user_by_name(name):
    """Select one user by name"""
    return session.execute(SELECT_USER_BY_NAME, [name])[0]


if __name__ == '__main__':
    session.execute("""CREATE KEYSPACE IF NOT EXISTS users
                WITH REPLICATION = {'class': 'SimpleStrategy',
                                    'replication_factor': 1}""")

    session.execute("""CREATE TABLE IF NOT EXISTS users (name text PRIMARY KEY,
                                                    age int,
                                                    email text)""")

    create_user('Bejan', 22, 'bj@gmail.com')
    create_user("Giddu", 40, 'Lud@gmail.com')
    create_user("Naila", 7, 'naila@gmail.com')
    create_user("Hena", 37, 'hena@gmail.com')

    users = get_users()
    for user in users:
        print user.name, user.age, user.email

    aliya = get_user_by_name('Aliya')
    print aliya.name, aliya.age, aliya.email

    names_to_query = ['Aliya', 'Naila']
    users = []
    for name in names_to_query:
        user = get_user_by_name(name)
        users.append(user)
    print users
#!/usr/bin/env python

from cassandra.cluster import Cluster
cluster = Cluster(['127.0.0.1'])

session = cluster.connect()

def create_user(name, age, email):
    """Creates new users in the users table"""
    cql = session.prepare(
        """
        INSERT INTO users (
            name,
            age,
            email
        )
        VALUES (?, ?, ?)
        """)
    session.execute(cql, [name, age, email])


if __name__ == '__main__':
    try:
        session.execute("""CREATE KEYSPACE users
                    WITH REPLICATION = {'class': 'SimpleStrategy',
                                        'replication_factor': 1}""")
    except:
        print "keyspace already exists"

    session.execute("""CREATE KEYSPACE IF NOT EXISTS users
                WITH REPLICATION = {'class': 'SimpleStrategy',
                                    'replication_factor': 1}""")

    session.execute('USE users')

    session.set_keyspace('users')

    session.execute("""CREATE TABLE IF NOT EXISTS users (name text PRIMARY KEY,
                                                    age int,
                                                    email text)""")

#    session.execute("""INSERT INTO users (name, age, email) VALUES ('Aliya', 2, 'aliya@gmail.com')""")

    create_user('Bejan', 22, 'bj@gmail.com')

    rows = session.execute('SELECT name, age, email FROM users')
    print rows
    for user_row in rows:
        print user_row.name, user_row.age, user_row.email

#    for row in rows:
#       print row[0], row[1], row[2]

    session.execute(
        """
        INSERT INTO users (
            name,
            age,
            email
        )
        VALUES (%s, %s, %s)
        """, ("Naila", 7, 'naila@gmail.com'))

    session.execute(
        """
        INSERT INTO users (
            name,
            age,
            email
        )
        VALUES (%s, %s, %s)
        """, ("Hena", 37, 'hena@gmail.com'))

#    session.execute("""INSERT INTO users (name, age, email)
#                   VALUES (%(name)s, %(age)s, %(email)s)""",
#                   {'name': "Amiya", 'age':  46, 'email': 'amiya@gmail.com'})

#   for (name, age, email) in rows:
#       print name, age, email

    user_lookup_statement = session.prepare("SELECT * FROM users WHERE name = ?")
    name_to_query = 'Aliya'
    user = session.execute(user_lookup_statement, [name_to_query])
    print user

    name_to_queryX = ['Aliya', 'Naila']
    users = []
    for name in name_to_queryX:
        print name
        user = session.execute(user_lookup_statement, ['Aliya'])
        users.append(user)
        print users
'''
UserRepository repository class
'''

from lib.user import User

class UserRepository:
    def __init__(self, db_connection):
        self._db_connection = db_connection

    def add(self, user):
        self._db_connection.execute("INSERT INTO users (username, email_address) VALUES (%s, %s)", [user.username, user.email_address])
        return None
            
    def get(self):
        rows = self._db_connection.execute("SELECT * FROM users;")
        users = []
        for row in rows:
            user = User(row['id'], row['username'], row['email_address'], row['signup_date'])
            users.append(user)
        return users

    def find(self, user_id):
        rows = self._db_connection.execute("SELECT * FROM users;")
        users = []
        for row in rows:
            user = User(row['id'], row['username'], row['email_address'], row['signup_date'])
            users.append(user)
        return users
    
    def delete(self, user_id):
        self._db_connection.execute("DELETE FROM users WHERE id = %s", [user_id])
        return None
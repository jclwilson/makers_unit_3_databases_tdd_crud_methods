'''
UserRepository class implementing CRUD methods on Post class.
'''

from lib import post_repository
from lib.user import User
from lib.post_repository import PostRepository

class UserRepository:
    def __init__(self, db_connection):
        self._db_connection = db_connection

    def add(self, user):
        self._db_connection.execute("INSERT INTO users (username, email_address) VALUES (%s, %s)", [user.username, user.email_address])
        return None
            
    def get(self):
        rows = self._db_connection.execute("SELECT * FROM users;")
        if len(rows) > 0:
            users = []
            for row in rows:
                user = User(row['id'], row['username'], row['email_address'], row['signup_date'])
                users.append(user)
            return users
        else:
            return None

    def find(self, user_id):
        rows = self._db_connection.execute("SELECT * FROM users;")
        if len(rows) > 0:
            row = rows[0]
            user = User(row['id'], row['username'], row['email_address'], row['signup_date'])
            return user
        else:
            return None

    def delete(self, user_id):
        self._db_connection.execute("DELETE FROM users WHERE id = %s", [user_id])
        return None

    def get_user_post_info(self, user_id):
        post_repository = PostRepository(self._db_connection)
        user = self.find(user_id)
        user.posts = post_repository.by_user(user_id)
        return user

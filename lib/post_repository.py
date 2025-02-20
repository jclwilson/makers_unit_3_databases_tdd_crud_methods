'''
PostRepository class implementing CRUD methods on Post class.
'''

from lib.post import Post

class PostRepository:
    '''
    Controls the CRUD operations for the posts table.
    '''
    def __init__(self, db_connection):
        '''
        '''
        self._db_connection = db_connection

    def add(self, post):
        '''
        Method to create a new post and add it to the database.

        from lib.post import Post
        Parameters: title, contents, user_id
        Side effects: creates a new post and adds it to the database.
        Returns: None
        '''
        self._db_connection.execute("INSERT INTO posts (title, content, views, user_id) VALUES (%s, %s, 0, %s)", [post.title, post.content, post.user_id])
        return None

    def get(self):
        '''
        Method to get all posts from the database
        Parameters: None
        Side effects: None
        Returns: A list of post instances.
        '''
        rows = self._db_connection.execute("SELECT * FROM posts;")
        if len(rows) > 0:
            posts = [] 
            for row in rows:
                post = Post(row['id'], row['title'], row['content'], row['publish_date'], row['views'], row['user_id'])
                posts.append(post)
            return posts
        else:
            return None

    def find(self, id):
        '''
        Method to get the details of an individual post from the database.
        Parameters: id
        Side effects: None
        Returns: Instance object
        '''
        rows = self._db_connection.execute("SELECT * FROM posts;")
        if len(rows) > 0:
            row = rows[0]
            return Post(row['id'], row['title'], row['content'], row['publish_date'], row['views'], row['user_id'])
        else:
            return None

    def by_user(self, user_id):
        '''
        Method to get all posts by a user from the database.
        Parameters: user_id
        Side effects: None
        Returns: List of instance objects
        '''
        rows = self._db_connection.execute("SELECT * FROM posts WHERE user_id = %s;", [user_id])
        if len(rows) > 0:
            posts = [] 
            for row in rows:
                post = Post(row['id'], row['title'], row['content'], row['publish_date'], row['views'], row['user_id'])
                posts.append(post)
            return posts
        else:
            return None

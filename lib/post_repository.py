'''
PostRepository class implementing CRUD methods on Post class.
'''

class PostRepository:
    '''
    Controls the CRUD operations for the posts table.
    '''
    def __init__(self):
        '''
        '''
        pass

    def add(self, title, contents, user_id):
        '''
        Method to create a new post and add it to the database.
        Parameters: title, contents, user_id
        Side effects: creates a new post and adds it to the database.
        Returns: None
        '''
        pass

    def get(self):
        '''
        Method to get all posts from the database
        Parameters: None
        Side effects: None
        Returns: A list of post instances.
        '''
        pass

    def find(self, id):
        '''
        Method to get the details of an individual post from the database.
        Parameters: id
        Side effects: None
        Returns: Instance object
        '''
        pass

    def by_user(self, user_id):
        '''
        Method to get all posts by a user from the database.
        Parameters: user_id
        Side effects: None
        Returns: List of instance objects
        '''
        pass

class Post:
    '''
    Class that models a signle post.
    '''
    def __init__(self, id, title, contents, publish_date, views, user_id):
        '''
        Parameters: id, title, contents, publish_date, views
        Side effects: None
        Returns: None
        '''
        self.id = id
        self.title = title
        self.contents = contents
        self.publish_date = publish_date
        self.views = views
        self.user_id = user_id

    def __eq__(self, other):
        '''
        Parameters: other
        Side effects: rewrites eq method
        Returns: statement asserting object instances with same attributes are equal.
        '''
        return self.__dict__ == other.__dict__

    def __repr__(self):
        '''
        Parameters: None
        Side effects: rewrites repr method.
        Returns: Pretty printed representation of the instance object.
        '''
        return f"Post({self.id}, {self.title}, {self.contents}, {self.publish_date}, {self.views}, {self.user_id})"

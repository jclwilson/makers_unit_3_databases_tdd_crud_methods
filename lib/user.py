'''
User model class representing a single user.
'''

class User:
    '''
    Parameters: id, username, email address, and signup date
    Side Effects: None
    Returns: None
    '''
    def __init__(self, id, username, email_address, signup_date):
        self.id = id
        self.username = username
        self.email_address = email_address
        self.signup_date = signup_date

    def __eq__(self, other):
        '''
        Parameters: Other
        Side effects: reqrites eq method
        Returns: statement asserting self == other.
        '''
        return self.__dict__ == other.__dict__

    def __repr__(self):
        '''
        Parameters: None
        Side effects: rewrites repr method.
        Returns: Pretty printed representation of the instance object.
        '''
        return f"User({self.id}, {self.username}, {self.email_address}, {self.signup_date})"

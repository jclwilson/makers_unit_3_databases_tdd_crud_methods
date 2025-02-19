'''
Test file for User class.
'''

from lib.user import User

def test_user_inits_correctly():
    '''
    When I create a user object
    it initialises correctly.
    '''
    user_1 = User(None, 'Jake', 'jake@email.com', None)
    user_1.username == 'Jake'
    assert user_1.email_address == 'jake@email.com'

def test_user_instance_objects_are_equal():
    '''
    When I add two users with identical attributes
    They are considered equal
    '''
    user_1 = User(None, 'Jake', 'jake@email.com', None)
    user_2 = User(None, 'Jake', 'jake@email.com', None)
    assert user_1 == user_2

def test_user_instance_objects_pretty_print():
    '''
    When the user object is converted to a string
    It pretty prints its attributes
    '''
    user_1 = User(None, 'Jake', 'jake@email.com', None)
    assert str(user_1) == 'User(None, Jake, jake@email.com, None)'

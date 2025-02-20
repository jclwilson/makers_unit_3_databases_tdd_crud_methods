'''
Tests for UserRepository repository class.
'''

import pytest 

from unittest.mock import ANY

from lib.user_repository import UserRepository
from lib.user import User

def test_add_user_to_database(db_connection):
    '''
    When I add a user
    The users details are added to the database
    '''
    db_connection.seed('seeds/social_network_tables.sql')
    user_repository = UserRepository(db_connection)
    user_1 = User(None, 'Jake', 'jake@email.com', None)
    user_repository.add(user_1)
    added_user = user_repository.get()
    assert added_user[0].id == 1
    assert added_user[0].username == 'Jake'
    assert added_user[0].email_address == 'jake@email.com'
    assert added_user[0].signup_date is not None

def test_add_multiple_users_to_database(db_connection):
    '''
    When I add mulitple users
    The details of all users are added to the database
    '''
    db_connection.seed('seeds/social_network_tables.sql')
    user_repository = UserRepository(db_connection)
    user_1 = User(None, 'Jake', 'jake@email.com', None)
    user_2 = User(None, 'Alec', 'alec@email.com', None)
    user_repository.add(user_1)
    user_repository.add(user_2)
    user_repository.get() == [user_1, user_2]

def test_find_users_in_database(db_connection):
    '''
    When I find user in the database
    The details of the user are returned as an object
    '''
    db_connection.seed('seeds/social_network_tables.sql')
    user_repository = UserRepository(db_connection)
    user_1 = User(None, 'Jake', 'jake@email.com', None)
    user_2 = User(None, 'Alec', 'alec@email.com', None)
    user_repository.add(user_1)
    user_repository.add(user_2)
    added_user = user_repository.find(1)
    assert added_user[0].id == 1
    assert added_user[0].username == 'Jake'
    assert added_user[0].email_address == 'jake@email.com'
    assert added_user[0].signup_date is not None

def test_delete_users_in_database(db_connection):
    db_connection.seed('seeds/social_network_tables.sql')
    user_repository = UserRepository(db_connection)
    user_1 = User(None, 'Delete Me', 'tobedeleted@email.com', None)
    user_repository.add(user_1)
    found_user = user_repository.find(1)
    assert found_user[0].id == 1
    assert found_user[0].username == 'Delete Me'
    assert found_user[0].email_address == 'tobedeleted@email.com'
    user_repository.delete(1)
    assert user_repository.find(1) == []
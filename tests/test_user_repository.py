'''
Tests for UserRepository repository class.
'''

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
    
    added_user_1 = user_repository.get()[0]
    added_user_2 = user_repository.get()[1]
    assert added_user_1.id == 1
    assert added_user_1.username == 'Jake'
    assert added_user_1.email_address == 'jake@email.com'
    
    assert added_user_2.id == 2
    assert added_user_2.username == 'Alec'
    assert added_user_2.email_address == 'alec@email.com'

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
    assert added_user.id == 1
    assert added_user.username == 'Jake'
    assert added_user.email_address == 'jake@email.com'
    assert added_user.signup_date is not None

def test_delete_users_in_database(db_connection):
    db_connection.seed('seeds/social_network_tables.sql')
    user_repository = UserRepository(db_connection)
    user_1 = User(None, 'Delete Me', 'tobedeleted@email.com', None)
    user_repository.add(user_1)
    found_user = user_repository.find(1)
    assert found_user.id == 1
    assert found_user.username == 'Delete Me'
    assert found_user.email_address == 'tobedeleted@email.com'
    user_repository.delete(1)
    assert user_repository.find(1) == None 

def test_get_user_post_info_combined_object(db_connection):
    db_connection.seed('seeds/social_network_tables.sql')
    db_connection.seed('seeds/social_network_users.sql')
    db_connection.seed('seeds/social_network_data.sql')
    user_repository = UserRepository(db_connection)
    user_post_object = user_repository.get_user_post_info(1)
    print(user_post_object)
    print(user_post_object.posts)
    assert user_post_object.id == 1
    assert user_post_object.username == 'Jake'
    assert user_post_object.email_address == 'jake@email.com'
    assert user_post_object.posts[0].title == 'An example title'
    assert user_post_object.posts[1].title == 'Art news'

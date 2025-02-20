'''
Test file for PostRepository class.
'''

from lib.post_repository import PostRepository
from lib.post import Post

def test_add_post_to_database(db_connection):
    '''
    When I create a post
    The post details are added to the database.
    '''
    db_connection.seed('seeds/social_network_tables.sql')
    db_connection.seed('seeds/social_network_users.sql')
    post_repository = PostRepository(db_connection)
    post_1 = Post(None, 'A test title', 'Test content', None, 0, 1)
    post_repository.add(post_1)
    added_post = post_repository.get()
    assert added_post[0].id == 1
    assert added_post[0].title == 'A test title'
    assert added_post[0].content == 'Test content'
    assert added_post[0].views == 0
    assert added_post[0].user_id == 1

def test_add_multiple_posts_to_database(db_connection):
    '''
    When I create multiple posts
    The details of all posts are added to the database.
    '''
    db_connection.seed('seeds/social_network_tables.sql')
    db_connection.seed('seeds/social_network_users.sql')
    post_repository = PostRepository(db_connection)
    post_1 = Post(None, 'A test title', 'Test content', None, 0, 1)
    post_2 = Post(None, 'Another test title', 'Test content', None, 0, 1)
    post_repository.add(post_1)
    post_repository.add(post_2)
    added_post_1 = post_repository.get()[0]
    added_post_2 = post_repository.get()[1]
    assert added_post_1.id == 1
    assert added_post_1.title == 'A test title'
    assert added_post_1.content == 'Test content'
    assert added_post_1.views == 0
    assert added_post_1.user_id == 1
    
    assert added_post_2.id == 2
    assert added_post_2.title == 'Another test title'
    assert added_post_2.content == 'Test content'
    assert added_post_2.views == 0
    assert added_post_2.user_id == 1

def test_find_post_in_database(db_connection):
    '''
    When I find a post in the database
Return the post information as an object.
    '''
    db_connection.seed('seeds/social_network_tables.sql')
    db_connection.seed('seeds/social_network_users.sql')
    post_repository = PostRepository(db_connection)
    post_1 = Post(None, 'A test title', 'Test content', None, 0, 1)
    post_2 = Post(None, 'Another test title', 'Test content', None, 0, 1)
    post_repository.add(post_1)
    post_repository.add(post_2)
    found_post = post_repository.find(1)
    assert found_post.id == 1
    assert found_post.title == 'A test title'
    assert found_post.content == 'Test content'
    assert found_post.views == 0
    assert found_post.user_id == 1

def test_view_all_posts_by_user(db_connection):
    '''
    When a user has multiple posts
    I can view all posts by that user.
    '''
    db_connection.seed('seeds/social_network_tables.sql')
    db_connection.seed('seeds/social_network_users.sql')
    post_repository = PostRepository(db_connection)
    post_1 = Post(None, 'A test title', 'Test content', None, 0, 1)
    post_2 = Post(None, 'Another test title', 'Test content', None, 0, 1)
    post_3 = Post(None, 'A post by user 2', 'Test content', None, 0, 2)
    post_repository.add(post_1)
    post_repository.add(post_2)
    found_posts = post_repository.by_user(1)
    assert found_posts[0].id == 1
    assert found_posts[0].title == 'A test title'
    assert found_posts[1].id == 2
    assert found_posts[1].title == 'Another test title'

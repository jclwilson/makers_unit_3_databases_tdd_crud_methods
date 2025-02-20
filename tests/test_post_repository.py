'''
Test file for PostRepository class.
'''

def test_post_is_added_to_database(db_connection):
    '''
    When I create a post
    The post details are added to the database.
    '''
    post_repository = PostRepository()
    post_1 = Post(None, 'A test title', 'Test content', None, 0, 1)
    post_repository.add(post_1)
    assert post.repository.get() == post_1

def test_add_multiple_posts_to_database(db_connection):
    '''
    When I create multiple posts
    The details of all posts are added to the database.
    '''
    post_repository = PostRepository()
    post_1 = Post(None, 'A test title', 'Test content', None, 0, 1)
    post_2 = Post(None, 'Another test title', 'Test content', None, 0, 1)
    post_repository.add(post_1)
    post_repository.add(post_2)
    assert post.repository.get() == [post_1, post_2]

def test_view_all_posts_by_user(db_connection):
    '''
    When a user has multiple posts
    I can view all posts by that user.
    '''
    post_repository = PostRepository()
    post_1 = Post(None, 'A test title', 'Test content', None, 0, 1)
    post_2 = Post(None, 'Another test title', 'Test content', None, 0, 1)
    post_3 = Post(None, 'A post by user 2', 'Test content', None, 0, 2)
    post_repository.add(post_1)
    post_repository.add(post_2)
    assert post.repository.by_user(1) == [post_1, post_2]

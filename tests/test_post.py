'''
Test file for Post class in file: lib/post.py
'''

from lib.post import Post

def test_post_inits_correctly():
    '''
    When I create a post
    It initialises correctly
    '''
    post_1 = Post(None, 'A test title', 'Test content', None, 0, 1)
    assert post_1.title == 'A test title'
    assert post_1.contents == 'Test content'
    assert post_1.views == 0
    assert post_1.user_id == 1

def test_two_post_objects_are_identical():
    '''
    When I add two posts with identical attributes
    They are considered equal
    '''
    post_1 = Post(None, 'A test title', 'Test content', None, 0, 1)
    post_2 = Post(None, 'A test title', 'Test content', None, 0, 1)
    assert post_1 == post_2

def test_post_string_pretty_prints():
    '''
    When the post object is converted to a string
    It pretty prints its attributes
    '''
    post_1 = Post(None, 'A test title', 'Test content', None, 0, 1)
    assert str(post_1) == 'Post(None, A test title, Test content, None, 0, 1)'

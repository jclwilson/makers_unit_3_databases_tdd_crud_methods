'''
Test file for Post class in file: lib/post.py
'''

'''
When I create a post
It initialises correctly
'''
post_1 = Post(None, 'A test title', 'Test content', None, 0, 1)
post_1.title == 'A test title'
post_1.content == 'Test content'
post_1.user_id == 1

'''
When I add two posts with identical attributes
They are considered equal
'''
post_1 = Post(None, 'A test title', 'Test content', None, 0, 1)
post_2 = Post(None, 'A test title', 'Test content', None, 0, 1)
post_1 == post_2

'''
When the post object is converted to a string
It pretty prints its attributes
'''
post_1 = Post(None, 'A test title', 'Test content', None, 0, 1)
str(post_1) == Post(A test title, Test content, 1)

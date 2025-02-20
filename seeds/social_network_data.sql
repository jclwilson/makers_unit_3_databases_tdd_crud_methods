-- Seed users table with example data

INSERT INTO users (username, email_address) VALUES ('jake', 'jake@email.com');
INSERT INTO users (username, email_address) VALUES ('imogen', 'imogen@email.com');
INSERT INTO users (username, email_address) VALUES ('jack', 'jack@email.com');
INSERT INTO users (username, email_address) VALUES ('alec', 'alec@email.com');

-- Seed users table with example data

INSERT INTO posts (title, content, user_id) VALUES ('An example title', 'Hello, today I went to the shops.', 1);
INSERT INTO posts (title, content, user_id) VALUES ('Swimming pool times', 'Hello, today I went to the swimming pool.', 3);
INSERT INTO posts (title, content, user_id) VALUES ('Tech news', 'A long blog post about a particualr computing problem.', 2);
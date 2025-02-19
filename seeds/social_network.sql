DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

-- Create table without foreign key first
CREATE TABLE users (
    id INT GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id),
    username TEXT NOT NULL,
    email_address TEXT NOT NULL,
    signup_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create table with foreign key after
CREATE TABLE posts (
    id INT GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id),
    title TEXT,
    content TEXT,
    publish_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    views INT,
    user_id INT,
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
            REFERENCES users(id)
                on delete cascade
);

-- Seed users table with example data

INSERT INTO users (username, email_address) VALUES ('jake', 'jake@email.com');
INSERT INTO users (username, email_address) VALUES ('imogen', 'imogen@email.com');
INSERT INTO users (username, email_address) VALUES ('jack', 'jack@email.com');
INSERT INTO users (username, email_address) VALUES ('alec', 'alec@email.com');

-- Seed users table with example data

INSERT INTO posts (title, content, user_id) VALUES ('An example title', 'Hello, today I went to the shops.', 1);
INSERT INTO posts (title, content, user_id) VALUES ('Swimming pool times', 'Hello, today I went to the swimming pool.', 3);
INSERT INTO posts (title, content, user_id) VALUES ('Tech news', 'A long blog post about a particualr computing problem.', 2);

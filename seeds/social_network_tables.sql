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
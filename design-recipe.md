# Design Recipe

## User Story

```
> As a social network user,
> So I can have my information registered,
> I'd like to have a user account with my email address.
 
> As a social network user,
> So I can have my information registered,
> I'd like to have a user account with my username.
 
> As a social network user,
> So I can write on my timeline,
> I'd like to create posts associated with my user account.
 
> As a social network user,
> So I can write on my timeline,
> I'd like each of my posts to have a title and a content.
 
> As a social network user,
> So I can know who reads my posts,
> I'd like each of my posts to have a number of views.
```
## Nouns and Verbs

```
Nouns:
- user account
- email address
- username
- timeline
- posts
- post title
- post content
- views

Verbs:
- register
- create
- read
- view
```

## Tables names and columns

| Record        | Properties    |
|-------------------------------|
| users          | username, email address
| posts          | post title, post content, publish date, views

## Columntypes

| Table : users |
----------------
| id | IDENTITY |
| username | text |
| email_address | text |
| signup_date | date |

| Table : posts |
----------------
| id | IDENTITY |
| title | text |
| content | text |
| publish_date | date |
| views | int |

## Table relationships

1. Can one user have many posts? YES
2. Can one post have many users? NO

-> Therefore,
-> A user HAS MANY posts
-> A post BELONGS TO a user

-> Therefore, the foreign key is on the posts table.

## SQL

```sql
-- Tidy up previous examples
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

```

## Create tables

```bash
psql -h localhost -d social_network < social_network.sql
```

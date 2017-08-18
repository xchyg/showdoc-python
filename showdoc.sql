BEGIN TRANSACTION;

CREATE TABLE category (
    cat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cat_name TEXT,
    parent_id INTEGER DEFAULT 0,
    item_id INTEGER,
    order_id INTEGER,
    addtime INTEGER
);

CREATE TABLE `item` (
    `item_id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `item_type` INTEGER DEFAULT 1,
    `item_name` TEXT,
    `item_description` TEXT,
    `uid` INTEGER,
    `username` TEXT,
    `password` TEXT,
    `addtime` INTEGER DEFAULT 0
);

CREATE TABLE `page` (
    `page_id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `author_uid` INTEGER DEFAULT 0,
    `author_username` TEXT,
    `item_id` INTEGER DEFAULT 0,
    `cat_id` INTEGER DEFAULT 0,
    `page_title` TEXT,
    `page_content` TEXT,
    `page_comments` TEXT,
    `order_id` INTEGER DEFAULT 99,
    `addtime` INTEGER DEFAULT 0
);

CREATE TABLE user(
    `uid` INTEGER PRIMARY KEY AUTOINCREMENT,
    `username` TEXT UNIQUE,
    `groupid` INTEGER DEFAULT 2,
    `name` TEXT,
    `avatar` TEXT,
    `avatar_small` TEXT,
    `email` TEXT,
    `password` TEXT,
    `cookie_token` TEXT,
    `cookie_token_expire` INTEGER DEFAULT 0,
    `reg_time` INTEGER DEFAULT 0,
    `last_login_time` INTEGER DEFAULT 0
);
COMMIT;

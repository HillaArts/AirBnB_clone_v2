-- Use the mysql database for managing users and privileges
USE mysql;

-- Check if the database exists, and create it if it doesn't
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Check if the user exists, and create the user if it doesn't
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges to the user on the hbnb_dev_db database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Make sure the privileges take effect immediately
FLUSH PRIVILEGES;


-- MySQL database and user setup
-- User 'hbnb_test' with the password 'hbnb_test_pwd'
-- Granted all privileges for the database hbnb_dev_db
-- Granted SELECT privilege for the database performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON  hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

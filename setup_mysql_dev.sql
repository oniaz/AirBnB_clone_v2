-- MySQL database and user setup
-- User 'hbnb_dev' with the password'hbnb_dev_pwd'
-- Granted all privileges for the database hbnb_dev_db
-- Granted SELECT privilege for the database performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON  hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Prepares a MySQL server for the project
-- create project developement database (hbnb_dev_db)
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creating new user (hbnb_dev) with all privileges on the hbnb_dev_db
-- and password (hbnb_dev_pwd) if not exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- granting all privileges to new user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- granting the SELECT privilege for hbnb_dev in the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

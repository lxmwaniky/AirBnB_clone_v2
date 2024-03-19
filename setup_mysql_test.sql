-- Test case 1: Check if hbnb_dev_db is created
SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'hbnb_dev_db';

-- Test case 2: Check if hbnb_dev user is created
SELECT User FROM mysql.user WHERE User = 'hbnb_dev';

-- Test case 3: Check if hbnb_dev user has all privileges on hbnb_dev_db
SHOW GRANTS FOR 'hbnb_dev'@'localhost';

-- Test case 4: Check if hbnb_dev user has SELECT privilege on performance_schema
SHOW GRANTS FOR 'hbnb_dev'@'localhost' ON performance_schema.*;
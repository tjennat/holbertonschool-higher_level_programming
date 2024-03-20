-- DROP USER IF EXISTS 'user_0d_1'@'localhost';
 DROP USER IF EXISTS 'user_0d_2'@'localhost';

-- Create user_0d_1 if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
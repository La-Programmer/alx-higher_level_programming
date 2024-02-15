-- CREATE MYSQL USER user_0d_1
CREATE USER IF NOT EXISTS user_0d_1@localhost
IDENTIFIED BY 'Secure2Pass!';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
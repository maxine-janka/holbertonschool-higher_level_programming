-- Creates a user with global privledges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'; -- Global privledges, all databases and all tables

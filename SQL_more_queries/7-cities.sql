-- Creates a new database named hbtn_0d_usa, and a table named cities.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES cities(id)
);
-- A value in the FOREIGN KEY column matches a value in the REFERENCES column
-- in the same or another table and defines relationships.

-- Creates a new database named hbtn_0d_usa, and a table names states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
-- AUTO_INCREMENT automatically generates a new id, starting at 1
-- PRIMARY KEY implies NOT NULL and unique

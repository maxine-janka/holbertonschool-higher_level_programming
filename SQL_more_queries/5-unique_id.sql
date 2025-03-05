-- Creates a table named unique_id in the current database, only if it doesn't exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256)
);

-- Creates a table named id_not_null in the current database, only if it doesn't exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);

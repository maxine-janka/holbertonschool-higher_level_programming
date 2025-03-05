-- Lists all records of the table names second_table, display in descending order
SELECT score, name 
FROM second_table
WHERE name != 'name'
ORDER BY score DESC;

-- Lists all records of the table names second_table, display in descending order
SELECT score, name 
FROM second_table
GROUP BY score
ORDER BY score DESC;

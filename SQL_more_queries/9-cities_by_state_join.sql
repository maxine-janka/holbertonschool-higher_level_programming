-- Lists all cities conatined in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id -- match each row where values are the same
ORDER BY cities.id ASC;

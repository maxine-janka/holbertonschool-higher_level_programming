-- Lists all shows in the Comedy genre from the database htbn_0d_tvshows
SELECT tv_shows.title
FROM tv_show_genres
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;

-- SELECT TABLE with the show title
-- start FROM tv_show_genres to JOIN the other two tables
-- JOIN tv_show_genres with tv_shows to match the id with the show_id
-- JOIN tv_show_genres with tv_genres to match the genre id with the genres
-- match only WHERE the name is Comedy

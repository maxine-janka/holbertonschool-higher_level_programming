-- Lists of genres of the show 'Dexter' from the database hbtn_0d_tvshows
SELECT tv_genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;

-- FROM, get 'Dexter' first
-- JOIN Connect Dexter to genres by geting genre_id values for Dexter
-- JOIN Get genre names for the genre id's for Dexter
-- WHERE Filter for only Dexter

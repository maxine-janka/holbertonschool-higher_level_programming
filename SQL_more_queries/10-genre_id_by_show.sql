 -- Lists all shows in the database hbtn_0d_tvshows that have atleast one genre linked
 SELECT tv_shows.title, tv_show_genres.genre_id
 FROM tv_shows
 JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
 ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;

-- SELECT column to display
-- FROM a table, can be tv_shows or tv_show_genres
-- JOIN other table. Grab the id from the tv_shows table and find the genre with that show_id in the tv_show_genres table.
-- ORDER BY title and genre id within the title.

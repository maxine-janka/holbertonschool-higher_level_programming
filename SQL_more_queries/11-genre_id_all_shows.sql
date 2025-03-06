--  -- Lists all shows in the database hbtn_0d_tvshows that have a linked genre, if no genre display NULL
 SELECT tv_shows.title, tv_show_genres.genre_id
 FROM tv_shows
 LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
 ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;

 -- JOIN = INNER JOIN, LEFT JOIN to include all rows from tv_shows even if there is no matching genre.
 
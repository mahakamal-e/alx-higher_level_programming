-- a script that lists all shows without the genre Comedy
SELECT tv_shows.title
FROM tv_shows
WHERE id NOT IN (
	SELECT tv_show_genres.show_id
	FROM tv_show_genres
	WHERE tv_show_genres.genre_id = (SELECT id FROM tv_genres WHERE tv_genres.name = 'Comedy')
)
ORDER BY tv_shows.title ASC;

-- a script that lists all shows without the genre Comedy
SELECT title
FROM tv_shows
WHERE id NOT IN (
    -- Subquery from Step 1
    SELECT show_id
    FROM tv_show_genres
    WHERE genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy')
)
ORDER BY title ASC;

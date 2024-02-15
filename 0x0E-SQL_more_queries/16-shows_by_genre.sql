-- a script that lists all shows, and all genres linked to that show.
SELECT t.title, tgs.name
FROM
  tv_shows AS t
  LEFT JOIN tv_show_genres AS tg
  ON tg.show_id = t.id
  LEFT JOIN tv_genres AS tgs
  ON tg.genre_id = tgs.id
  ORDER BY t.title, tgs.name;

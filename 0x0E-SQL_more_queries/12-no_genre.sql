-- No Genre
-- Impert DataBase Dump
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows JOIN tv_show_genres
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;

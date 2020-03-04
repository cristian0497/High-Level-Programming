-- Onlu Comedy
-- List all Comedy showss in the database
SELECT tv_shows.title FROM tv_genres JOIN tv_genres 
ON tv_genres.id = tv_show_genres.genre_id WHERE tv_genres.id = 5
ORDER BY tv_shows.title ASC;

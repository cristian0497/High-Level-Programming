-- print with AS function
-- Number by score with AS attribute
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score DESC;

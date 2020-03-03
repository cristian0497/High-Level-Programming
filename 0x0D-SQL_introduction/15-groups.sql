-- print with AS function
-- Number by score with AS attribute
SELECT score, id AS number FROM second_table WHERE score IN (SELECT SCORE FROM second_table) ORDER BY score DESC;

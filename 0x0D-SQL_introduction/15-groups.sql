-- line1 comment
SELECT score, COUNT(*) AS number 
FROM second_table
GROUP BY score;
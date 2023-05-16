-- List all records of  table second_table having a name value in my MySQL server.
-- Records are ordered in descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC

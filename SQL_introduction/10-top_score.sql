-- Create a scriot that lists all records of the second_table of a database hbtn_0c_0
-- The results should display both the score and the name (in this order)
-- The records should be ordered by score (top first)
-- Thje database name will be passed as an argument of mysql command
SELECT score, name FROM second_table ORDER BY score DESC;
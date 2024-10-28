-- Create a script  that displays the score with score >= 10 in the second_table of the database hbtn_0c_0
--  Result should display the score and the name (in this order)
--  The database name will be passed as an argument of mysql command
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
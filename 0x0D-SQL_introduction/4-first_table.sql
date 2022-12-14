-- Write a script that creates a table called first_table in the current database in your MySQL server.
-- First_table description: id INT; name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command
-- If the table first_table already exists, your script should not fail
-- Not allowed to use the SELECT or SHOW statements

CRETE TABLE IF NOT EXISTS first_table (if INT, name VARCHAR(256));

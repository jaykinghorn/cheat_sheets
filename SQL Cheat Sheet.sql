SQL Cheat Sheet

-- Don't forget to check field types if queries don't return expected values. 
-- Use the following as the standard template
SELECT column_names
FROM table
WHERE
	(condition)
	--brackets help to identify priority of operations
	AND second condition
ORDER BY column --DESC for descending, can pass multiple values in ORDER BY

--Unique Values
SELECT DISTINCT(column)

--Wildcard
WHERE column LIKE 'string%'
	--percent indicates wildcard before or after string based on position 

-- Select a Range
WHERE column BETWEEN X AND Y

WHERE is NULL -- or is NOT NULL

-- Calculated Field
-- in the SELECT statement, perform your calculation using AS to define an alias for the new field
SELECT a, b, c, a*b AS d

--Date range selections
-- Varies significantly by DBMS - the following is for SQLITE
WHERE column BETWEEN 'date1' AND 'date2'

-- similar for MySQL
WHERE YEAR(column) = year	--date isn't treated as a string here

--Aggregate Functions
-- AVG(), COUNT(), MIN(), MAX(), SUM()
-- COUNT can use a wildcard (*) to count values with a value
SELECT AVG(column) AS column_alias
FROM table;

--Groupby Dates
GROUP BY YEAR(column_names)

-- Range of dates 
BETWEEN '01-01-2010' AND '06-30-2017'

--YYYY-MM-DD is the expected date format
EXTRACT(year FROM your_date_field) --can change month, day, etc
FORMAT_DATETIME() -- formats an existing date string format
PARSE_DATETIME() --turns 12/07/07 into a proper date format 2007-12-07

Safe Updates MSQL
SET SQL_SAFE_UPDATES=0;
UPDATE table_name
SET col = replace(col, 'old_value', 'new_value');
SET SQL_SAFE_UPDATES=1;

Formatting Results 
FORMAT("%'d", numeric_column)AS Number
-- adds commas for easier legibility, doesn't work in SQlite (check for alternate syntax)

CAST(column AS INT64) -- or float
CAST(column AS DATE) 
CAST(column AS STRING) 

ROUND(AVG(colums),2)
-- Rounds to two decimal places

Troubleshooting
-- if performing an aggregated command (Min, Max, Sum, Avg) on one column, you have to
-- Group By on other columns that don't have a aggregation function 

-- If you are using a Where clause with an alias, you have to use the original column name
-- not the alias. SQL looks to the table name, then Where clause to filter data and return
-- queries faster. This is not true for HAVING statements following a Group BY. 
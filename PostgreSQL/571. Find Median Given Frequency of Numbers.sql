Table: Numbers

+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
| frequency   | int  |
+-------------+------+
num is the primary key (column with unique values) for this table.
Each row of this table shows the frequency of a number in the database.
 

The median is the value separating the higher half from the lower half of a data sample.

Write a solution to report the median of all the numbers in the database after decompressing the Numbers table. Round the median to one decimal point.



1.
WITH RECURSIVE expand_rows AS
	(SELECT num, frequency, 1 AS repetition
	FROM Numbers
	WHERE frequency > 0
	
	UNION ALL
	
	SELECT num, frequency, repetition + 1
	FROM expand_rows
	WHERE repetition < frequency)
SELECT ROUND(median::NUMERIC, 1) 
AS median
FROM
	(SELECT PERCENTILE_CONT(0.5) 
	WITHIN GROUP (ORDER BY num ASC)
	AS median
	FROM expand_rows)
AS sub;


2.
WITH RECURSIVE expand_rows AS
	(SELECT num, frequency, 1 AS repetition
	FROM Numbers
	WHERE frequency > 0
	
	UNION ALL
	
	SELECT num, frequency, repetition + 1
	FROM expand_rows
	WHERE repetition < frequency)
SELECT ROUND(
	(PERCENTILE_CONT(0.5) 
	WITHIN GROUP 
	(ORDER BY num ASC)
	)::NUMERIC, 
	1) AS median
FROM expand_rows;
Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| company      | varchar |
| salary       | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the company and the salary of one employee.
 

Write a solution to find the rows that contain the median salary of each company. While calculating the median, when you sort the salaries of the company, break the ties by id.

Return the result table in any order.



1.
WITH ranked AS
	(SELECT *, 
	ROW_NUMBER() 
	OVER 
	(PARTITION BY company ORDER BY salary ASC) AS our_rank
	FROM Employee 
	ORDER BY company ASC, our_rank ASC),
grouped AS
	(SELECT company,
	UNNEST(CASE WHEN MAX(our_rank) % 2 = 0 THEN ARRAY[FLOOR(MAX(our_rank)::NUMERIC / 2), FLOOR(MAX(our_rank)::NUMERIC / 2) + 1]
	ELSE ARRAY[FLOOR(MAX(our_rank)::NUMERIC / 2) + 1] END) AS our_array 
	FROM ranked
	GROUP BY company)
SELECT main.id, main.company, main.salary 
FROM ranked AS main
INNER JOIN
grouped AS sub
ON main.company = sub.company AND main.our_rank = sub.our_array;
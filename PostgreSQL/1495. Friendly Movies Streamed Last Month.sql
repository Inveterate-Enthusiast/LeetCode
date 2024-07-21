Table: TVProgram

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| program_date  | date    |
| content_id    | int     |
| channel       | varchar |
+---------------+---------+
(program_date, content_id) is the primary key (combination of columns with unique values) for this table.
This table contains information of the programs on the TV.
content_id is the id of the program in some channel on the TV.
 

Table: Content

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| content_id       | varchar |
| title            | varchar |
| Kids_content     | enum    |
| content_type     | varchar |
+------------------+---------+
content_id is the primary key (column with unique values) for this table.
Kids_content is an ENUM (category) of types ('Y', 'N') where: 
'Y' means is content for kids otherwise 'N' is not content for kids.
content_type is the category of the content as movies, series, etc.
 

Write a solution to report the distinct titles of the kid-friendly movies streamed in June 2020.

Return the result table in any order.


1.
WITH merged AS
	(SELECT main.*, sub.* 
	FROM TVProgram AS main
	LEFT JOIN
	Content AS sub
	ON main.content_id = sub.content_id::NUMERIC)
SELECT DISTINCT title 
FROM merged
WHERE TO_CHAR(program_date, 'YYYY-MM') = '2020-06'
AND Kids_content = 'Y'
AND content_type = 'Movies';

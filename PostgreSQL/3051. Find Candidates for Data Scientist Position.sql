Table: Candidates

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| candidate_id | int     |
| skill        | varchar |
+--------------+---------+
(candidate_id, skill) is the primary key (columns with unique values) for this table.
Each row includes candidate_id and skill.
Write a query to find the candidates best suited for a Data Scientist position. The candidate must be proficient in Python, Tableau, and PostgreSQL.

Return the result table ordered by candidate_id in ascending order.



1.
SELECT candidate_id
FROM Candidates
GROUP BY candidate_id
HAVING ARRAY_AGG(DISTINCT skill::text) @> ARRAY['Python', 'Tableau', 'PostgreSQL']::text[]
ORDER BY candidate_id ASC;
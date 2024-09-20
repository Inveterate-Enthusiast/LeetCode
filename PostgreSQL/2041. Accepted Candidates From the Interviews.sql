Table: Candidates

+--------------+----------+
| Column Name  | Type     |
+--------------+----------+
| candidate_id | int      |
| name         | varchar  |
| years_of_exp | int      |
| interview_id | int      |
+--------------+----------+
candidate_id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of a candidate, their number of years of experience, and their interview ID.


Table: Rounds

+--------------+------+
| Column Name  | Type |
+--------------+------+
| interview_id | int  |
| round_id     | int  |
| score        | int  |
+--------------+------+
(interview_id, round_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the score of one round of an interview.


Write a solution to report the IDs of the candidates who have at least two years of experience
and the sum of the score of their interview rounds is strictly greater than 15.

Return the result table in any order.



1.
SELECT main.candidate_id
FROM Candidates AS main
LEFT JOIN
(
    SELECT interview_id, SUM(score)
    FROM Rounds
    GROUP BY interview_id
) AS sub
ON main.interview_id = sub.interview_id
WHERE main.years_of_exp >= 2 AND sub.sum > 15;
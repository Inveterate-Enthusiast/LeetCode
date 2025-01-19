--Table: Scores
--
--+-------------+---------+
--| Column Name | Type    |
--+-------------+---------+
--| student_id  | int     |
--| subject     | varchar |
--| score       | int     |
--| exam_date   | varchar |
--+-------------+---------+
--(student_id, subject, exam_date) is the primary key for this table.
--Each row contains information about a student's score in a specific subject on a particular exam date. score is between 0 and 100 (inclusive).
--Write a solution to find the students who have shown improvement. A student is considered to have shown improvement if they meet both of these conditions:
--
--Have taken exams in the same subject on at least two different dates
--Their latest score in that subject is higher than their first score
--Return the result table ordered by student_id, subject in ascending order.
--
--
--
--1.
WITH grouped AS (
    SELECT
        student_id,
        subject,
        MIN(exam_date) AS date_prev,
        MAX(exam_date) AS date_cur
    FROM Scores

    GROUP BY student_id, subject
)
SELECT
    base.student_id,
    base.subject,
    sub_prev.score AS first_score,
    sub_cur.score AS latest_score
FROM grouped AS base

INNER JOIN Scores AS sub_prev
    ON sub_prev.student_id = base.student_id
    AND sub_prev.subject = base.subject
    AND sub_prev.exam_date = date_prev

INNER JOIN Scores AS sub_cur
    ON sub_cur.student_id = base.student_id
    AND sub_cur.subject = base.subject
    AND sub_cur.exam_date = date_cur

WHERE sub_prev.score < sub_cur.score

ORDER BY student_id ASC, subject ASC;
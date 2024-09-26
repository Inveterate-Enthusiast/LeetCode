Table: Schools

+-------------+------+
| Column Name | Type |
+-------------+------+
| school_id   | int  |
| capacity    | int  |
+-------------+------+
school_id is the column with unique values for this table.
This table contains information about the capacity of some schools. The capacity is the maximum number of students the school can accept.


Table: Exam

+---------------+------+
| Column Name   | Type |
+---------------+------+
| score         | int  |
| student_count | int  |
+---------------+------+
score is the column with unique values for this table.
Each row in this table indicates that there are student_count students that got at least score points in the exam.
The data in this table will be logically correct, meaning a row recording a higher score will have the same
or smaller student_count compared to a row recording a lower score. More formally,
for every two rows i and j in the table, if scorei > scorej then student_counti <= student_countj.


Every year, each school announces a minimum score requirement that a student needs to apply to it.
The school chooses the minimum score requirement based on the exam results of all the students:

They want to ensure that even if every student meeting the requirement applies, the school can accept everyone.
They also want to maximize the possible number of students that can apply.
They must use a score that is in the Exam table.
Write a solution to report the minimum score requirement for each school.
If there are multiple score values satisfying the above conditions, choose the smallest one.
If the input data is not enough to determine the score, report -1.

Return the result table in any order.


1.
WITH crossed AS
    (
    SELECT main.school_id, sub.score, (CASE WHEN main.capacity >= sub.student_count THEN TRUE ELSE FALSE END) AS greater
    FROM Schools AS main
    CROSS JOIN
    Exam AS sub
    ),
ranked AS
    (
    SELECT school_id, score, DENSE_RANK() OVER(PARTITION BY school_id ORDER BY score ASC) AS our_rank
    FROM crossed
    WHERE greater = TRUE
    )
SELECT main.school_id, COALESCE(sub.score, (-1)) AS score
FROM Schools AS main
LEFT JOIN
(SELECT * FROM ranked WHERE our_rank = 1) AS sub
ON main.school_id = sub.school_id;


2.
WITH merged AS
    (
    SELECT main.school_id, sub.score, DENSE_RANK() OVER(PARTITION BY school_id ORDER BY score ASC) AS our_rank
    FROM Schools AS main
    LEFT JOIN
    Exam AS sub
    ON main.capacity >= sub.student_count
    )
SELECT main.school_id, COALESCE(sub.score, (-1)) AS score
FROM Schools AS main
LEFT JOIN
(SELECT * FROM merged WHERE our_rank = 1) AS sub
ON main.school_id = sub.school_id;
Table: Tasks

+-------------+------+
| Column Name | Type |
+-------------+------+
| task_id     | int  |
| assignee_id | int  |
| submit_date | date |
+-------------+------+
task_id is the primary key (column with unique values) for this table.
Each row in this table contains the ID of a task, the id of the assignee, and the submission date.


Write a solution to report:

the number of tasks that were submitted during the weekend (Saturday, Sunday) as weekend_cnt, and
the number of tasks that were submitted during the working days as working_cnt.
Return the result table in any order.



1.
WITH with_days AS (
    SELECT
        *,
        TO_CHAR(submit_date, 'FMDay') AS day_name
        FROM Tasks
)
SELECT
(
    SELECT COUNT(DISTINCT task_id) FROM with_days WHERE day_name = 'Saturday' OR day_name = 'Sunday'
) AS weekend_cnt,
(
    SELECT COUNT(DISTINCT task_id) FROM with_days WHERE day_name <> 'Saturday' AND day_name <> 'Sunday'
) AS working_cnt
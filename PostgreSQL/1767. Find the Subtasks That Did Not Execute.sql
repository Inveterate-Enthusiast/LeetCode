Table: Tasks

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| task_id        | int     |
| subtasks_count | int     |
+----------------+---------+
task_id is the column with unique values for this table.
Each row in this table indicates that task_id was divided into subtasks_count subtasks labeled from 1 to subtasks_count.
It is guaranteed that 2 <= subtasks_count <= 20.


Table: Executed

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| task_id       | int     |
| subtask_id    | int     |
+---------------+---------+
(task_id, subtask_id) is the combination of columns with unique values for this table.
Each row in this table indicates that for the task task_id, the subtask with ID subtask_id was executed successfully.
It is guaranteed that subtask_id <= subtasks_count for each task_id.


Write a solution to report the IDs of the missing subtasks for each task_id.

Return the result table in any order.


1.
WITH unnested AS (
    SELECT
        task_id,
        GENERATE_SERIES(1, subtasks_count, 1) AS subtask_id
    FROM Tasks
)
SELECT
    main.task_id,
    main.subtask_id
FROM unnested AS main

LEFT JOIN Executed AS sub
    ON sub.task_id = main.task_id
    AND sub.subtask_id = main.subtask_id

WHERE sub.subtask_id IS NULL;
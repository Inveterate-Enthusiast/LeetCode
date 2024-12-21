--Table: Tasks
--
--+---------------+----------+
--| Column Name   | Type     |
--+---------------+----------+
--| task_id       | int      |
--| employee_id   | int      |
--| start_time    | datetime |
--| end_time      | datetime |
--+---------------+----------+
--(task_id, employee_id) is the primary key for this table.
--Each row in this table contains the task identifier, the employee identifier, and the start and end times of each task.
--Write a solution to find the total duration of tasks for each employee and the maximum number of concurrent tasks an
--employee handled at any point in time. The total duration should be rounded down to the nearest number of full hours.
--
--Return the result table ordered by employee_id ascending order.
--
--
--
--1.
WITH with_prev_end AS (
    SELECT
        *,
        LAG(end_time, 1) OVER(PARTITION BY employee_id ORDER BY start_time ASC, task_id ASC) AS prev_end
    FROM Tasks
),
with_overlap AS (
    SELECT
        *,
        EXTRACT(EPOCH FROM AGE(prev_end, start_time)) AS overlap_sec
    FROM with_prev_end
),
duration AS (
    SELECT
        employee_id,
        FLOOR(
            SUM(
                EXTRACT(EPOCH FROM AGE(end_time, start_time))
                -
                (CASE
                    WHEN COALESCE(overlap_sec, 0) > 0 THEN overlap_sec
                    ELSE 0
                END)
            )::NUMERIC
            /
            (60^2)::NUMERIC
        ) AS total_task_hours
    FROM with_overlap
    GROUP BY employee_id
),
unioned AS (
    SELECT
        employee_id,
        task_id,
        start_time AS our_time,
        1 AS change
    FROM Tasks

    UNION ALL

    SELECT
        employee_id,
        task_id,
        end_time AS our_time,
        (-1) AS change
    FROM Tasks
),
active_tasks AS (
    SELECT
        *,
        SUM(change) OVER(PARTITION BY employee_id ORDER BY our_time ASC, task_id ASC, change DESC) AS our_tasks
    FROM unioned
)
SELECT
    main.employee_id,
    main.total_task_hours,
    sub.max_concurrent_tasks
FROM duration AS main

INNER JOIN (
    SELECT
        employee_id,
        MAX(our_tasks) AS max_concurrent_tasks
    FROM active_tasks
    GROUP BY employee_id
) AS sub
    ON sub.employee_id = main.employee_id

ORDER BY employee_id ASC;
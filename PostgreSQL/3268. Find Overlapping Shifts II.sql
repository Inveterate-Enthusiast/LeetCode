--Table: EmployeeShifts
--
--+------------------+----------+
--| Column Name      | Type     |
--+------------------+----------+
--| employee_id      | int      |
--| start_time       | datetime |
--| end_time         | datetime |
--+------------------+----------+
--(employee_id, start_time) is the unique key for this table.
--This table contains information about the shifts worked by employees, including the start time, and end time.
--Write a solution to analyze overlapping shifts for each employee.
--Two shifts are considered overlapping if they occur on the same date and one shift's end_time is later than another shift's start_time.
--
--For each employee, calculate the following:
--
--The maximum number of shifts that overlap at any given time.
--The total duration of all overlaps in minutes.
--Return the result table ordered by employee_id in ascending order.
--
--
--1.
WITH shifts AS (
    SELECT
        *,
        ROW_NUMBER() OVER() AS our_row
    FROM EmployeeShifts
),
unioned AS (
    SELECT
        employee_id,
        start_time AS time,
        1 AS our_bool
    FROM shifts

    UNION ALL

    SELECT
        employee_id,
        end_time AS time,
        -1 AS our_bool
    FROM shifts
),
unioned_sub AS (
    SELECT
        *,
        SUM(our_bool) OVER(PARTITION BY employee_id ORDER BY time ASC, our_bool DESC) AS cum_shifts
    FROM unioned
),
grouped_shifts AS (
    SELECT
        employee_id,
        MAX(cum_shifts) AS max_overlapping_shifts
    FROM unioned_sub

    GROUP BY employee_id
),
merged AS (
    SELECT
        main.employee_id,
        EXTRACT(EPOCH FROM AGE(LEAST(main.end_time, sub.end_time), sub.start_time)) AS diff
    FROM shifts AS main

    INNER JOIN shifts AS sub
        ON sub.employee_id = main.employee_id
        AND sub.our_row != main.our_row
        AND sub.start_time >= main.start_time
        AND sub.start_time < main.end_time
),
grouped_duration AS (
    SELECT
        employee_id,
        FLOOR(SUM(diff) / 60) AS total_overlap_duration
    FROM merged

    GROUP BY employee_id
)
SELECT
    main.employee_id,
    main.max_overlapping_shifts,
    COALESCE(sub.total_overlap_duration, 0) AS total_overlap_duration
FROM grouped_shifts AS main

LEFT JOIN grouped_duration AS sub
    ON sub.employee_id = main.employee_id

ORDER BY main.employee_id ASC;
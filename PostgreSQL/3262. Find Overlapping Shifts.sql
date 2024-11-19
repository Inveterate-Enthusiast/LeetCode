Table: EmployeeShifts

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| start_time       | time    |
| end_time         | time    |
+------------------+---------+
(employee_id, start_time) is the unique key for this table.
This table contains information about the shifts worked by employees, including the start and end times on a specific date.
Write a solution to count the number of overlapping shifts for each employee.
Two shifts are considered overlapping if one shift’s end_time is later than another shift’s start_time.

Return the result table ordered by employee_id in ascending order.


1.
SELECT
    main.employee_id,
    COUNT(*) AS overlapping_shifts
FROM EmployeeShifts AS main

INNER JOIN EmployeeShifts AS sub
ON main.employee_id = sub.employee_id
AND main.start_time < sub.start_time
AND main.end_time > sub.start_time

GROUP BY main.employee_id
ORDER BY main.employee_id ASC;
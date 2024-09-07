Table: Calls

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| from_id     | int     |
| to_id       | int     |
| duration    | int     |
+-------------+---------+
This table does not have a primary key (column with unique values), it may contain duplicates.
This table contains the duration of a phone call between from_id and to_id.
from_id != to_id


Write a solution to report the number of calls and the total call duration between each pair of distinct persons (person1, person2) where person1 < person2.

Return the result table in any order.


1.
SELECT person1, person2, COUNT(duration) AS call_count, SUM(duration) AS total_duration
FROM (
    SELECT (CASE WHEN from_id < to_id THEN from_id ELSE to_id END) AS person1,
            (CASE WHEN from_id > to_id THEN from_id ELSE to_id END) AS person2,
            duration
    FROM Calls
)
GROUP BY person1, person2;
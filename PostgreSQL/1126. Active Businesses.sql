Table: Events

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| business_id   | int     |
| event_type    | varchar |
| occurrences   | int     |
+---------------+---------+
(business_id, event_type) is the primary key (combination of columns with unique values) of this table.
Each row in the table logs the info that an event of some type occurred at some business for a number of times.
The average activity for a particular event_type is the average occurrences across all companies that have this event.

An active business is a business that has more than one event_type such that their occurrences is strictly greater than the average activity for that event.

Write a solution to find all active businesses.

Return the result table in any order.


1.
WITH grouped AS
    (SELECT event_type, ((SUM(occurrences))::NUMERIC / (COUNT(event_type))::NUMERIC) AS our_avg
    FROM Events
    GROUP BY event_type)
SELECT main.business_id
FROM Events AS main
INNER JOIN
grouped AS sub
ON main.event_type = sub.event_type
WHERE main.occurrences > sub.our_avg
GROUP BY main.business_id
HAVING COUNT(main.business_id) > 1;

2.
WITH grouped AS
    (SELECT *, AVG(occurrences) OVER(PARTITION BY event_type) AS our_avg
    FROM Events)
SELECT business_id
FROM grouped
WHERE occurrences > our_avg
GROUP BY business_id
HAVING COUNT(business_id) > 1;
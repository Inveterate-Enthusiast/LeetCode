Table: Actions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| post_id       | int     |
| action_date   | date    | 
| action        | enum    |
| extra         | varchar |
+---------------+---------+
This table may have duplicate rows.
The action column is an ENUM (category) type of ('view', 'like', 'reaction', 'comment', 'report', 'share').
The extra column has optional information about the action, such as a reason for the report or a type of reaction.
extra is never NULL.
 

Write a solution to report the number of posts reported yesterday for each report reason. Assume today is 2019-07-05.

Return the result table in any order.



1.
WITH our_dist AS
(SELECT DISTINCT extra, post_id FROM Actions WHERE action_date = ('2019-07-05'::DATE - INTERVAL '1 DAYS') AND extra IS NOT NULL AND action = 'report')
SELECT extra AS report_reason, COUNT(extra) AS report_count FROM our_dist GROUP BY extra;
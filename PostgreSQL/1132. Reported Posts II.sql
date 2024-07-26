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


Table: Removals

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| post_id       | int     |
| remove_date   | date    |
+---------------+---------+
post_id is the primary key (column with unique values) of this table.
Each row in this table indicates that some post was removed due to being reported or as a result of an admin review.


Write a solution to find the average daily percentage of posts that got removed after being reported as spam, rounded to 2 decimal places.


1.
WITH merged AS
    (SELECT DISTINCT main.action_date, main.post_id, main.extra, (CASE WHEN sub.remove_date IS NULL then 0 ELSE 1 END) AS bool
    FROM Actions AS main
    LEFT JOIN
    Removals AS sub
    ON main.post_id = sub.post_id)
SELECT ROUND(AVG(our_avg), 2) AS average_daily_percent
FROM(
    SELECT action_date,
        (((SUM(bool))::NUMERIC / (COUNT(DISTINCT post_id))::NUMERIC) * 100) AS our_avg
    FROM merged
    WHERE extra = 'spam'
    GROUP BY action_date
);
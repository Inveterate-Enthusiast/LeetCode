Table: Activity

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| session_id    | int     |
| activity_date | date    |
| activity_type | enum    |
+---------------+---------+
This table may have duplicate rows.
The activity_type column is an ENUM (category) of type ('open_session', 'end_session', 'scroll_down', 'send_message').
The table shows the user activities for a social media website. 
Note that each session belongs to exactly one user.
 

Write a solution to find the average number of sessions per user for a period of 30 days ending 2019-07-27 inclusively, 
rounded to 2 decimal places. The sessions we want to count for a user are those with at least one activity in that time period.




1.
WITH grouped AS
(SELECT user_id, COUNT(DISTINCT session_id) AS count FROM Activity 
WHERE activity_date BETWEEN '2019-07-27'::DATE - INTERVAL '29 DAYS' AND '2019-07-27' 
GROUP BY user_id)
SELECT COALESCE(ROUND(AVG(count), 2), 0) AS average_sessions_per_user FROM grouped;
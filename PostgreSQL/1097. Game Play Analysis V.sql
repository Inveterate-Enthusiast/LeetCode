Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.


The install date of a player is the first login day of that player.

We define day one retention of some date x to be the number of players whose install date is x and they logged back in
on the day right after x, divided by the number of players whose install date is x, rounded to 2 decimal places.

Write a solution to report for each install date, the number of players that installed the game on that day, and the day one retention.

Return the result table in any order.


1.
WITH lead_sub AS
    (SELECT player_id, event_date,
    DENSE_RANK() OVER(PARTITION BY player_id ORDER BY event_date ASC) AS our_rank,
    LEAD(event_date, 1, event_date) OVER(PARTITION BY player_id ORDER BY event_date ASC) AS our_lead
    FROM Activity)
SELECT event_date AS install_dt,
SUM(CASE WHEN our_rank = 1 THEN 1 ELSE 0 END) AS installs,
ROUND(
((SUM(CASE WHEN (our_rank = 1) AND (our_lead = (event_date + INTERVAL '1 DAYS')) THEN 1 ELSE 0 END))::NUMERIC
/
(SUM(CASE WHEN our_rank = 1 THEN 1 ELSE 0 END))::NUMERIC),
2) AS Day1_retention
FROM lead_sub
GROUP BY event_date
HAVING SUM(CASE WHEN our_rank = 1 THEN 1 ELSE 0 END) > 0;
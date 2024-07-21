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
 

Write a solution to report the device that is first logged in for each player.

Return the result table in any order.

CREATE TABLE Activity (
	player_id INT NOT NULL,
	device_id INT NOT NULL,
	event_date DATE NOT NULL,
	games_played INT NOT NULL
	);
	
\COPY Activity FROM 'C:\Users\User\Desktop\Python Books\Files\LeetCode\data\csvs\512. Activity.csv' DELIMITER ';' CSV HEADER;

DROP TABLE Activity;

1.
WITH grouped AS
(SELECT player_id, MIN(event_date) AS first_date FROM Activity GROUP BY player_id)
SELECT main.player_id, main.device_id FROM Activity AS main INNER JOIN grouped AS sub ON main.player_id = sub.player_id AND main.event_date = sub.first_date;

2.
SELECT main.player_id, main.device_id FROM Activity AS main 
INNER JOIN 
(SELECT player_id, MIN(event_date) AS event_date FROM Activity GROUP BY player_id) AS sub ON
main.player_id = sub.player_id AND main.event_date = sub.event_date ORDER BY main.player_id ASC;

3.
SELECT DISTINCT player_id, device_id FROM 
(SELECT player_id, device_id, RANK() OVER(PARTITION BY player_id ORDER BY event_date) AS our_rank FROM Activity)
WHERE our_rank = 1;

4.
WITH ranked AS
(SELECT player_id, device_id, DENSE_RANK() OVER our_window AS our_rank FROM Activity WINDOW our_window AS (PARTITION BY player_id ORDER BY event_date))
SELECT DISTINCT player_id, device_id FROM ranked WHERE our_rank = 1;
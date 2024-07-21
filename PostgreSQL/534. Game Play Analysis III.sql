Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (column with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
 

Write a solution to report for each player and date, how many games played so far by the player. That is, the total number of games played by the player until that date. Check the example for clarity.

Return the result table in any order.

CREATE TABLE Activity (
	player_id INT NOT NULL,
	device_id INT NOT NULL,
	event_date DATE NOT NULL,
	games_played INT NOT NULL
	);
	
\COPY Activity FROM 'C:\Users\User\Desktop\Python Books\Files\LeetCode\data\csvs\534. Activity.csv' DELIMITER ';' CSV HEADER;

DROP TABLE Activity;


1.
SELECT player_id, event_date, 
SUM(games_played) OVER our_window AS games_played_so_far 
FROM Activity 
WINDOW our_window AS (PARTITION BY player_id ORDER BY event_date);

2.
SELECT main.player_id, main.event_date, SUM(sub.games_played) AS games_played_so_far 
FROM Activity AS main
INNER JOIN Activity AS sub ON
main.player_id = sub.player_id AND main.event_date >= sub.event_date
GROUP BY main.player_id, main.event_date ORDER BY main.player_id ASC, main.event_date ASC;
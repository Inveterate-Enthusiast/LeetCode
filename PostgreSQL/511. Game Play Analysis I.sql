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
 

Write a solution to find the first login date for each player.

Return the result table in any order.

CREATE TABLE Activity (
	player_id INT NOT NULL,
	device_id INT NOT NULL,
	event_date DATE NOT NULL,
	games_played INT NOT NULL
	);
	
\COPY Activity FROM 'C:\Users\User\Desktop\Python Books\Files\LeetCode\data\csvs\511. Activity.csv' DELIMITER ';' CSV HEADER;

DROP TABLE Activity;

1.
SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id ORDER BY player_id ASC;
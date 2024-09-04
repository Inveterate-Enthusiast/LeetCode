Table: TeamStats

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| team_id          | int     |
| team_name        | varchar |
| matches_played   | int     |
| wins             | int     |
| draws            | int     |
| losses           | int     |
+------------------+---------+
team_id is the unique key for this table.
This table contains team id, team name, matches_played, wins, draws, and losses.
Write a solution to calculate the points and rank for each team in the league. Points are calculated as follows:

3 points for a win
1 point for a draw
0 points for a loss
Note: Teams with the same points must be assigned the same rank.

Return the result table ordered by points in descending, and then by team_name in ascending order.


1.
SELECT team_id, team_name,
((wins * 3) + (draws)) AS points,
(RANK() OVER (ORDER BY ((wins * 3) + (draws)) DESC)) AS position
FROM TeamStats
ORDER BY points DESC, team_name ASC;
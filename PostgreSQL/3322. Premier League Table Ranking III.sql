Table: SeasonStats

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| season_id        | int     |
| team_id          | int     |
| team_name        | varchar |
| matches_played   | int     |
| wins             | int     |
| draws            | int     |
| losses           | int     |
| goals_for        | int     |
| goals_against    | int     |
+------------------+---------+
(season_id, team_id) is the unique key for this table.
This table contains season id, team id, team name, matches played, wins, draws, losses, goals scored (goals_for),
and goals conceded (goals_against) for each team in each season.
Write a solution to calculate the points, goal difference, and rank for each team in each season. The ranking should be determined as follows:

Teams are first ranked by their total points (highest to lowest)
If points are tied, teams are then ranked by their goal difference (highest to lowest)
If goal difference is also tied, teams are then ranked alphabetically by team name
Points are calculated as follows:

3 points for a win
1 point for a draw
0 points for a loss
Goal difference is calculated as: goals_for - goals_against

Return the result table ordered by season_id in ascending order, then by rank in ascending order, and finally by team_name in ascending order.




1.
WITH points AS (
    SELECT
        *,
        ((wins * 3) + draws) AS points,
        (goals_for - goals_against) AS goal_difference
    FROM SeasonStats
),
ranked AS (
    SELECT
        *,
        DENSE_RANK() OVER(PARTITION BY season_id ORDER BY points DESC, goal_difference DESC, team_name ASC) AS position
    FROM points
)
SELECT
    season_id,
    team_id,
    team_name,
    points,
    goal_difference,
    position
FROM ranked

ORDER BY season_id ASC, position ASC, team_name ASC;
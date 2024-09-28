Table: Teams

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| team_id        | int     |
| team_name      | varchar |
+----------------+---------+
team_id is the column with unique values for this table.
Each row contains information about one team in the league.


Table: Matches

+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| home_team_id    | int     |
| away_team_id    | int     |
| home_team_goals | int     |
| away_team_goals | int     |
+-----------------+---------+
(home_team_id, away_team_id) is the primary key (combination of columns with unique values) for this table.
Each row contains information about one match.
home_team_goals is the number of goals scored by the home team.
away_team_goals is the number of goals scored by the away team.
The winner of the match is the team with the higher number of goals.


Write a solution to report the statistics of the league.
The statistics should be built using the played matches where the winning team gets three points and the losing team gets no points.
If a match ends with a draw, both teams get one point.

Each row of the result table should contain:

team_name - The name of the team in the Teams table.
matches_played - The number of matches played as either a home or away team.
points - The total points the team has so far.
goal_for - The total number of goals scored by the team across all matches.
goal_against - The total number of goals scored by opponent teams against this team across all matches.
goal_diff - The result of goal_for - goal_against.
Return the result table ordered by points in descending order.
If two or more teams have the same points, order them by goal_diff in descending order.
If there is still a tie, order them by team_name in lexicographical order.



1.
WITH unioned AS
    (
    SELECT home_team_id AS team_id,
    COUNT(*) AS matches_played,
    (SUM(
        CASE
            WHEN home_team_goals > away_team_goals THEN 3
            WHEN home_team_goals < away_team_goals THEN 0
            ELSE 1
        END
    )) AS points,
    SUM(home_team_goals) AS goal_for,
    SUM(away_team_goals) AS goal_against
    FROM Matches
    GROUP BY home_team_id

    UNION ALL

    SELECT away_team_id AS team_id,
    COUNT(*) AS matches_played,
    (SUM(
        CASE
            WHEN away_team_goals > home_team_goals THEN 3
            WHEN away_team_goals < home_team_goals THEN 0
            ELSE 1
        END
    )) AS points,
    SUM(away_team_goals) AS goal_for,
    SUM(home_team_goals) AS goal_against
    FROM Matches
    GROUP BY away_team_id
    ),
grouped AS
    (
    SELECT team_id,
    SUM(matches_played) AS matches_played,
    SUM(points) AS points,
    SUM(goal_for) AS goal_for,
    SUM(goal_against) AS goal_against
    FROM unioned
    GROUP BY team_id
    )
SELECT sub.team_name, main.matches_played, main.points, main.goal_for, main.goal_against, (main.goal_for - main.goal_against) AS goal_diff
FROM grouped AS main
LEFT JOIN
Teams AS sub
ON main.team_id = sub.team_id
ORDER BY main.points DESC, goal_diff DESC, sub.team_name ASC;
Table: Teams

+---------------+----------+
| Column Name   | Type     |
+---------------+----------+
| team_id       | int      |
| team_name     | varchar  |
+---------------+----------+
team_id is the column with unique values of this table.
Each row of this table represents a single football team.


Table: Matches

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| match_id      | int     |
| host_team     | int     |
| guest_team    | int     |
| host_goals    | int     |
| guest_goals   | int     |
+---------------+---------+
match_id is the column of unique values of this table.
Each row is a record of a finished match between two different teams.
Teams host_team and guest_team are represented by their IDs in the Teams table (team_id), and they scored host_goals and guest_goals goals, respectively.


You would like to compute the scores of all teams after all matches. Points are awarded as follows:
A team receives three points if they win a match (i.e., Scored more goals than the opponent team).
A team receives one point if they draw a match (i.e., Scored the same number of goals as the opponent team).
A team receives no points if they lose a match (i.e., Scored fewer goals than the opponent team).
Write a solution that selects the team_id, team_name and num_points of each team in the tournament after all described matches.

Return the result table ordered by num_points in decreasing order. In case of a tie, order the records by team_id in increasing order.


1.
WITH new_column AS
    (SELECT *, (
        CASE
            WHEN host_goals > guest_goals THEN 'left'
            WHEN guest_goals > host_goals THEN 'right'
            ELSE 'None'
        END
    ) AS win
    FROM Matches),
concated AS
    (SELECT host_team AS team_id, SUM(
        CASE
            WHEN win = 'left' THEN 3
            WHEN win = 'None' THEN 1
            ELSE 0
        END
    ) AS num_points
    FROM new_column
    GROUP BY host_team

    UNION ALL

    SELECT guest_team AS team_id, SUM(
        CASE
            WHEN win = 'right' THEN 3
            WHEN win = 'None' THEN 1
            ELSE 0
        END
    ) AS num_points
    FROM new_column
    GROUP BY guest_team),
grouped AS
    (SELECT team_id, SUM(num_points) AS num_points
    FROM concated
    GROUP BY team_id)
SELECT main.team_id, main.team_name, COALESCE(sub.num_points, 0) AS num_points
FROM Teams AS main
LEFT JOIN
grouped AS sub
ON main.team_id = sub.team_id
ORDER BY
num_points DESC, main.team_id ASC;
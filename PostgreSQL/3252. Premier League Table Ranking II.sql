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
Write a solution to calculate the points, position, and tier for each team in the league. Points are calculated as follows:

3 points for a win
1 point for a draw
0 points for a loss
Note: Teams with the same points must be assigned the same position.

Tier ranking:

Divide the league into 3 tiers based on points:
Tier 1: Top 33% of teams
Tier 2: Middle 33% of teams
Tier 3: Bottom 34% of teams
In case of ties at tier boundaries, place tied teams in the higher tier.
Return the result table ordered by points in descending, and then by team_name in ascending order.


1.
WITH with_points AS (
    SELECT
        *,
        ((wins * 3) + draws) AS points
    FROM TeamStats
),
ranked AS (
    SELECT
        *,
        RANK() OVER(ORDER BY points DESC) AS position,
        COUNT(team_id) OVER() AS max_pos
    FROM with_points
)
SELECT
    team_name,
    points,
    position,
    (
        CASE
            WHEN position <= CEIL(max_pos * 0.33) THEN 'Tier 1'
            WHEN position > CEIL(max_pos * (1 - 0.33)) THEN 'Tier 3'
            ELSE 'Tier 2'
        END
    ) AS tier
FROM ranked

ORDER BY points DESC, team_name ASC;
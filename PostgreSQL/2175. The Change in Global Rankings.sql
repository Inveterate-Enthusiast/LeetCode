Table: TeamPoints

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| team_id     | int     |
| name        | varchar |
| points      | int     |
+-------------+---------+
team_id contains unique values.
Each row of this table contains the ID of a national team, the name of the country it represents,
and the points it has in the global rankings. No two teams will represent the same country.


Table: PointsChange

+---------------+------+
| Column Name   | Type |
+---------------+------+
| team_id       | int  |
| points_change | int  |
+---------------+------+
team_id contains unique values.
Each row of this table contains the ID of a national team and the change in its points in the global rankings.
points_change can be:
- 0: indicates no change in points.
- positive: indicates an increase in points.
- negative: indicates a decrease in points.
Each team_id that appears in TeamPoints will also appear in this table.


The global ranking of a national team is its rank after sorting all the teams by their points in descending order.
If two teams have the same points, we break the tie by sorting them by their name in lexicographical order.

The points of each national team should be updated based on its corresponding points_change value.

--Write a solution to calculate the change in the global rankings after updating each team's points.

Return the result table in any order.


1.
WITH first_rank AS
    (
    SELECT *, ROW_NUMBER() OVER(ORDER BY points DESC, name ASC) AS row
    FROM TeamPoints
    ),
second_rank AS
    (
    SELECT *, ROW_NUMBER() OVER(ORDER BY points DESC, name ASC) AS row
    FROM (
		SELECT main.team_id, main.name, COALESCE((main.points + sub.points_change), 0) AS points
		FROM TeamPoints AS main
		FULL OUTER JOIN
		PointsChange AS sub
		ON main.team_id = sub.team_id
		)
    )
SELECT 
	COALESCE(main.team_id, sub.team_id) AS team_id, 
	COALESCE(main.name, sub.name) AS name,
	(main.row - sub.row) AS rank_diff
FROM first_rank AS main
FULL OUTER JOIN
second_rank AS sub
ON main.team_id = sub.team_id;
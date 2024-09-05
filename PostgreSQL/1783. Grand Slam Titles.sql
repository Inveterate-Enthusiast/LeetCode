Table: Players

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| player_id      | int     |
| player_name    | varchar |
+----------------+---------+
player_id is the primary key (column with unique values) for this table.
Each row in this table contains the name and the ID of a tennis player.


Table: Championships

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| year          | int     |
| Wimbledon     | int     |
| Fr_open       | int     |
| US_open       | int     |
| Au_open       | int     |
+---------------+---------+
year is the primary key (column with unique values) for this table.
Each row of this table contains the IDs of the players who won one each tennis tournament of the grand slam.


Write a solution to report the number of grand slam tournaments won by each player. Do not include the players who did not win any tournament.

Return the result table in any order.



1.
SELECT main.player_id, sub.player_name, main.grand_slams_count
FROM (
    SELECT player_id, COUNT(player_id) AS grand_slams_count
    FROM (
        SELECT Wimbledon AS player_id
        FROM Championships

        UNION ALL

        SELECT Fr_open AS player_id
        FROM Championships

        UNION ALL

        SELECT US_open AS player_id
        FROM Championships

        UNION ALL

        SELECT Au_open AS player_id
        FROM Championships
    )
    GROUP BY player_id
) AS main
LEFT JOIN
Players AS sub
ON main.player_id = sub.player_id;



2.
WITH grouped AS
    (
    SELECT DISTINCT COALESCE(Wimbledon, Fr_open, US_open, Au_open) AS player_id,
    SUM(COUNT(*)) OVER(PARTITION BY COALESCE(Wimbledon, Fr_open, US_open, Au_open)) AS grand_slams_count
    FROM Championships
    GROUP BY GROUPING SETS(Wimbledon, Fr_open, US_open, Au_open)
    )
SELECT main.player_id, sub.player_name, main.grand_slams_count
FROM grouped AS main
LEFT JOIN
Players AS sub
ON main.player_id = sub.player_id;
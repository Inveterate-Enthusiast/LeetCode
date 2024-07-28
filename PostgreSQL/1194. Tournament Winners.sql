Table: Players

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| player_id   | int   |
| group_id    | int   |
+-------------+-------+
player_id is the primary key (column with unique values) of this table.
Each row of this table indicates the group of each player.
Table: Matches

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| match_id      | int     |
| first_player  | int     |
| second_player | int     |
| first_score   | int     |
| second_score  | int     |
+---------------+---------+
match_id is the primary key (column with unique values) of this table.
Each row is a record of a match, first_player and second_player contain the player_id of each match.
first_score and second_score contain the number of points of the first_player and second_player respectively.
You may assume that, in each match, players belong to the same group.


The winner in each group is the player who scored the maximum total points within the group. In the case of a tie, the lowest player_id wins.

Write a solution to find the winner in each group.

Return the result table in any order.


1.
WITH concated AS
    (SELECT first_player AS player_id, SUM(first_score) AS total
    FROM Matches
    GROUP BY first_player

    UNION ALL

    SELECT second_player AS player_id, SUM(second_score) AS total
    FROM Matches
    GROUP BY second_player),
grouped AS
    (SELECT player_id, SUM(total) AS total
    FROM concated
    GROUP BY player_id),
ranked AS
    (SELECT sub.group_id, main.player_id, DENSE_RANK() OVER(PARTITION BY sub.group_id ORDER BY main.total DESC, main.player_id ASC) AS our_rank
    FROM grouped AS main
    LEFT JOIN
    Players AS sub
    ON main.player_id = sub.player_id)
SELECT group_id, player_id
FROM ranked
WHERE our_rank = 1;

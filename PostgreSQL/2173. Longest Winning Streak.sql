--Table: Matches
--
--+-------------+------+
--| Column Name | Type |
--+-------------+------+
--| player_id   | int  |
--| match_day   | date |
--| result      | enum |
--+-------------+------+
--(player_id, match_day) is the primary key (combination of columns with unique values) for this table.
--Each row of this table contains the ID of a player, the day of the match they played, and the result of that match.
--The result column is an ENUM (category) type of ('Win', 'Draw', 'Lose').
--
--
--The winning streak of a player is the number of consecutive wins uninterrupted by draws or losses.
--
--Write a solution to count the longest winning streak for each player.
--
--Return the result table in any order.
--
--
--1.
WITH extra_col AS (
    SELECT
        *,
        (CASE WHEN NOT result = 'Win' THEN 1 ELSE 0 END) AS extra_col
    FROM Matches
),
our_window AS (
    SELECT
        *,
        SUM(extra_col) OVER(PARTITION BY player_id ORDER BY match_day ASC) AS cum_sum
    FROM extra_col
),
grouped AS (
    SELECT
        player_id,
        cum_sum,
        SUM(CASE WHEN result = 'Win' THEN 1 ELSE 0 END) AS cnt
    FROM our_window

    GROUP BY player_id, cum_sum
)
SELECT
    player_id,
    MAX(cnt) AS longest_streak
FROM grouped
GROUP BY player_id;
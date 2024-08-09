Table: Scores

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| player_name   | varchar |
| gender        | varchar |
| day           | date    |
| score_points  | int     |
+---------------+---------+
(gender, day) is the primary key (combination of columns with unique values) for this table.
A competition is held between the female team and the male team.
Each row of this table indicates that a player_name and with gender has scored score_point in someday.
Gender is 'F' if the player is in the female team and 'M' if the player is in the male team.


Write a solution to find the total score for each gender on each day.

Return the result table ordered by gender and day in ascending order.



1.
SELECT gender, day, SUM(score_points) OVER(PARTITION BY gender ORDER BY day ASC) AS total
FROM Scores
ORDER BY 1 ASC, 2 ASC;
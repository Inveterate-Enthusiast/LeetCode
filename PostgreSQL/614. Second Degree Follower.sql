Table: Follow

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| followee    | varchar |
| follower    | varchar |
+-------------+---------+
(followee, follower) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates that the user follower follows the user followee on a social network.
There will not be a user following themself.


A second-degree follower is a user who:

follows at least one user, and
is followed by at least one user.
Write a solution to report the second-degree users and the number of their followers.

Return the result table ordered by follower in alphabetical order.

1.
SELECT followee AS follower, COUNT(DISTINCT follower) AS num
FROM Follow
WHERE followee IN (SELECT DISTINCT follower FROM Follow WHERE followee IS NOT NULL)
GROUP BY followee
HAVING COUNT(DISTINCT follower) >= 1
ORDER BY followee ASC;
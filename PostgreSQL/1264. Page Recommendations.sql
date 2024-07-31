Table: Friendship

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user1_id      | int     |
| user2_id      | int     |
+---------------+---------+
(user1_id, user2_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates that there is a friendship relation between user1_id and user2_id.


Table: Likes

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| page_id     | int     |
+-------------+---------+
(user_id, page_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates that user_id likes page_id.


Write a solution to recommend pages to the user with user_id = 1 using the pages that your friends liked. It should not recommend pages you already liked.

Return result table in any order without duplicates.


1.
WITH friends AS
    (SELECT user2_id AS user_id
    FROM Friendship
    WHERE user1_id = 1

    UNION ALL

    SELECT user1_id AS user_id
    FROM Friendship
    WHERE user2_id = 1),
pages AS
    (SELECT main.page_id
    FROM Likes AS main
    INNER JOIN
    friends AS sub
    ON sub.user_id = main.user_id),
not_pages AS
    (SELECT page_id
    FROM Likes
    WHERE user_id = 1)
SELECT DISTINCT page_id AS recommended_page
FROM pages
EXCEPT
SELECT page_id
FROM not_pages;

2.
WITH friends AS
    (SELECT user2_id AS user_id
    FROM Friendship
    WHERE user1_id = 1

    UNION ALL

    SELECT user1_id AS user_id
    FROM Friendship
    WHERE user2_id = 1)
SELECT DISTINCT main.page_id AS recommended_page
FROM Likes AS main
INNER JOIN
friends AS sub
ON sub.user_id = main.user_id

EXCEPT

SELECT page_id
FROM Likes
WHERE user_id = 1;
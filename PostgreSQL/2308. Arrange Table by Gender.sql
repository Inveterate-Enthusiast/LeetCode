Table: Genders

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| gender      | varchar |
+-------------+---------+
user_id is the primary key (column with unique values) for this table.
gender is ENUM (category) of type 'female', 'male', or 'other'.
Each row in this table contains the ID of a user and their gender.
The table has an equal number of 'female', 'male', and 'other'.


Write a solution to rearrange the Genders table such that the rows alternate between 'female', 'other', and 'male' in order.
The table should be rearranged such that the IDs of each gender are sorted in ascending order.

Return the result table in the mentioned order.

1.
WITH ranked AS
    (
    SELECT *,
    DENSE_RANK() OVER(PARTITION BY gender ORDER BY user_id) AS our_rank,
    (CASE
        WHEN gender = 'female' THEN 1
        WHEN gender = 'other' THEN 2
        ELSE 3
    END) AS pos
    FROM Genders
    )
SELECT user_id, gender
FROM ranked
ORDER BY our_rank ASC, pos ASC;
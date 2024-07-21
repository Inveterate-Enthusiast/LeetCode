Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write a solution to report all the duplicate emails. Note that its guaranteed that the email field is not NULL.

Return the result table in any order.

!!!SOLUTION

1.
SELECT email FROM Person GROUP BY email HAVING COUNT(*) > 1;
2.
SELECT DISTINCT(main.email) FROM Person AS main, Person AS sub WHERE main.email = sub.email AND main.id <> sub.id;
3.
SELECT DISTINCT(main.email) FROM Person AS main JOIN Person AS sub ON main.email = sub.email AND main.id <> sub.id;
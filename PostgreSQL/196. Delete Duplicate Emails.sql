Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.

For Pandas users, please note that you are supposed to modify Person in place.

After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.

1.
WITH sub AS 
(SELECT *, ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn FROM Person)
DELETE FROM Person WHERE id IN (SELECT id FROM sub WHERE rn > 1);
2.
DELETE FROM Person AS main USING Person AS sub WHERE main.email = sub.email AND main.id > sub.id;
3.
WITH del AS 
(SELECT main.id FROM Person AS main JOIN Person AS sub ON main.email = sub.email AND main.id > sub.id)
DELETE FROM Person WHERE id IN (SELECT id FROM del);
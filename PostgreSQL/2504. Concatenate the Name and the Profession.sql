Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| person_id   | int     |
| name        | varchar |
| profession  | ENUM    |
+-------------+---------+
person_id is the primary key (column with a unique value) for this table.
Each row in this table contains a person's ID, name, and profession.
The profession column in an enum of the type ('Doctor', 'Singer', 'Actor', 'Player', 'Engineer', or 'Lawyer')


Write a solution to report each person's name followed by the first letter of their profession enclosed in parentheses.

Return the result table ordered by person_id in descending order.


1.
SELECT person_id, (name || '(' || LEFT(profession, 1) || ')') AS name
FROM Person
ORDER BY person_id DESC;
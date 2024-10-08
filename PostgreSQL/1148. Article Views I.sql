Table: Views

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.
 

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.


1.
SELECT DISTINCT main.author_id AS id FROM Views AS main 
INNER JOIN Views AS sub 
ON main.author_id = sub.viewer_id AND main.article_id = sub.article_id 
ORDER BY id ASC;

2.
SELECT DISTINCT author_id AS id FROM Views
WHERE (author_id, article_id) IN
(SELECT viewer_id, article_id FROM Views) ORDER BY id ASC;

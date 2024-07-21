Table: Submissions

+---------------+----------+
| Column Name   | Type     |
+---------------+----------+
| sub_id        | int      |
| parent_id     | int      |
+---------------+----------+
This table may have duplicate rows.
Each row can be a post or comment on the post.
parent_id is null for posts.
parent_id for comments is sub_id for another post in the table.
 

Write a solution to find the number of comments per post. The result table should contain post_id and its corresponding number_of_comments.

The Submissions table may contain duplicate comments. You should count the number of unique comments per post.

The Submissions table may contain duplicate posts. You should treat them as one post.

The result table should be ordered by post_id in ascending order.



1.
WITH merged AS
(SELECT DISTINCT main.sub_id AS sub_id, sub.sub_id AS comment FROM (SELECT sub_id FROM Submissions WHERE parent_id IS NULL) AS main LEFT JOIN Submissions AS sub
ON main.sub_id = sub.parent_id)
SELECT sub_id AS post_id, COUNT(comment) AS number_of_comments FROM merged GROUP BY sub_id ORDER BY post_id ASC;
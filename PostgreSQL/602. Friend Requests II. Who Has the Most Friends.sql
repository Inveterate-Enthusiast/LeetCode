Table: RequestAccepted

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
(requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.
 

Write a solution to find the people who have the most friends and the most friends number.

The test cases are generated so that only one person has the most friends.

1.
WITH grouped1 AS
	(SELECT requester_id AS id, COUNT(DISTINCT accepter_id) AS num
	FROM RequestAccepted
	GROUP BY requester_id),
grouped2 AS
	(SELECT accepter_id AS id, COUNT(DISTINCT requester_id) AS num
	FROM RequestAccepted
	GROUP BY accepter_id),
merged AS
	(SELECT COALESCE(main.id, sub.id) AS id, (COALESCE(main.num, 0) + COALESCE(sub.num, 0)) AS num
	FROM grouped1 AS main
	FULL OUTER JOIN
	grouped2 AS sub
	ON main.id = sub.id)
SELECT id, num
FROM merged
WHERE num = (SELECT MAX(num) FROM merged);


2.
WITH unioned AS
	(SELECT requester_id AS id FROM RequestAccepted
	UNION ALL
	SELECT accepter_id AS id FROM RequestAccepted),
grouped AS
	(SELECT id, COUNT(id) AS num
	FROM unioned
	GROUP BY id)
SELECT id, num
FROM grouped 
WHERE num = (SELECT MAX(num) FROM grouped);
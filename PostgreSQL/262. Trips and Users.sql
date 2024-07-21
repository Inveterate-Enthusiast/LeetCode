Table: Trips

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| client_id   | int      |
| driver_id   | int      |
| city_id     | int      |
| status      | enum     |
| request_at  | varchar  |     
+-------------+----------+
id is the primary key (column with unique values) for this table.
The table holds all taxi trips. Each trip has a unique id, while client_id and driver_id are foreign keys to the users_id at the Users table.
Status is an ENUM (category) type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').
 

Table: Users

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| users_id    | int      |
| banned      | enum     |
| role        | enum     |
+-------------+----------+
users_id is the primary key (column with unique values) for this table.
The table holds all users. Each user has a unique users_id, and role is an ENUM type of ('client', 'driver', 'partner').
banned is an ENUM (category) type of ('Yes', 'No').
 

The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

Write a solution to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.

Return the result table in any order.



1. -- Хороший код, но нужно фильтровать весь основной запрос, а не внутри расчета
WITH not_banned AS
	(SELECT users_id FROM Users WHERE banned = 'No')
SELECT request_at AS "Day",
(CASE 
	WHEN SUM(CASE 
				WHEN 
				client_id IN 
				(SELECT users_id FROM not_banned) 
				AND 
				driver_id IN 
				(SELECT users_id FROM not_banned) 
				THEN 1 ELSE 0 END
			) = 0
	THEN 0
	ELSE (
		ROUND(
		((SUM(CASE 
				WHEN 
				client_id IN 
				(SELECT users_id FROM not_banned) 
				AND 
				driver_id IN 
				(SELECT users_id FROM not_banned)
				AND
				status != 'completed'
				THEN 1 ELSE 0 END
			)
		)::NUMERIC / 
		(SUM(CASE 
				WHEN 
				client_id IN 
				(SELECT users_id FROM not_banned) 
				AND 
				driver_id IN 
				(SELECT users_id FROM not_banned) 
				THEN 1 ELSE 0 END
			)
		)::NUMERIC),
		2)
	)
END) AS "Cancellation Rate"
FROM Trips
WHERE request_at::DATE BETWEEN '2013-10-01'::DATE AND '2013-10-03'::DATE
GROUP BY request_at
ORDER BY request_at ASC;


2.
WITH not_banned AS
	(SELECT users_id FROM Users WHERE banned = 'No')
SELECT request_at AS "Day",
(CASE 
	WHEN COUNT(status) = 0 THEN 0
	ELSE (
		ROUND(
		(SUM(CASE
				WHEN status != 'completed'
				THEN 1 ELSE 0 END)
		)::NUMERIC / 
		COUNT(status)::NUMERIC,
		2)
	)
END) AS "Cancellation Rate"
FROM Trips
WHERE request_at::DATE BETWEEN '2013-10-01'::DATE AND '2013-10-03'::DATE
AND 
client_id IN (SELECT users_id FROM not_banned)
AND
driver_id IN (SELECT users_id FROM not_banned)
GROUP BY request_at
ORDER BY request_at ASC;
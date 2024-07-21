Table: FriendRequest

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| sender_id      | int     |
| send_to_id     | int     |
| request_date   | date    |
+----------------+---------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date of the request.
 

Table: RequestAccepted

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.
 

Find the overall acceptance rate of requests, which is the number of acceptance divided by the number of requests. Return the answer rounded to 2 decimals places.

Note that:

The accepted requests are not necessarily from the table friend_request. In this case, Count the total accepted requests (no matter whether they are in the original requests), and divide it by the number of requests to get the acceptance rate.
It is possible that a sender sends multiple requests to the same receiver, and a request could be accepted more than once. In this case, the ‘duplicated’ requests or acceptances are only counted once.
If there are no requests at all, you should return 0.00 as the accept_rate.





1.
WITH
sub_friend AS
(SELECT COUNT(*)::NUMERIC AS f_count FROM (SELECT COUNT(*) FROM FriendRequest GROUP BY sender_id, send_to_id)),
sub_accepted AS
(SELECT COUNT(*)::NUMERIC AS a_count FROM (SELECT COUNT(*) FROM RequestAccepted GROUP BY requester_id, accepter_id))
SELECT,
CASE
WHEN sub_accepted.a_count = 0 OR sub_friend.f_count = 0 THEN 0.00
ELSE
ROUND(sub_accepted.a_count / sub_friend.f_count, 2)
END AS accept_rate FROM sub_accepted, sub_friend;

2.
WITH
sub_friend AS
(SELECT DISTINCT sender_id, send_to_id FROM FriendRequest),
sub_accepted AS
(SELECT DISTINCT requester_id, accepter_id FROM RequestAccepted)
SELECT COALESCE(
	ROUND(
		(
			(SELECT COUNT(*)::NUMERIC FROM sub_accepted) / 
			(CASE WHEN (SELECT COUNT(*)::NUMERIC FROM sub_friend) = 0 THEN NULL ELSE (SELECT COUNT(*)::NUMERIC FROM sub_friend) END)
		), 
		2), 
	0.00) AS accept_rate;
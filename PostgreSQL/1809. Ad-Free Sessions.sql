Table: Playback

+-------------+------+
| Column Name | Type |
+-------------+------+
| session_id  | int  |
| customer_id | int  |
| start_time  | int  |
| end_time    | int  |
+-------------+------+
session_id is the column with unique values for this table.
customer_id is the ID of the customer watching this session.
The session runs during the inclusive interval between start_time and end_time.
It is guaranteed that start_time <= end_time and that two sessions for the same customer do not intersect.


Table: Ads

+-------------+------+
| Column Name | Type |
+-------------+------+
| ad_id       | int  |
| customer_id | int  |
| timestamp   | int  |
+-------------+------+
ad_id is the column with unique values for this table.
customer_id is the ID of the customer viewing this ad.
timestamp is the moment of time at which the ad was shown.


Write a solution to report all the sessions that did not get shown any ads.

Return the result table in any order.


1.
WITH merged AS
    (SELECT main.customer_id, main.timestamp, sub.session_id, sub.start_time, sub.end_time
    FROM Ads AS main
    FULL OUTER JOIN
    Playback AS sub
    ON
    main.customer_id = sub.customer_id)
SELECT session_id
FROM Playback
WHERE session_id NOT IN (SELECT session_id FROM merged WHERE start_time <= timestamp AND timestamp <= end_time);
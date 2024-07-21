Table: Cinema

+-------------+------+
| Column Name | Type |
+-------------+------+
| seat_id     | int  |
| free        | bool |
+-------------+------+
seat_id is an auto-increment column for this table.
Each row of this table indicates whether the ith seat is free or not. 1 means free while 0 means occupied.
 

Find all the consecutive available seats in the cinema.

Return the result table ordered by seat_id in ascending order.

The test cases are generated so that more than two seats are consecutively available.


1.
WITH
sub AS
(SELECT seat_id FROM Cinema WHERE free = 1)
SELECT seat_id FROM sub WHERE seat_id + 1 IN (SELECT seat_id FROM sub) OR seat_id - 1 IN (SELECT seat_id FROM sub) ORDER BY seat_id ASC;
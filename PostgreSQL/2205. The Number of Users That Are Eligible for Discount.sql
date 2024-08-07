Table: Purchases

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| user_id     | int      |
| time_stamp  | datetime |
| amount      | int      |
+-------------+----------+
(user_id, time_stamp) is the primary key (combination of columns with unique values) for this table.
Each row contains information about the purchase time and the amount paid for the user with ID user_id.


A user is eligible for a discount if they had a purchase in the inclusive interval of time [startDate, endDate]
with at least minAmount amount. To convert the dates to times, both dates should be considered as the start of the day
(i.e., endDate = 2022-03-05 should be considered as the time 2022-03-05 00:00:00).

Write a solution to report the number of users that are eligible for a discount.


1.
CREATE OR REPLACE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT AS $$
BEGIN
  RETURN (
	  -- Write your PostgreSQL query statement below.
      SELECT COALESCE(COUNT(DISTINCT user_id), 0) AS user_cnt
      FROM (SELECT user_id, MAX(amount) AS amount FROM Purchases WHERE time_stamp BETWEEN startDate::TIMESTAMP AND endDate::TIMESTAMP GROUP BY user_id)
      WHERE amount >= minAmount
  );
END;
$$ LANGUAGE plpgsql;
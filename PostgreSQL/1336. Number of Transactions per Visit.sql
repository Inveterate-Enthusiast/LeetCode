Table: Visits

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| visit_date    | date    |
+---------------+---------+
(user_id, visit_date) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates that user_id has visited the bank in visit_date.


Table: Transactions

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| user_id          | int     |
| transaction_date | date    |
| amount           | int     |
+------------------+---------+
This table may contain duplicates rows.
Each row of this table indicates that user_id has done a transaction of amount in transaction_date.
It is guaranteed that the user has visited the bank in the transaction_date.(i.e The Visits table contains (user_id, transaction_date) in one row)


A bank wants to draw a chart of the number of transactions bank visitors did in one visit to the bank
and the corresponding number of visitors who have done this number of transaction in one visit.

--Write a solution to find how many users visited the bank and didn't do any transactions, how many visited the bank and did one transaction, and so on.

The result table will contain two columns:

transactions_count which is the number of transactions done in one visit.
visits_count which is the corresponding number of users who did transactions_count in one visit to the bank.
transactions_count should take all values from 0 to max(transactions_count) done by one or more users.

Return the result table ordered by transactions_count.



1.
WITH merged AS
    (SELECT main.user_id, main.visit_date, sub.amount
    FROM Visits AS main
    LEFT JOIN
    Transactions AS sub
    ON main.user_id = sub.user_id AND main.visit_date = sub.transaction_date),
grouped AS
    (SELECT user_id, visit_date, COUNT(amount) AS transactions_count
    FROM merged
    GROUP BY user_id, visit_date),
new_grouped AS
    (SELECT transactions_count, COUNT(user_id) AS visits_count
    FROM grouped
    GROUP BY transactions_count)
SELECT main.transactions_count, COALESCE(sub.visits_count, 0) AS visits_count
FROM (SELECT GENERATE_SERIES(0, (SELECT MAX(transactions_count) FROM new_grouped), 1) AS transactions_count) AS main
LEFT JOIN
new_grouped AS sub
ON main.transactions_count = sub.transactions_count
ORDER BY main.transactions_count ASC;
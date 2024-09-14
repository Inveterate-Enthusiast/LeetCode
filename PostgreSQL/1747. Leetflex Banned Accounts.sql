Table: LogInfo

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| account_id  | int      |
| ip_address  | int      |
| login       | datetime |
| logout      | datetime |
+-------------+----------+
This table may contain duplicate rows.
The table contains information about the login and logout dates of Leetflex accounts. It also contains the IP address from which the account was logged in and out.
It is guaranteed that the logout time is after the login time.


Write a solution to find the account_id of the accounts that should be banned from Leetflex. An account should be banned if it was logged in at some moment from two different IP addresses.

Return the result table in any order.



1.
WITH merged AS
    (
    SELECT main.account_id, main.login AS login_left, sub.login AS login_right, sub.logout AS logout_right,
    main.ip_address AS ip_left, sub.ip_address AS ip_right
    FROM LogInfo AS main
    INNER JOIN
    LogInfo AS sub
    ON main.account_id = sub.account_id
    )
SELECT DISTINCT account_id
FROM merged
WHERE login_left BETWEEN login_right AND logout_right
AND ip_left != ip_right;
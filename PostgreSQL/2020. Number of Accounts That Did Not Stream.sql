Table: Subscriptions

+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| start_date  | date |
| end_date    | date |
+-------------+------+
account_id is the primary key column for this table.
Each row of this table indicates the start and end dates of an account's subscription.
Note that always start_date < end_date.


Table: Streams

+-------------+------+
| Column Name | Type |
+-------------+------+
| session_id  | int  |
| account_id  | int  |
| stream_date | date |
+-------------+------+
session_id is the primary key column for this table.
account_id is a foreign key from the Subscriptions table.
Each row of this table contains information about the account and the date associated with a stream session.


Write an SQL query to report the number of accounts that bought a subscription in 2021 but did not have any stream session.



1.
WITH sub_with_years AS (
    SELECT
        *,
        EXTRACT(YEAR FROM start_date) AS start_year,
        EXTRACT(YEAR FROM end_date) AS end_year
    FROM Subscriptions
),
filtered AS (
    SELECT * FROM sub_with_years WHERE (start_year <= 2021) AND (end_year >= 2021)
),
streams_with_years AS (
    SELECT
        *,
        EXTRACT(YEAR FROM stream_date) AS year
    FROM Streams
),
have_stream AS (
    SELECT
        main.account_id,
        COUNT(DISTINCT sub.session_id) AS count
        FROM filtered AS main
        LEFT JOIN
        (
            SELECT * FROM streams_with_years WHERE year = 2021
        )
        AS sub
        ON main.account_id = sub.account_id AND ((sub.year >= main.start_year) OR (sub.year <= main.end_year))
        GROUP BY main.account_id
),
merged AS (
    SELECT
        main.account_id,
        COALESCE(sub.count, 0) AS count
        FROM filtered AS main
        LEFT JOIN
        have_stream AS sub
        ON main.account_id = sub.account_id
)
SELECT COUNT(DISTINCT account_id) AS accounts_count
FROM merged
WHERE count = 0;
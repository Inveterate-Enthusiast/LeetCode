Table Person:

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| id             | int     |
| name           | varchar |
| phone_number   | varchar |
+----------------+---------+
id is the column of unique values for this table.
Each row of this table contains the name of a person and their phone number.
Phone number will be in the form 'xxx-yyyyyyy' where xxx is the country code (3 characters) and yyyyyyy is the phone number (7 characters)
where x and y are digits. Both can contain leading zeros.


Table Country:

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| name           | varchar |
| country_code   | varchar |
+----------------+---------+
country_code is the column of unique values for this table.
Each row of this table contains the country name and its code. country_code will be in the form 'xxx' where x is digits.


Table Calls:

+-------------+------+
| Column Name | Type |
+-------------+------+
| caller_id   | int  |
| callee_id   | int  |
| duration    | int  |
+-------------+------+
This table may contain duplicate rows.
Each row of this table contains the caller id, callee id and the duration of the call in minutes. caller_id != callee_id


A telecommunications company wants to invest in new countries. The company intends to invest in the countries
where the average call duration of the calls in this country is strictly greater than the global average call duration.

Write a solution to find the countries where this company can invest.

Return the result table in any order.


1.
WITH added AS
    (SELECT *, SUBSTRING(phone_number FROM '(\d{3})-.*') AS country_code
    FROM Person),
concated AS
    (SELECT caller_id AS id, duration
    FROM Calls

    UNION ALL

    SELECT callee_id AS id, duration
    FROM Calls),
merged AS
    (SELECT main.country_code, sub.duration
    FROM added AS main
    RIGHT JOIN
    concated AS sub
    ON main.id = sub.id),
grouped AS
    (SELECT country_code
    FROM merged
    GROUP BY country_code
    HAVING AVG(duration) > (SELECT AVG(duration) FROM merged))
SELECT sub.name AS country
FROM grouped AS main
LEFT JOIN
Country AS sub
ON main.country_code = sub.country_code;
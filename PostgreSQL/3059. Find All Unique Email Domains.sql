Table: Emails

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
Write a solution to find all unique email domains and count the number of individuals associated with each domain. Consider only those domains that end with .com.

Return the result table ordered by email domains in ascending order.



1.
SELECT REGEXP_MATCHES(email, '^.*?@(.*)$') AS email_domain, COUNT(email) AS count
FROM Emails
WHERE email ~ '^.*?@.*\.com$'
GROUP BY email_domain
ORDER BY email_domain ASC;


2.
SELECT SUBSTRING(email FROM '^.*?@(.*)$') AS email_domain, COUNT(email) AS count
FROM Emails
WHERE email ~ '^.*?@.*\.com$'
GROUP BY email_domain
ORDER BY email_domain ASC;
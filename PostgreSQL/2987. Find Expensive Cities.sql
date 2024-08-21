Table: Listings

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| listing_id  | int     |
| city        | varchar |
| price       | int     |
+-------------+---------+
listing_id is column of unique values for this table.
This table contains listing_id, city, and price.
Write a solution to find cities where the average home prices exceed the national average home price.

Return the result table sorted by city in ascending order.




1.
SELECT city
FROM Listings
GROUP BY city
HAVING AVG(price) > (SELECT AVG(price) FROM Listings)
ORDER BY city ASC;
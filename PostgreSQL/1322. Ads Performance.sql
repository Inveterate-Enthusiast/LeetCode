Table: Ads

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| ad_id         | int     |
| user_id       | int     |
| action        | enum    |
+---------------+---------+
(ad_id, user_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the ID of an Ad, the ID of a user, and the action taken by this user regarding this Ad.
The action column is an ENUM (category) type of ('Clicked', 'Viewed', 'Ignored').
 

A company is running Ads and wants to calculate the performance of each Ad.

Performance of the Ad is measured using Click-Through Rate (CTR) where:


Write a solution to find the ctr of each Ad. Round ctr to two decimal points.

Return the result table ordered by ctr in descending order and by ad_id in ascending order in case of a tie.


CREATE TABLE Ads (
	ad_id INT NOT NULL,
	user_id INT NOT NULL,
	action VARCHAR(150) NOT NULL
);
\COPY Ads FROM 'C:\Users\User\Desktop\Python Books\Files\LeetCode\data\csvs\1322. Ads Performance.csv' DELIMITER ';' CSV HEADER;

DROP TABLE Ads;

1.
WITH grouped AS
(SELECT ad_id, 
SUM(CASE WHEN action = 'Clicked' THEN 1 ELSE 0 END) AS clicked_count,
SUM(CASE WHEN action IN ('Clicked', 'Viewed') THEN 1 ELSE 0 END) AS all_count
FROM Ads GROUP BY ad_id)
SELECT ad_id, 
ROUND((CASE WHEN all_count = 0 THEN 0
ELSE (clicked_count::NUMERIC / all_count::NUMERIC)*100
END), 2) AS ctr 
FROM grouped 
ORDER BY ctr DESC, ad_id ASC;
-- Table: MyNumbers

-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | num         | int  |
-- +-------------+------+
-- This table may contain duplicates (In other words, there is no primary key for this table in SQL).
-- Each row of this table contains an integer.

--1.
WITH grouped AS
(SELECT num FROM MyNumbers GROUP BY num HAVING COUNT(*) = 1)
SELECT MAX(num) AS num FROM grouped;

--2.
WITH grouped AS
(SELECT num FROM MyNumbers GROUP BY num HAVING COUNT(*) = 1 ORDER BY num DESC FETCH FIRST 1 ROW ONLY)
SELECT NULLIF((SELECT num FROM grouped), NULL) AS num;

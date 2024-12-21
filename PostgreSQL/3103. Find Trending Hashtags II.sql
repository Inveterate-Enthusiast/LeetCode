--Table: Tweets
--
--+-------------+---------+
--| Column Name | Type    |
--+-------------+---------+
--| user_id     | int     |
--| tweet_id    | int     |
--| tweet_date  | date    |
--| tweet       | varchar |
--+-------------+---------+
--tweet_id is the primary key (column with unique values) for this table.
--Each row of this table contains user_id, tweet_id, tweet_date and tweet.
--It is guaranteed that all tweet_date are valid dates in February 2024.
--
--Write a solution to find the top 3 trending hashtags in February 2024. Every tweet may contain several hashtags.
--
--Return the result table ordered by count of hashtag, hashtag in descending order.
--
--
--
--1.
WITH hash_list AS (
    SELECT
        *,
        UNNEST(REGEXP_MATCHES(tweet, '#[\w]+', 'g')) AS hashtag
    FROM Tweets

    WHERE EXTRACT(YEAR FROM tweet_date) = 2024
    AND EXTRACT(MONTH FROM tweet_date) = 2
)
SELECT
    hashtag,
    COUNT(*) AS count
FROM hash_list

GROUP BY hashtag
ORDER BY count DESC, hashtag DESC
LIMIT 3;
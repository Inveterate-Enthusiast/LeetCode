Table: Tweets

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| tweet_id    | int     |
| tweet_date  | date    |
| tweet       | varchar |
+-------------+---------+
tweet_id is the primary key (column with unique values) for this table.
Each row of this table contains user_id, tweet_id, tweet_date and tweet.
Write a solution to find the top 3 trending hashtags in February 2024. Each tweet only contains one hashtag.

Return the result table orderd by count of hashtag, hashtag in descending order.


1.
WITH re AS (
    SELECT
        *,
        SUBSTRING(tweet, '#\w+') AS hashtag
    FROM Tweets
),
grouped AS (
    SELECT
        hashtag,
        COUNT(*) AS hashtag_count
    FROM re
    GROUP BY hashtag
),
ranked AS (
    SELECT
        *,
        DENSE_RANK() OVER(ORDER BY hashtag_count DESC) AS our_rank
    FROM grouped

)
SELECT
    hashtag,
    hashtag_count
FROM ranked
WHERE our_rank <= 3
ORDER BY hashtag_count DESC, hashtag DESC
LIMIT 3;
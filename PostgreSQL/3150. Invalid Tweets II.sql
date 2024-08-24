Table: Tweets

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
This table contains all the tweets in a social media app.
Write a solution to find invalid tweets. A tweet is considered invalid if it meets any of the following criteria:

It exceeds 140 characters in length.
It has more than 3 mentions.
It includes more than 3 hashtags.
Return the result table ordered by tweet_id in ascending order.




1.
SELECT tweet_id
FROM Tweets
WHERE (LENGTH(content) > 140) OR (content ~ '^.*?@.+@.+@.+@.+$') OR (content ~ '^.*?#.+#.+#.+#.+$')
ORDER BY tweet_id ASC;



2.
SELECT tweet_id
FROM Tweets
WHERE (LENGTH(content) > 140) OR (REGEXP_COUNT(content, '@\S+') > 3) OR (REGEXP_COUNT(content, '#\S+') > 3)
ORDER BY tweet_id ASC;
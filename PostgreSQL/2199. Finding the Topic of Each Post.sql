--Table: Keywords
--
--+-------------+---------+
--| Column Name | Type    |
--+-------------+---------+
--| topic_id    | int     |
--| word        | varchar |
--+-------------+---------+
--(topic_id, word) is the primary key (combination of columns with unique values) for this table.
--Each row of this table contains the id of a topic and a word that is used to express this topic.
--There may be more than one word to express the same topic and one word may be used to express multiple topics.
--
--
--Table: Posts
--
--+-------------+---------+
--| Column Name | Type    |
--+-------------+---------+
--| post_id     | int     |
--| content     | varchar |
--+-------------+---------+
--post_id is the primary key (column with unique values) for this table.
--Each row of this table contains the ID of a post and its content.
--Content will consist only of English letters and spaces.
--
--
--Leetcode has collected some posts from its social media website and is interested in finding the topics of each post. Each topic can be expressed by one or more keywords. If a keyword of a certain topic exists in the content of a post (case insensitive) then the post has this topic.
--
--Write a solution to find the topics of each post according to the following rules:
--
--If the post does not have keywords from any topic, its topic should be "Ambiguous!".
--If the post has at least one keyword of any topic, its topic should be a string of the IDs of its topics sorted in ascending order and separated by commas ','. The string should not contain duplicate IDs.
--Return the result table in any order.
--
--
--
--
--1.
WITH splited AS (
    SELECT
        post_id,
        UNNEST(STRING_TO_ARRAY(LOWER(content), ' ')) AS content
    FROM Posts
),
merged AS (
    SELECT
        main.post_id,
        sub.topic_id
    FROM splited AS main

    INNER JOIN Keywords AS sub
        ON LOWER(sub.word) = main.content
)
SELECT
    main.post_id,
    (
        CASE
            WHEN COUNT(sub.post_id) = 0
                THEN 'Ambiguous!'
            ELSE ARRAY_TO_STRING(ARRAY_AGG(DISTINCT sub.topic_id), ',')
        END
    ) AS topic
FROM Posts AS main

LEFT JOIN merged AS sub
    ON sub.post_id = main.post_id

GROUP BY main.post_id;
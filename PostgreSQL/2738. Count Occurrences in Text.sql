Table: Files

+-------------+---------+
| Column Name | Type    |
+-- ----------+---------+
| file_name   | varchar |
| content     | text    |
+-------------+---------+
file_name is the column with unique values of this table.
Each row contains file_name and the content of that file.
Write a solution to find the number of files that have at
least one occurrence of the words 'bull' and 'bear' as a standalone word, respectively, disregarding any instances
where it appears without space on either side (e.g. 'bullet', 'bears', 'bull.', or 'bear' at the beginning or
end of a sentence will not be considered)

Return the word 'bull' and 'bear' along with the corresponding
number of occurrences in any order.


1.
WITH cnt AS (
    SELECT
        *,
        ARRAY_LENGTH(REGEXP_MATCHES(content, '.* bull .*', 'g'), 1) AS bull,
        ARRAY_LENGTH(REGEXP_MATCHES(content, '.* bear .*', 'g'), 1) AS bear
    FROM Files
)
SELECT
    UNNEST(ARRAY['bull', 'bear']) AS word,
    UNNEST(ARRAY[SUM(bull), SUM(bear)]) AS count
FROM cnt;
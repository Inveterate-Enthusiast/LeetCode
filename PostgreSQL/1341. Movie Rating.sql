Table: Movies

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id is the primary key (column with unique values) for this table.
title is the name of the movie.


Table: Users

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.


Table: MovieRating

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) is the primary key (column with unique values) for this table.
This table contains the rating of a movie by a user in their review.
created_at is the user's review date.


Write a solution to:

Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.


1.
SELECT name AS results
FROM (
    SELECT main.user_id, sub.name, main.rating, DENSE_RANK() OVER(ORDER BY rating DESC, sub.name ASC) AS our_rank
    FROM (
        SELECT user_id, COUNT(rating) AS rating
        FROM MovieRating
        GROUP BY user_id
    ) AS main
    LEFT JOIN Users AS sub
    ON main.user_id = sub.user_id
)
WHERE our_rank = 1

UNION ALL

SELECT title AS results
FROM (
    SELECT main.movie_id, sub.title, main.our_avg, DENSE_RANK() OVER(ORDER BY main.our_avg DESC, sub.title ASC) AS our_rank
    FROM (
        SELECT movie_id, AVG(rating) AS our_avg
        FROM MovieRating
        WHERE TO_CHAR(created_at, 'YYYY-MM') = '2020-02'
        GROUP BY movie_id
    ) AS main
    LEFT JOIN Movies AS sub
    ON main.movie_id = sub.movie_id
)
WHERE our_rank = 1;
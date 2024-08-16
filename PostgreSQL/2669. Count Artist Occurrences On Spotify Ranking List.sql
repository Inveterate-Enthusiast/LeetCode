Table: Spotify

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| track_name  | varchar |
| artist      | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row contains an id, track_name, and artist.
Write a solution to find how many times each artist appeared on the Spotify ranking list.

--Return the result table having the artist's name along with the corresponding number of occurrences ordered by occurrence count in descending order.
If the occurrences are equal, then it’s ordered by the artist’s name in ascending order.


1.
WITH ranked AS
    (SELECT *, DENSE_RANK() OVER(PARTITION BY artist ORDER BY id ASC) AS our_rank
    FROM Spotify)
SELECT artist, MAX(our_rank) AS occurrences
FROM ranked
GROUP BY artist
ORDER BY occurrences DESC, artist ASC;


2.
SELECT artist, COUNT(id) AS occurrences
FROM Spotify
GROUP BY artist
ORDER BY occurrences DESC, artist ASC;
Table: books

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| book_id        | int     |
| title          | varchar |
| author         | varchar |
| published_year | int     |
| rating         | decimal |
+----------------+---------+
book_id is the unique key for this table.
Each row of this table contains information about a book including its unique ID, title, author, publication year, and rating.
--rating can be NULL, indicating that the book hasn't been rated yet.
Write a solution to find all books that have not been rated yet (i.e., have a NULL rating).

Return the result table ordered by book_id in ascending order.



1.
SELECT
    book_id,
    title,
    author,
    published_year
FROM books
WHERE rating IS NULL
ORDER BY book_id ASC;
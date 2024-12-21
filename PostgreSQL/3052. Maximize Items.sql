--Table: Inventory
--
--+----------------+---------+
--| Column Name    | Type    |
--+----------------+---------+
--| item_id        | int     |
--| item_type      | varchar |
--| item_category  | varchar |
--| square_footage | decimal |
--+----------------+---------+
--item_id is the column of unique values for this table.
--Each row includes item id, item type, item category and sqaure footage.
--Leetcode warehouse wants to maximize the number of items it can stock in a 500,000 square feet warehouse.
--It wants to stock as many prime items as possible, and afterwards use the remaining square footage to stock the most number of non-prime items.
--
--Write a solution to find the number of prime and non-prime items that can be stored in the 500,000 square feet warehouse.
--Output the item type with prime_eligible followed by not_prime and the maximum number of items that can be stocked.
--
--Note:
--
--Item count must be a whole number (integer).
--If the count for the not_prime category is 0, you should output 0 for that particular category.
--Return the result table ordered by item count in descending order.
--
--
--1.
WITH grouped AS (
    SELECT
        item_type,
        SUM(square_footage) AS foot,
        COUNT(DISTINCT item_id) AS items
    FROM Inventory

    GROUP BY item_type
)
SELECT
    main.item_type,
    (
        CASE
            WHEN main.item_type = 'prime_eligible' THEN sub.item_count
            ELSE FLOOR((500000 - sub.occupied_foot) / main.foot) * main.items
        END
    ) AS item_count
FROM grouped AS main

LEFT JOIN (
    SELECT
        (FLOOR(500000 / foot) * items) AS item_count,
        (FLOOR(500000 / foot) * foot) AS occupied_foot
    FROM grouped
    WHERE item_type = 'prime_eligible'
) AS sub
    ON TRUE

ORDER BY item_count DESC;
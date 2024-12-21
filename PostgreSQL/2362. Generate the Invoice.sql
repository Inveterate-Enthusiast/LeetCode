--Table: Products
--
--+-------------+------+
--| Column Name | Type |
--+-------------+------+
--| product_id  | int  |
--| price       | int  |
--+-------------+------+
--product_id contains unique values.
--Each row in this table shows the ID of a product and the price of one unit.
--
--
--Table: Purchases
--
--+-------------+------+
--| Column Name | Type |
--+-------------+------+
--| invoice_id  | int  |
--| product_id  | int  |
--| quantity    | int  |
--+-------------+------+
--(invoice_id, product_id) is the primary key (combination of columns with unique values) for this table.
--Each row in this table shows the quantity ordered from one product in an invoice.
--
--
--Write a solution to show the details of the invoice with the highest price. If two or more invoices have the same price, return the details of the one with the smallest invoice_id.
--
--Return the result table in any order.
--
--
--
--1.
WITH merged AS (
    SELECT
        main.invoice_id,
        main.product_id,
        main.quantity,
        (main.quantity * sub.price) AS price
    FROM Purchases AS main

    LEFT JOIN Products AS sub
        ON sub.product_id = main.product_id
),
grouped AS (
    SELECT
        invoice_id,
        SUM(price) AS amount
    FROM merged

    GROUP BY invoice_id
)
SELECT
    main.product_id,
    main.quantity,
    main.price
FROM merged AS main

INNER JOIN (
    SELECT
        invoice_id
    FROM grouped
    WHERE amount = (SELECT MAX(amount) FROM grouped)
    ORDER BY invoice_id ASC
    LIMIT 1
) AS sub
    ON sub.invoice_id = main.invoice_id;
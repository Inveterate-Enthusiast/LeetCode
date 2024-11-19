Table: Customers

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| customer_name | varchar |
| email         | varchar |
+---------------+---------+
customer_id is the column of unique values for this table.
Each row of this table contains the name and the email of a customer of an online shop.


Table: Contacts

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | id      |
| contact_name  | varchar |
| contact_email | varchar |
+---------------+---------+
(user_id, contact_email) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the name and email of one contact of customer with user_id.
This table contains information about people each customer trust. The contact may or may not exist in the Customers table.


Table: Invoices

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| invoice_id   | int     |
| price        | int     |
| user_id      | int     |
+--------------+---------+
invoice_id is the column of unique values for this table.
Each row of this table indicates that user_id has an invoice with invoice_id and a price.


Write a solution to find the following for each invoice_id:

customer_name: The name of the customer the invoice is related to.
price: The price of the invoice.
contacts_cnt: The number of contacts related to the customer.
trusted_contacts_cnt: The number of contacts related to the customer and at the same time they are customers to the shop.
(i.e their email exists in the Customers table.)
Return the result table ordered by invoice_id.



1.
SELECT
    main.invoice_id,
    cus_sub.customer_name,
    MAX(main.price) AS price,
    COUNT(con_sub.contact_name) AS contacts_cnt,
    COUNT(trust_sub.customer_name) AS trusted_contacts_cnt
FROM Invoices AS main

LEFT JOIN Customers AS cus_sub
    ON cus_sub.customer_id = main.user_id

LEFT JOIN Contacts AS con_sub
    ON con_sub.user_id = cus_sub.customer_id

LEFT JOIN Customers AS trust_sub
    ON trust_sub.email = con_sub.contact_email

GROUP BY main.invoice_id, cus_sub.customer_name
ORDER BY main.invoice_id ASC;
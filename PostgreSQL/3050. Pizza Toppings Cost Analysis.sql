Table: Toppings

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| topping_name | varchar |
| cost         | decimal |
+--------------+---------+
topping_name is the primary key for this table.
Each row of this table contains topping name and the cost of the topping.
Write a solution to calculate the total cost of all possible 3-topping pizza combinations from a given list of toppings.
The total cost of toppings must be rounded to 2 decimal places.

Note:

Do not include the pizzas where a topping is repeated. For example, ‘Pepperoni, Pepperoni, Onion Pizza’.
Toppings must be listed in alphabetical order. For example, 'Chicken, Onions, Sausage'. 'Onion, Sausage, Chicken' is not acceptable.
Return the result table ordered by total cost in descending order and combination of toppings in ascending order.


1.
WITH merged AS (
    SELECT
        pizza1.topping_name AS p1,
        pizza2.topping_name AS p2,
        pizza3.topping_name AS p3,
        ROUND((pizza1.cost + pizza2.cost + pizza3.cost), 2) AS total_cost
    FROM Toppings AS pizza1

    INNER JOIN Toppings AS pizza2
        ON pizza2.topping_name > pizza1.topping_name

    INNER JOIN Toppings AS pizza3
        ON pizza3.topping_name > pizza2.topping_name
)
SELECT
    CONCAT(p1, ',', p2, ',', p3) AS pizza,
    total_cost
FROM merged
ORDER BY total_cost DESC, pizza ASC;
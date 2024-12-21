--Table: Terms
--
--+-------------+------+
--| Column Name | Type |
--+-------------+------+
--| power       | int  |
--| factor      | int  |
--+-------------+------+
--power is the column with unique values for this table.
--Each row of this table contains information about one term of the equation.
--power is an integer in the range [0, 100].
--factor is an integer in the range [-100, 100] and cannot be zero.
--
--
--You have a very powerful program that can solve any equation of one variable in the world.
-- The equation passed to the program must be formatted as follows:
--
--The left-hand side (LHS) should contain all the terms.
--The right-hand side (RHS) should be zero.
--Each term of the LHS should follow the format "<sign><fact>X^<pow>" where:
--<sign> is either "+" or "-".
--<fact> is the absolute value of the factor.
--<pow> is the value of the power.
--If the power is 1, do not add "^<pow>".
--For example, if power = 1 and factor = 3, the term will be "+3X".
--If the power is 0, add neither "X" nor "^<pow>".
--For example, if power = 0 and factor = -3, the term will be "-3".
--The powers in the LHS should be sorted in descending order.
--Write a solution to build the equation.
--
--
--
--1.
WITH sub AS (
    SELECT
        *,
        CONCAT(
            (CASE WHEN factor < 0 THEN '-' ELSE '+' END),
            ABS(factor),
            (
                CASE
                    WHEN power = 0 THEN NULL
                    WHEN power = 1 THEN 'X'
                    ELSE CONCAT('X^', power)
                END
            )
        ) AS term
    FROM Terms
    ORDER BY power DESC
)
SELECT
    STRING_AGG(sub.term, '') || MAX(_end._end) AS equation
FROM sub
LEFT JOIN (SELECT '=0' AS _end) AS _end
    ON TRUE

WHERE NOT sub.term = '';
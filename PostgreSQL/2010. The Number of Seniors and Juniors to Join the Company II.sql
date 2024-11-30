-- Table: Candidates

--+-------------+------+
--| Column Name | Type |
--+-------------+------+
--| employee_id | int  |
--| experience  | enum |
--| salary      | int  |
--+-------------+------+
--employee_id is the column with unique values for this table.
--experience is an ENUM (category) of types ('Senior', 'Junior').
--Each row of this table indicates the id of a candidate, their monthly salary, and their experience.
--The salary of each candidate is guaranteed to be unique.
--
--
--A company wants to hire new employees. The budget of the company for the salaries is $70000. The company's criteria for hiring are:
--
--Keep hiring the senior with the smallest salary until you cannot hire any more seniors.
--Use the remaining budget to hire the junior with the smallest salary.
--Keep hiring the junior with the smallest salary until you cannot hire any more juniors.
--Write a solution to find the ids of seniors and juniors hired under the mentioned criteria.
--
--Return the result table in any order.


-- 1.
WITH windows AS (
    SELECT
        *,
        SUM(salary) OVER(PARTITION BY experience ORDER BY salary ASC) AS cum_salary
    FROM Candidates
    WHERE experience = 'Senior' OR experience = 'Junior'
),
filtering AS (
    SELECT
        main.*,
        (
            CASE
                WHEN main.experience = 'Senior' THEN main.cum_salary
                ELSE (70000 - COALESCE(sub.cum_salary, 0)) - main.cum_salary
            END
        ) AS second_cum
    FROM windows AS main

    LEFT JOIN windows AS sub
        ON sub.cum_salary = (SELECT MAX(cum_salary) FROM windows WHERE experience = 'Senior' AND cum_salary <= 70000)

    WHERE main.cum_salary <= 70000
)
SELECT DISTINCT
    employee_id
FROM filtering
WHERE second_cum >= 0
--Table: Candidates
--
--+-------------+------+
--| Column Name | Type |
--+-------------+------+
--| employee_id | int  |
--| experience  | enum |
--| salary      | int  |
--+-------------+------+
--employee_id is the column with unique values for this table.
--experience is an ENUM (category) type of values ('Senior', 'Junior').
--Each row of this table indicates the id of a candidate, their monthly salary, and their experience.
--
--
--A company wants to hire new employees. The budget of the company for the salaries is $70000. The company's criteria for hiring are:
--
--Hiring the largest number of seniors.
--After hiring the maximum number of seniors, use the remaining budget to hire the largest number of juniors.
--Write a solution to find the number of seniors and juniors hired under the mentioned criteria.
--
--Return the result table in any order.


--1.
WITH windows AS (
    SELECT
        *,
        SUM(salary) OVER(PARTITION BY experience ORDER BY salary ASC) AS cum_salary
    FROM Candidates
    WHERE experience = 'Senior' OR experience = 'Junior'
),
sub AS (
    SELECT
        main.*,
        (
            CASE
                WHEN main.experience = 'Senior' THEN main.cum_salary
                ELSE COALESCE(70000 - sub.cum_salary, 70000) - main.cum_salary
            END
        ) AS second_cum
    FROM windows AS main

    LEFT JOIN windows AS sub
        ON sub.cum_salary = (SELECT MAX(cum_salary) FROM windows WHERE experience = 'Senior' AND cum_salary <= 70000)

    WHERE main.cum_salary <= 70000
)
SELECT
    main.experience,
    COALESCE(COUNT(DISTINCT sub.employee_id), 0) AS accepted_candidates
FROM windows AS main

LEFT JOIN sub
    ON sub.experience = main.experience
    AND sub.second_cum >= 0
GROUP BY main.experience;
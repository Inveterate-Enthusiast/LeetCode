Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

-- в функциях требуется постоянные явные ссылки на столбцы

1.
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    WITH grouped AS
		(SELECT DISTINCT e.salary, DENSE_RANK() OVER (ORDER BY e.salary DESC) AS rank FROM Employee AS e)
	SELECT (SELECT grouped.salary FROM grouped WHERE rank = N)
  );
END;
$$ LANGUAGE plpgsql;
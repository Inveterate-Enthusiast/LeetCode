Table: Countries

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| country_id    | int     |
| country_name  | varchar |
+---------------+---------+
country_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID and the name of one country.
 

Table: Weather

+---------------+------+
| Column Name   | Type |
+---------------+------+
| country_id    | int  |
| weather_state | int  |
| day           | date |
+---------------+------+
(country_id, day) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the weather state in a country for one day.
 

Write a solution to find the type of weather in each country for November 2019.

The type of weather is:

Cold if the average weather_state is less than or equal 15,
Hot if the average weather_state is greater than or equal to 25, and
Warm otherwise.
Return the result table in any order.




1.
WITH grouped AS
(SELECT country_id, AVG(weather_state) AS avg_weather FROM Weather WHERE day BETWEEN '2019-11-01'::DATE AND '2019-11-30'::DATE GROUP BY country_id)
SELECT sub.country_name,
(CASE 
	WHEN main.avg_weather <= 15 THEN 'Cold'
	WHEN main.avg_weather >= 25 THEN 'Hot'
	ELSE 'Warm'
END) AS weather_type
FROM grouped AS main LEFT JOIN Countries AS sub
ON main.country_id = sub.country_id;
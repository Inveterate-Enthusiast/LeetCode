Table: Experiments

+-----------------+------+
| Column Name     | Type |
+-----------------+------+
| experiment_id   | int  |
| platform        | enum |
| experiment_name | enum |
+-----------------+------+
experiment_id is the column with unique values for this table.
platform is an enum (category) type of values ('Android', 'IOS', 'Web').
experiment_name is an enum (category) type of values ('Reading', 'Sports', 'Programming').
This table contains information about the ID of an experiment done with a random person, the platform used to do the experiment, and the name of the experiment.


Write a solution to report the number of experiments done on each of the three platforms for each of the three given experiments.
Notice that all the pairs of (platform, experiment) should be included in the output including the pairs with zero experiments.

Return the result table in any order.


1.
WITH exp AS (
    SELECT UNNEST(ARRAY['Programming', 'Sports', 'Reading']) AS experiment_name
),
platforms AS (
    SELECT UNNEST(ARRAY['Android', 'IOS', 'Web']) AS platform
),
crossed AS (
    SELECT platforms.platform, exp.experiment_name
    FROM platforms
    CROSS JOIN
    exp
)
SELECT main.platform, main.experiment_name, COALESCE(sub.num_experiments, 0) AS num_experiments
FROM crossed AS main
LEFT JOIN
(SELECT experiment_name, platform, COUNT(experiment_id) AS num_experiments FROM Experiments GROUP BY 1, 2) AS sub
ON main.platform = sub.platform AND main.experiment_name = sub.experiment_name;
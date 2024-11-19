Table: Candidates

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| candidate_id | int     |
| skill        | varchar |
| proficiency  | int     |
+--------------+---------+
(candidate_id, skill) is the unique key for this table.
Each row includes candidate_id, skill, and proficiency level (1-5).
Table: Projects

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| project_id   | int     |
| skill        | varchar |
| importance   | int     |
+--------------+---------+
(project_id, skill) is the primary key for this table.
Each row includes project_id, required skill, and its importance (1-5) for the project.
Leetcode is staffing for multiple data science projects. Write a solution to find the best candidate for each project based on the following criteria:

Candidates must have all the skills required for a project.
Calculate a score for each candidate-project pair as follows:
Start with 100 points
Add 10 points for each skill where proficiency > importance
Subtract 5 points for each skill where proficiency < importance
Include only the top candidate (highest score) for each project. If there’s a tie, choose the candidate with the lower candidate_id.
If there is no suitable candidate for a project, do not return that project.

Return a result table ordered by project_id in ascending order.



1.
WITH merged AS (
    SELECT
        pro.project_id,
        can.candidate_id,
        pro.skill,
        pro.importance,
        can.proficiency,
        pro.pro_count,
        COUNT(can.skill) OVER(PARTITION BY project_id, candidate_id) AS can_count
    FROM (
        SELECT
            *,
            COUNT(skill) OVER(PARTITION BY project_id) AS pro_count
        FROM Projects
    ) AS pro

    LEFT JOIN Candidates AS can
        ON can.skill = pro.skill
),
filtered AS (
    SELECT
        project_id,
        candidate_id,
        100 + SUM(
            CASE
                WHEN proficiency > importance THEN 10
                WHEN proficiency < importance THEN (-5)
                ELSE 0
            END
        ) AS score
    FROM merged
    WHERE pro_count <= can_count
    GROUP BY project_id, candidate_id
),
ranked AS (
    SELECT
        *,
        DENSE_RANK() OVER(PARTITION BY project_id ORDER BY score DESC, candidate_id ASC) AS our_rank
    FROM filtered
)
SELECT
    project_id,
    candidate_id,
    score
FROM ranked
WHERE our_rank = 1
ORDER BY project_id ASC;
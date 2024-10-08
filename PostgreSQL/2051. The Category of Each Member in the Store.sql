Table: Members

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| member_id   | int     |
| name        | varchar |
+-------------+---------+
member_id is the column with unique values for this table.
Each row of this table indicates the name and the ID of a member.


Table: Visits

+-------------+------+
| Column Name | Type |
+-------------+------+
| visit_id    | int  |
| member_id   | int  |
| visit_date  | date |
+-------------+------+
visit_id is the column with unique values for this table.
member_id is a foreign key (reference column) to member_id from the Members table.
Each row of this table contains information about the date of a visit to the store and the member who visited it.


Table: Purchases

+----------------+------+
| Column Name    | Type |
+----------------+------+
| visit_id       | int  |
| charged_amount | int  |
+----------------+------+
visit_id is the column with unique values for this table.
visit_id is a foreign key (reference column) to visit_id from the Visits table.
Each row of this table contains information about the amount charged in a visit to the store.


A store wants to categorize its members. There are three tiers:

"Diamond": if the conversion rate is greater than or equal to 80.
"Gold": if the conversion rate is greater than or equal to 50 and less than 80.
"Silver": if the conversion rate is less than 50.
"Bronze": if the member never visited the store.
The conversion rate of a member is (100 * total number of purchases for the member) / total number of visits for the member.

Write a solution to report the id, the name, and the category of each member.

Return the result table in any order.



1.
WITH merged AS (
    SELECT
        main.member_id,
        main.visit_id,
        (CASE WHEN sub.visit_id IS NULL THEN 0 ELSE 1 END) AS our_check
        FROM Visits AS main
        LEFT JOIN
        Purchases AS sub
        ON main.visit_id = sub.visit_id
),
grouped AS (
    SELECT
        member_id,
        COUNT(DISTINCT visit_id) AS vis_count,
        SUM(our_check) AS pur_count
        FROM merged
        GROUP BY member_id
),
calculated AS (
    SELECT
        member_id,
        (
            CASE
                WHEN ((100 * pur_count) / vis_count) >= 80 THEN 'Diamond'
                WHEN ((100 * pur_count) / vis_count) < 50 THEN 'Silver'
                ELSE 'Gold'
            END
        ) AS category
    FROM grouped
)
SELECT
    main.member_id,
    main.name,
    COALESCE(sub.category, 'Bronze') AS category
FROM Members AS main
LEFT JOIN
calculated AS sub
ON main.member_id = sub.member_id;
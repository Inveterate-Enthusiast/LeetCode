--Table:  logs
--
--+-------------+---------+
--| Column Name | Type    |
--+-------------+---------+
--| log_id      | int     |
--| ip          | varchar |
--| status_code | int     |
--+-------------+---------+
--log_id is the unique key for this table.
--Each row contains server access log information including IP address and HTTP status code.
--Write a solution to find invalid IP addresses. An IPv4 address is invalid if it meets any of these conditions:
--
--Contains numbers greater than 255 in any octet
--Has leading zeros in any octet (like 01.02.03.04)
--Has less or more than 4 octets
--Return the result table ordered by invalid_count, ip in descending order respectively.
--
--
--
--
--1.
WITH split AS (
    SELECT
        log_id,
        ip,
        REGEXP_SPLIT_TO_ARRAY(ip, '\.') AS our_list
    FROM logs
),
unnested AS (
    SELECT
        *,
        (CASE WHEN ARRAY_LENGTH(our_list, 1) != 4 THEN 1 ELSE 0 END) AS bool_len,
        UNNEST(our_list) AS octet
    FROM split
),
final AS (
    SELECT
        *,
        (CASE WHEN octet::INT > 255 THEN 1 ELSE 0 END) AS bool_octet,
        (CASE WHEN (REGEXP_SPLIT_TO_ARRAY(octet, ''))[1]::INT = 0 THEN 1 ELSE 0 END) AS bool_zero
    FROM unnested
),
grouped AS (
    SELECT
        ip,
        COUNT(DISTINCT log_id) AS invalid_count,
        (SUM(bool_len) + SUM(bool_octet) + SUM(bool_zero)) AS filter
    FROM final

    GROUP BY ip
)
SELECT
    ip,
    invalid_count
FROM grouped

WHERE filter > 0

ORDER BY invalid_count DESC, ip DESC;
Table: user_permissions

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| permissions | int     |
+-------------+---------+
user_id is the primary key.
Each row of this table contains the user ID and their permissions encoded as an integer.
Consider that each bit in the permissions integer represents a different access level or feature that a user has.

Write a solution to calculate the following:

common_perms: The access level granted to all users. This is computed using a bitwise AND operation on the permissions column.
any_perms: The access level granted to any user. This is computed using a bitwise OR operation on the permissions column.
Return the result table in any order.



1.
SELECT
    BIT_AND(permissions) AS common_perms,
    BIT_OR(permissions) AS any_perms
FROM user_permissions;
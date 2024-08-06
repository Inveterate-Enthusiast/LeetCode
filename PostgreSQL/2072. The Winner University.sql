Table: NewYork

+-------------+------+
| Column Name | Type |
+-------------+------+
| student_id  | int  |
| score       | int  |
+-------------+------+
In SQL, student_id is the primary key for this table.
Each row contains information about the score of one student from New York University in an exam.


Table: California

+-------------+------+
| Column Name | Type |
+-------------+------+
| student_id  | int  |
| score       | int  |
+-------------+------+
In SQL, student_id is the primary key for this table.
Each row contains information about the score of one student from California University in an exam.


There is a competition between New York University and California University.
The competition is held between the same number of students from both universities.
The university that has more excellent students wins the competition.
If the two universities have the same number of excellent students, the competition ends in a draw.

An excellent student is a student that scored 90% or more in the exam.

Return:

"New York University" if New York University wins the competition.
"California University" if California University wins the competition.
"No Winner" if the competition ends in a draw.



1.
WITH new_york AS
    (SELECT COUNT(student_id) AS num
    FROM NewYork
    WHERE score >= 90),
california AS
    (SELECT COUNT(student_id) AS num
    FROM California
    WHERE score >= 90)
SELECT (
    CASE
        WHEN (SELECT num FROM new_york) > (SELECT num FROM california) THEN 'New York University'
        WHEN (SELECT num FROM new_york) < (SELECT num FROM california) THEN 'California University'
        ELSE 'No Winner'
    END
) AS winner;
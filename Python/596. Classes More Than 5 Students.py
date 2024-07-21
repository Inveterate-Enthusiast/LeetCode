# Table: Courses
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | student     | varchar |
# | class       | varchar |
# +-------------+---------+
# (student, class) is the primary key (combination of columns with unique values) for this table.
# Each row of this table indicates the name of a student and the class in which they are enrolled.

# Write a solution to find all the classes that have at least five students.
#
# Return the result table in any order.
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses.drop_duplicates(subset=["student", "class"])
    grouped = courses.groupby(
        by="class",
        as_index=False
    )["student"].count()
    return grouped[grouped["student"] >= 5][["class"]]

Courses = pd.DataFrame({
    "student": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
    "class": ["Math", "English", "Math", "Biology", "Math", "Computer", "Math", "Math", "Math"]
})

print(find_classes(Courses))

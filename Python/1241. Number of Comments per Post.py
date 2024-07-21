# Table: Submissions
#
# +---------------+----------+
# | Column Name   | Type     |
# +---------------+----------+
# | sub_id        | int      |
# | parent_id     | int      |
# +---------------+----------+
# This table may have duplicate rows.
# Each row can be a post or comment on the post.
# parent_id is null for posts.
# parent_id for comments is sub_id for another post in the table.

# Write a solution to find the number of comments per post. The result table should contain post_id and its corresponding number_of_comments.
#
# The Submissions table may contain duplicate comments. You should count the number of unique comments per post.
#
# The Submissions table may contain duplicate posts. You should treat them as one post.
#
# The result table should be ordered by post_id in ascending order.
import pandas as pd

def count_comments(submissions: pd.DataFrame) -> pd.DataFrame:
    submissions.drop_duplicates(subset=["sub_id", "parent_id"], inplace=True)
    merged = pd.merge(
        left=submissions[submissions["parent_id"].isna()],
        right=submissions[~submissions["parent_id"].isna()],
        left_on="sub_id",
        right_on="parent_id",
        how="left",
        copy=False,
        suffixes=("_sub", "_par")
    )
    return merged.groupby(by="sub_id_sub", as_index=False).agg(number_of_comments=("sub_id_par", "count")).rename(columns={"sub_id_sub": "post_id"})





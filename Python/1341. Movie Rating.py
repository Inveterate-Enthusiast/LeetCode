# Table: Movies
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | movie_id      | int     |
# | title         | varchar |
# +---------------+---------+
# movie_id is the primary key (column with unique values) for this table.
# title is the name of the movie.
#
#
# Table: Users
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | name          | varchar |
# +---------------+---------+
# user_id is the primary key (column with unique values) for this table.
#
#
# Table: MovieRating
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | movie_id      | int     |
# | user_id       | int     |
# | rating        | int     |
# | created_at    | date    |
# +---------------+---------+
# (movie_id, user_id) is the primary key (column with unique values) for this table.
# This table contains the rating of a movie by a user in their review.
# created_at is the user's review date.
#
#
# Write a solution to:
#
# Find the name of the user who has rated the greatest number of movies.
# In case of a tie, return the lexicographically smaller user name.

# Find the movie name with the highest average rating in February 2020.
# In case of a tie, return the lexicographically smaller movie name.
import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    grouped_users = (movie_rating
                     .groupby(by="user_id", as_index=False)
                     .agg(our_num=("rating", "count"))
                     .merge(right=users, on="user_id", how="left"))
    grouped_users.sort_values(by=["our_num", "name"], ascending=[False, True], inplace=True)
    grouped_users["our_rank"] = grouped_users.reset_index().index + 1

    grouped_movies = (movie_rating
                      .loc[movie_rating["created_at"].dt.strftime("%Y-%m") == "2020-02"]
                      .groupby(by="movie_id", as_index=False)
                      .agg(our_num=("rating", "mean"))
                      .merge(right=movies, on="movie_id", how="left"))
    grouped_movies.sort_values(by=["our_num", "title"], ascending=[False, True], inplace=True)
    grouped_movies["our_rank"] = grouped_movies.reset_index().index + 1

    return pd.DataFrame({
        "results": [(grouped_users.loc[grouped_users["our_rank"] == 1, "name"].iloc[0]),
                    (grouped_movies.loc[grouped_movies["our_rank"] == 1, "title"].iloc[0])]
    })
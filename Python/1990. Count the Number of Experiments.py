# Table: Experiments
#
# +-----------------+------+
# | Column Name     | Type |
# +-----------------+------+
# | experiment_id   | int  |
# | platform        | enum |
# | experiment_name | enum |
# +-----------------+------+
# experiment_id is the column with unique values for this table.
# platform is an enum (category) type of values ('Android', 'IOS', 'Web').
# experiment_name is an enum (category) type of values ('Reading', 'Sports', 'Programming').
# This table contains information about the ID of an experiment done with a random person,
# the platform used to do the experiment, and the name of the experiment.
#
#
# Write a solution to report the number of experiments done on each of the three platforms for each of the three given experiments.
# Notice that all the pairs of (platform, experiment) should be included in the output including the pairs with zero experiments.
#
# Return the result table in any order.
import pandas as pd

def count_experiments(experiments: pd.DataFrame) -> pd.DataFrame:
    platform = pd.DataFrame({
        "platform": ["Android", "IOS", "Web"]
    })
    experiment = pd.DataFrame({
        "experiment_name": ["Programming", "Sports", "Reading"]
    })
    common = pd.merge(
        left=platform,
        right=experiment,
        how="cross"
    )
    result = pd.merge(
        left=common,
        right=experiments.groupby(by=["platform", "experiment_name"]).agg(num_experiments=("experiment_id", "count")),
        how="left",
        on=["platform", "experiment_name"]
    ).fillna(0)
    return result


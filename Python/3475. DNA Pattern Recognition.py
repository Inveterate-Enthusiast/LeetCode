# Table: Samples
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | sample_id      | int     |
# | dna_sequence   | varchar |
# | species        | varchar |
# +----------------+---------+
# sample_id is the unique key for this table.
# Each row contains a DNA sequence represented as a string of characters (A, T, G, C) and the species it was collected from.
# Biologists are studying basic patterns in DNA sequences. Write a solution to identify sample_id with the following patterns:
#
# Sequences that start with ATG (a common start codon)
# Sequences that end with either TAA, TAG, or TGA (stop codons)
# Sequences containing the motif ATAT (a simple repeated pattern)
# Sequences that have at least 3 consecutive G (like GGG or GGGG)
# Return the result table ordered by sample_id in ascending order.


import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    atg_pattern = "^ATG"
    taa_pattern = "(TAA|TAG|TGA)$"
    atat_pattern = ".*ATAT.*"
    ggg_pattern = "G{3,}"
    samples["has_start"] = samples["dna_sequence"].str.contains(atg_pattern, regex=True, na=True).astype(int)
    samples["has_stop"] = samples["dna_sequence"].str.contains(taa_pattern, regex=True, na=True).astype(int)
    samples["has_atat"] = samples["dna_sequence"].str.contains(atat_pattern, regex=True, na=True).astype(int)
    samples["has_ggg"]  = samples["dna_sequence"].str.contains(ggg_pattern, regex=True, na=True).astype(int)
    return samples.sort_values(by="sample_id", ascending=True)
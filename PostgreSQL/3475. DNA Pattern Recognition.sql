--Table: Samples
--
--+----------------+---------+
--| Column Name    | Type    |
--+----------------+---------+
--| sample_id      | int     |
--| dna_sequence   | varchar |
--| species        | varchar |
--+----------------+---------+
--sample_id is the unique key for this table.
--Each row contains a DNA sequence represented as a string of characters (A, T, G, C) and the species it was collected from.
--Biologists are studying basic patterns in DNA sequences. Write a solution to identify sample_id with the following patterns:
--
--Sequences that start with ATG (a common start codon)
--Sequences that end with either TAA, TAG, or TGA (stop codons)
--Sequences containing the motif ATAT (a simple repeated pattern)
--Sequences that have at least 3 consecutive G (like GGG or GGGG)
--Return the result table ordered by sample_id in ascending order.
--
--
--
--1.
SELECT
    *,
    CAST(dna_sequence ~ '^ATG' AS INTEGER) AS has_start,
    CAST(dna_sequence ~ '(TAA|TAG|TGA)$' AS INTEGER) AS has_stop,
    CAST(dna_sequence ~ '.*ATAT.*' AS INTEGER) AS has_atat,
    CAST(dna_sequence ~ 'G{3,}' AS INTEGER) AS has_ggg
FROM Samples
ORDER BY sample_id ASC;
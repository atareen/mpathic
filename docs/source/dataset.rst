==========================================
``dataset``
==========================================

**Overview**

The datasets used in mpathic are pandas dataframes, comprising of columns of counts and sequence values. An example
of a valid dataset looks like


+------------------+------------------+---------------------------------+
|      ct          |      ct_1        | seq                             |
+==================+==================+=================================+
|      30          |      24          | AGWEMAKTSSGQRYFLNHIDQTTTW       |
+------------------+------------------+---------------------------------+
|      28          |      20          | AGWEMAKTSSGQRYFLNHIDRTTTW       |
+------------------+------------------+---------------------------------+
|      26          |      11          | AGWEMAKTRSGQRYFLNHIDQTTTW       |
+------------------+------------------+---------------------------------+

⋮

+------------------+------------------+---------------------------------+
|      2           |      1           | YVWEMAKTSSGQRYFLNHIDQTTTW       |
+------------------+------------------+---------------------------------+

**Specifications**::

    0. The dataframe must have at least one row.
    1. A 'tag' column is mandatory and must occur first. Values must be valid DNA sequences, all the same length.
    2. A single 'seq', 'seq_rna', or 'seq_pro' column is mandatory and must come second. Values must be valid DNA,
    RNA, or protein strings, all of the same length.
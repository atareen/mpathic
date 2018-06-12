==========================================
Tutorial
==========================================


Datasets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

   dataset_df = mpa.io.load_dataset('sort_seq_data.txt')
   model_df = mpa.io.load_model('crp_model.txt')
   contigs_list = mpa.io.load_contigs_from_fasta('genome_ecoli.fa', model_df)

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


Run MPAthic Classes
~~~~~~~~~~~~~~~~~~~
**Sort-Seq Simulations**::

   mpa.SimulateLibrary(wtseq="TAATGTGAGTTAGCTCACTCAT")
   mpa.SimulateSort(df=dataset_df,mp=model_df)

**Profiles**::

   mpa.ProfileInfo(dataset_df = dataset_df)
   mpa.ProfileMut(dataset_df = dataset_df)
   mpa.ProfileFreq(dataset_df = dataset_df)


**Models**::

   mpa.LearnModel(df=dataset_df)
   mpa.EvaluateModel(dataset_df = dataset_df, model_df = model_df)
   mpa.ScanModel(model_df = model_df, contigs_list = contigs_list)
   mpa.PredictiveInfo(data_df = dataset_df, model_df = model_df,start=52)
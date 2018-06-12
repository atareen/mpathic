==========================================
Tutorial
==========================================

We begin by importing the MPAthic package::

    import mpathic as mpa

We can use the :doc:`simulate_library` class to create a library of random mutants from an initial wildtype sequence and mutation rate::

    sim_library = mpa.SimulateLibrary(wtseq="TAATGTGAGTTAGCTCACTCAT", mutrate=0.24)
    sim_library.output_df.head()

The `output_df` attribute of the ``sim_library`` class looks like the dataframe below

+------------------+------------------------------+
|      ct          | seq                          |
+==================+==============================+
|      21          | TAATGTGAGTTAGCTCACTCAT       |
+------------------+------------------------------+
|      7           | TAATGTGAGTTAGCTAACTCAT       |
+------------------+------------------------------+
|      6           | TAATGTGAGTTAGCTCACTCAA       |
+------------------+------------------------------+

⋮

+------------------+------------------------------+
|      1           | TAATGTGTGTTCGCTCATCCAT       |
+------------------+------------------------------+


In general, MPAthic datasets are pandas dataframes, comprising of columns of counts and sequence values. To simulate
a Sort-Seq (pdf reference here) experiment, we use the :doc:`simulate_sort` class. This class requires a dataset input
and a model dataframe input. We first import these inputs using ``io`` module provided with the MPAthic package::

    # Load dataset and model dataframes
    dataset_df = mpa.io.load_dataset('sort_seq_data.txt')
    model_df = mpa.io.load_model('crp_model.txt')

    # Simulate a Sort-Seq experiment
    mpa.SimulateSort(df=dataset_df,mp=model_df)


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
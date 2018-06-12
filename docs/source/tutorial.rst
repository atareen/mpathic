==========================================
``Tutorial``
==========================================


Load Dataset and Model Dataframes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

   dataset_df = mpa.io.load_dataset('sort_seq_data.txt')
   model_df = mpa.io.load_model('crp_model.txt')
   contigs_list = mpa.io.load_contigs_from_fasta('genome_ecoli.fa', model_df)


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
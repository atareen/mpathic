==========================================
mpa.PredictiveInfo
==========================================

**Overview**

The predictive information class is a good way of assessing the quality of a model inferred from a massively parallel dataset.

**Usage**

	>>> loader = mpathic.io
    >>> dataset_df = loader.load_dataset(mpathic.__path__[0] + '/data/sortseq/full-0/library.txt')
    >>> mp_df = loader.load_model(mpathic.__path__[0] + '/examples/true_model.txt')
	>>> ss = mpathic.SimulateSort(df=dataset_df, mp=mp_df)
    >>> temp_ss = ss.output_df

    >>> temp_ss = ss.output_df
    >>> cols = ['ct', 'ct_0', 'ct_1', 'ct_2', 'ct_3', 'seq']
    >>> temp_ss = temp_ss[cols]
    >>> pi = mpathic.PredictiveInfo(data_df = temp_ss, model_df = mp_df, start=0)
    >>> print(pi.out_MI)


Class Details
-------------

.. autoclass:: predictive_info.PredictiveInfo
    :members:

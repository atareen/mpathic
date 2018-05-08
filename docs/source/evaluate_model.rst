.. _evaluate_model:

==========================================
``evaluate_model``
==========================================

.. contents::

Overview
-------------
``evaluate_model`` is able to make quantitative predictions of the activities of arbitrary
sequences. Specifically, it predicts the activities of models inferred from  :doc:`learn_model`


Usage
--------

	>>> import mpathic as mpa
	>>> model = mpa.io.load_model("./mpathic/data/sortseq/full-0/crp_model.txt")
	>>> dataset = mpa.io.load_dataset("./mpathic/data/sortseq/full-0/data.txt")
	>>> mpa.evaluate_model_class(dataset_df = dataset, model_df = model)



Example Input and Output
------------------------

The **evaluate_model** class needs expects two inputs in its constructor: a model dataframe
and the dataset. An example of each is given below

**Model Input Dataframe**::

    pos     val_A     val_C     val_G     val_T
    0     0  0.000831 -0.014006  0.144818 -0.131643
    1     1 -0.033734  0.087419 -0.029997 -0.023688
    2     2  0.009189  0.018999  0.026719 -0.054908
    3     3 -0.003516  0.073503  0.001759 -0.071745
    4     4  0.062168 -0.028879 -0.057249  0.023961
    ...


**Dataset Input Dataframe**::

    seq       ct_0       ct_1       ct_2       ct_3       ct_4

    AAAAAAGGTGAGTTA   0.000000   0.000000   1.000000   0.000000   0.000000
    AAAAAATATAAGTTA   0.000000   0.000000   0.000000   0.000000   1.000000
    AAAAAATATGATTTA   0.000000   0.000000   0.000000   1.000000   0.000000
    
**Example Output Table**::

	0        0.348108
	1       -0.248134
	2        0.009507
	3        0.238852
	4       -0.112121
	...


Class Details
-------------

.. automodule:: mpathic.src.evaluate_model_class
    :members: 


.. autoclass:: mpathic.src.evaluate_model_class.evaluate_model_class
    :members: 


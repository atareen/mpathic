==========================================
mpa.SimulateSort
==========================================

.. contents::

**Overview**

``SimulateSort`` is a program within the mpathic package which simulates
performing a Sort Seq experiment.


**Usage**

    >>> import mpathic
    >>> loader = mpathic.io
    >>> mp_df = loader.load_model('./mpathic/examples/true_model.txt')
    >>> dataset_df = loader.load_dataset('./mpathic/data/sortseq/full-0/library.txt')
    >>> mpathic.SimulateSort(df=dataset_df,mp=mp_df)

**Example Input and Output**

The input table to this function must contain sequence, counts, and energy columns

Example Input Table::

   seq    ct    val
   AGGTA  5     -.4
   AGTTA  1     -.2
   ...

Example Output Table::

   seq    ct    val    ct_1     ct_2     ct_3 ...
   AGGTA  5     -.4    1        2        1
   AGTTA  1     -.2    0        1        0
   ...

The output table will contain all the original columns, along with the sorted columns (ct_1, ct_2 ...)

Class Details
-------------

.. autoclass:: simulate_sort.SimulateSort
    :members:


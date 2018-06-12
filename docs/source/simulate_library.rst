==========================================
``SimulateLibrary``
==========================================

Overview
--------
simulate library is a program within the mpathic package which creates a library of
random mutants from an initial wildtype sequence and mutation rate.


Usage
-----

    >>> import mpathic
    >>> mpathic.simulate_library_class(wtseq="TAATGTGAGTTAGCTCACTCAT")


**Example Output Table**::

    ct            seq
    100           ACAGGGTTAC
    50            ACGGGGTTAC
    ...


Class Details
-------------

.. autoclass:: simulate_library.SimulateLibrary
    :members: 

.. _simulate_library:

==========================================
``simulate_library``
==========================================

**Overview**

``simulate_library`` is a program within the mpathic package which creates a library of
random mutants from an initial wildtype sequence and mutation rate.


**Usage**

    >>> import mpathic as mpa
    >>> sl = mpa.simulate_library_class
    >>> sl.simulate_library_class(wtseq="TAATGTGAGTTAGCTCACTCAT")


**Example Output Table**::

    ct            seq
    100           ACAGGGTTAC
    50            ACGGGGTTAC
    ...


.. mpathic documentation master file, created by
   sphinx-quickstart on Mon Apr 23 09:37:52 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


========
MPAthic
========

*Written by Ammar Tareen, William Ireland, and Justin B. Kinney.*

.. raw:: html

    <h1><font color="red">Under Active Development</font></h1>


MPAthic fits quantitative models to data. Barring a few exceptions, each method takes
one or more tabular text files as input and returns a tabular text file as output. All input and
output files are designed to be human readable. The first line of each tabular text file contains
headers describing the contents of each column. All input files are required to have the proper set of
columns, which of course depend on the command being executed. By default, input is taken from the standard
input and output is written to the standard output.


Welcome to mpathic's documentation!
===================================

.. toctree::

   dataset
   simulate_library
   simulate_sort
   profile
   learn_model
   evaluate_model



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Code for this and other examples can be found on the :doc:`dataset` page.
The :doc:`learn_model` page details the mpathic API.
==========================================
Installation Issues
==========================================

Fortran Compiler
----------------

1. Missing Fortran compiler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`pymc <https://docs.pymc.io/>`_ requires a fortran compiler in order to work. During installation, MPAthic will
look for existing fortran compilers on the users machine. If none are present, the following error will be thrown:

.. image:: _static/install_issues_1.png

Fix
~~~
We recommend installing `GCC <https://gcc.gnu.org/install/>`_, as this satisfy both Non-Python MPAthic
dependencies (i.e. Cython and pymc). In addition to official instructions, GCC can be obtained easily on
macOS via `homebrew <https://brew.sh/>`_::

    brew install gcc


Cython
------

1. Existing Cython versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/install_issues_2.png

2 Cython environment error
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/install_issues_3.png

Fix
~~~
Run the anaconda command::

    conda install -c anaconda cython

Or pip install directly::

    pip install Cython==0.28.1
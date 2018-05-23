#!/usr/bin/env python
'''
Calculates the fractional number of character occurances at each position within the set of sequences passed.
'''
from __future__ import division
import argparse
import numpy as np
import sys
import pandas as pd
import qc as qc
import io_local as io
import profile_ct as profile_ct
import pdb
from mpathic import SortSeqError
from utils import handle_errors, check, ControlledError

class profile_freq_class:

    """

    Profile Frequencies computes character frequencies (0.0 to 1.0) at each position

    Parameters
    ----------
    dataset_df: (pandas dataframe)
        A dataframe containing a valid dataset.

    bin: (int)
        A bin number specifying which counts to use

    start: (int)
        An integer specifying the sequence start position

    end: (int)
        An integer specifying the sequence end position

    Returns
    -------
    freq_df (pd.DataFrame):
        A dataframe containing counts for each nucleotide/amino \n
        acid character at each position.

    """

    @handle_errors
    def __init__(self,dataset_df, bin=None, start=0, end=None):

        # binding parameters to the instance of the class
        self.dataset_df = dataset_df
        self.bin = bin
        self.start = start
        self.end = end

        # this is resulting dataframe
        self.freq_df = None


        # do some input checking validation
        self._input_check()


        if dataset_df is not None:
            # check is dataframe is qc'ed
            qc.validate_dataset(dataset_df)

        else:
            raise SortSeqError("Input data set is None, please enter a valid dataset.")

        # Validate dataset_df
        qc.validate_dataset(dataset_df)

        # Compute counts
        counts_df = profile_ct.main(dataset_df, bin=bin, start=start, end=end)

        # Create columns for profile_freqs table
        ct_cols = [c for c in counts_df.columns if qc.is_col_type(c, 'ct_')]
        freq_cols = ['freq_' + c.split('_')[1] for c in ct_cols]

        # Compute frequencies from counts
        freq_df = counts_df[ct_cols].div(counts_df['ct'], axis=0)
        freq_df.columns = freq_cols
        freq_df['pos'] = counts_df['pos']

        # Validate as counts dataframe
        freq_df = qc.validate_profile_freq(freq_df, fix=True)

        self.freq_df = freq_df

    def _input_check(self):

        """
        check input parameters for correctness
        """

        check(isinstance(self.dataset_df, pd.DataFrame),
              'type(dataset_df) = %s; must be a pandas dataframe ' % type(self.dataset_df))

        if self.bin is not None:
            check(isinstance(self.bin, int),
                  'type(bin) = %s; must be of type int ' % type(self.bin))

            check(self.bin > 0, 'bin = %d must be a positive int ' % self.bin)

        if self.start is not None:
            check(isinstance(self.start, int),
                  'type(start) = %s; must be of type int ' % type(self.start))

        if self.end is not None:
            check(isinstance(self.end, int),
                  'type(end) = %s; must be of type int ' % type(self.end))










#!/usr/bin/env python

'''Simulate cell sorting based on expression'''
from __future__ import division
import argparse
import numpy as np
import scipy as sp
import pandas as pd
import sys
import Models as Models
import utils as utils
import io_local as io
import qc as qc
import evaluate_model as evaluate_model
from mpathic import SortSeqError


class simulate_sort_class:
    # def __init__(self,df,mp,noisetype,npar,nbins,sequence_library=True,start=0,end=None,chunksize=50000):
    def __init__(self, df, mp=None, noisetype='None', npar=[0.2], nbins=3, sequence_library=True, start=0,
                 end=None, chunksize=3):

        # validate noise parameters

        if not isinstance(npar, list):
            raise SortSeqError('Noise parameters must be given as a list')
        if noisetype == 'Normal':
            if len(npar) != 1:
                raise SortSeqError('''For a normal noise model, there must be one 
                         input parameter (width of normal distribution)''')
        if noisetype == 'LogNormal':
            if len(npar) != 2:
                raise SortSeqError('''For a LogNormal noise model there must 
                         be 2 input parameters''')
        if nbins <= 1:
            raise SortSeqError('number of bins must be greater than 1')
            # generate predicted energy of each sequence.


        # determine cutoffs for bins now
        # do progressive sum to try to find cutoffs so their will be equal numbers in each bin


            # Determine model type to use for noise
        if noisetype == 'LogNormal':
            NoiseModelSort = Models.LogNormalNoise(npar)
        elif noisetype == 'Normal':
            NoiseModelSort = Models.NormalNoise(npar)
        elif noisetype == 'None':
            NoiseModelSort = Models.NormalNoise([1e-16])
        elif noisetype == 'Plasmid':
            NoiseModelSort = Models.PlasmidNoise()
        else:
            NoiseModelSort = Models.CustomModel(noisetype, npar)
        i = 0
        output_df = pd.DataFrame()

        # split the dataframe according to chunksize
        df = np.array_split(df, chunksize)
        for chunk in df:
            # df -> pandas data frame
            # chunk is of type str. headings of the columns.

            chunk.reset_index(inplace=True, drop=True)
            chunk = evaluate_model.main(chunk, mp, left=start, right=None)
    
            # Apply noise to our calculated energies
            noisyexp, listnoisyexp = NoiseModelSort.genlist(chunk)
            if i == 0:
                # Determine Expression Cutoffs for bins
                noisyexp.sort()
                val_cutoffs = list(
                    noisyexp[np.linspace(0, len(noisyexp), nbins, endpoint=False, dtype=int)])
                val_cutoffs.append(np.inf)
                val_cutoffs[0] = -np.inf
            #print val_cutoffs
            # Determine Expression Cutoffs for bins
            seqs_arr = np.zeros([len(listnoisyexp), nbins], dtype=int)
            # split sequence into bins based on calculated cutoffs
            for i, entry in enumerate(listnoisyexp):
                seqs_arr[i, :] = np.histogram(entry, bins=val_cutoffs)[0]
            col_labels = ['ct_' + str(i + 1) for i in range(nbins)]
            if sequence_library:
                chunk.loc[:, 'ct_0'] = utils.sample(chunk.loc[:, 'ct'], int(chunk.loc[:, 'ct'].sum() / nbins))
            temp_output_df = pd.concat([chunk, pd.DataFrame(seqs_arr, columns=col_labels)], axis=1)
            col_labels = utils.get_column_headers(temp_output_df)
            # temp_output_df['ct'] = temp_output_df[col_labels].sum(axis=1)
            temp_output_df.drop('val', axis=1, inplace=True)
            #print temp_output_df.shape
            #print output_df.shape
            output_df = pd.concat([output_df, temp_output_df], axis=0).copy()
            i = i + 1

        output_df['ct'] = output_df[col_labels].sum(axis=1)
        output_df.reset_index(inplace=True, drop=True)

        #return output_df
        print(output_df.head())
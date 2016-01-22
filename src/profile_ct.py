#!/usr/bin/env python
'''
Calculates the total number of character occurances at each position within the set of sequences passed.
'''
from __future__ import division
import argparse
import numpy as np
import sys
import pandas as pd
import sst.qc as qc
import sst.io as io

def main(dataset_df, bin=None, start=0, end=None):
    """
    Computes character counts at each position

    Arguments:
        dataset_df (pd.DataFrame): A dataframe containing a valid dataset.
        bin (int): A bin number specifying which counts to use
        start (int): An integer specifying the sequence start position
        end (int): An integer specifying the sequence end position

    Returns:
        counts_df (pd.DataFrame): A dataframe containing counts for each nucleotide/amino acid character at each position. 
    """

    # Validate dataset_df
    qc.validate_dataset(dataset_df)

    # Retrieve type of sequence
    seq_cols = [c for c in dataset_df.columns if qc.is_col_type(c,'seqs')]
    if not len(seq_cols)==1:
        raise TypeError('Dataset dataframe must have only one seq colum.')
    seq_type = seq_cols[0]
    alphabet = qc.seq_alphabets_dict[seq_type]
    num_chars = len(alphabet)

    # Retrieve sequence length
    if not dataset_df.shape[0] > 1:
        raise TypeError('Dataset dataframe must have at least one row.')
    total_seq_length = len(dataset_df[seq_type].iloc[0])

    # Validate start and end
    if start<0:
        raise TypeError('start=%d is negative.'%start)
    elif start>=total_seq_length:
        raise TypeError('start=%d >= total_seq_length=%d'%\
            (start,total_seq_length))

    if end is None:
        end=total_seq_length
    elif end<=start:
        raise TypeError('end=%d <= start=%d.'%(end,start))
    elif end>total_seq_length:
        raise TypeError('end=%d > total_seq_length=%d'%\
            (start,total_seq_length))

    # Set positions
    poss = pd.Series(range(start,end),name='pos')
    num_poss = len(poss)

    # Retrieve counts
    if bin is None:
        ct_col = 'ct'
    else:
        ct_col = 'ct_%d'%bin
    if not ct_col in dataset_df.columns:
        raise TypeError('Column "%s" is not in columns=%s'%\
            (ct_col,str(dataset_df.columns)))
    counts = dataset_df[ct_col]

    # Compute counts profile
    counts_array = np.zeros([num_poss,num_chars])
    counts_cols = ['ct_'+a for a in alphabet]
    for i,pos in enumerate(range(start,end)):
        char_list = dataset_df[seq_type].str.slice(pos,pos+1)
        counts_array[i,:] = [np.sum(counts[char_list==a]) for a in alphabet]
    temp_df = pd.DataFrame(counts_array,columns=counts_cols)
    counts_df = pd.concat([poss,temp_df],axis=1)

    # Validate as counts dataframe
    counts_df = qc.validate_profile_ct(counts_df,fix=True)
    return counts_df


# Define commandline wrapper
def wrapper(args):
    
    # Load dataset dataframe
    if args.i:
        df = io.load_dataset(args.i)
    else:
        df = io.load_dataset(sys.stdin)
    
    # Compute counts profile dataframe
    output_df = main(df,bin=args.bin,start=args.start,end=args.end)

    # Set output buffer
    if args.out:
        outloc = open(args.out,'w')
    else:
        outloc = sys.stdout

    # Write results to file/stdout
    io.write(out_df,outloc)


# Connects argparse to wrapper
def add_subparser(subparsers):
    p = subparsers.add_parser('profile_ct')
    p.add_argument(
        '-b','--bin',default=None, help='''Dataset bin to use for counts. If blank, total counts will be used''')
    p.add_argument(
        '-i', '--i', default=None,help='''Input file, otherwise input through the standard input.''')
    p.add_argument(
        '-s','--start',type=int,default=0,help ='''Position to start your analyzed region''')
    p.add_argument(
        '-e','--end',type=int,default = None, help='''Position to end your analyzed region''')
    p.add_argument(\
        '-o', '--out', default=None,help='''Output file, otherwise use standard output.''')
    p.set_defaults(func=wrapper)

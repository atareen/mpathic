"""
The simulate library class generates simulated data for a Sort Seq Experiment
with a given mutation rate and wild type sequence.
"""

import argparse
import numpy as np
import scipy as sp
import pandas as pd
import sys
import utils as utils
import qc as qc
import io_local as io
from mpathic import SortSeqError
from utils import check, handle_errors
import pdb
from numpy.random import choice

class simulate_library_class:

    """

    parameters
    ----------
    wtseq: (string)
        wildtype sequence

    mutrate: (float)
        mutation rate

    numseq: (int)
        number of sequences

    dicttype: (string)
        sequence dictionary: valid choices include 'dna', 'rna', 'pro'

    probarr: (np.ndarray)
        probability matrix used to generate bases

    tags: (boolean)
        If simulating tags, each generated seq gets a unique tag

    tag_length: (int)
        Length of tags. Should be >= 0


    attributes
    ----------
    output_df: (pandas dataframe)
        Contains the output of simulate library in a pandas dataframe.


    """

    # main function for simulating library
    @handle_errors
    def __init__(
                 self,
                 wtseq="ACGTGTACGTAAATGATGAA",
                 mutrate=0.10,
                 numseq=10000,
                 dicttype='dna',
                 probarr=None,
                 tags=False,
                 tag_length=10):


        self.wtseq = wtseq
        self.mutrate = mutrate
        self.numseq = numseq
        self.dicttype = dicttype
        self.probarr = probarr
        self.tags = tags
        self.tag_length = tag_length

        # Validate inputs
        self._input_check()

        #generate sequence dictionary
        seq_dict,inv_dict = utils.choose_dict(dicttype)

        mutrate = float(mutrate)
        if (mutrate < 0.0) or (mutrate > 1.0):
            raise SortSeqError('Invalid mutrate==%f'%mutrate)

        numseq = int(numseq)
        if (numseq <= 0):
            raise SortSeqError('numseq must be positive. Is %d'%numseq)

        tag_length = int(tag_length)
        if (tag_length <= 0):
            raise SortSeqError('tag_length must be positive. Is %d'%tag_length)

        if isinstance(probarr,np.ndarray):
            L = probarr.shape[1]
            #Generate bases according to provided probability matrix
            letarr = np.zeros([numseq,L])
            for z in range(L):
                letarr[:,z] = np.random.choice(
                    range(len(seq_dict)),numseq,p=probarr[:,z])
        else:
            parr = []
            wtseq = wtseq.upper()
            L = len(wtseq)
            letarr = np.zeros([numseq,L])
            #Check to make sure the wtseq uses the correct bases.
            lin_seq_dict,lin_inv_dict = utils.choose_dict(dicttype,modeltype='MAT')
            def check_sequences(s):
                return set(s).issubset(lin_seq_dict)
            if not check_sequences(wtseq):
                raise SortSeqError(
                    'wtseq can only contain bases in ' + str(lin_seq_dict.keys()))
            #find wtseq array
            wtarr = self.seq2arr(wtseq,seq_dict)
            mrate = mutrate/(len(seq_dict)-1) #prob of non wildtype
            #Generate sequences by mutating away from wildtype
            '''probabilities away from wildtype (0 = stays the same, a 3 for 
                example means a C becomes an A, a 1 means C-> G)'''
            parr = np.array(
                [1-(len(seq_dict)-1)*mrate]
                + [mrate for i in range(len(seq_dict)-1)])
            #Generate random movements from wtseq
            letarr = np.random.choice(
                range(len(seq_dict)),[numseq,len(wtseq)],p=parr)
            #Find sequences
            letarr = np.mod(letarr + wtarr,len(seq_dict))
        seqs= []
        #Convert Back to letters
        for i in range(numseq):
            seqs.append(self.arr2seq(letarr[i,:],inv_dict))

        seq_col = qc.seqtype_to_seqcolname_dict[dicttype]
        seqs_df = pd.DataFrame(seqs, columns=[seq_col])

        # If simulating tags, each generated seq gets a unique tag
        if tags:
            tag_seq_dict,tag_inv_dict = utils.choose_dict('dna')
            tag_alphabet_list = tag_seq_dict.keys()

            # Make sure tag_length is long enough for the number of tags needed
            if len(tag_alphabet_list)**tag_length < 2*numseq:
                raise SortSeqError(\
                    'tag_length=%d is too short for num_tags_needed=%d'%\
                    (tag_length,numseq))

            # Generate a unique tag for each unique sequence
            tag_set = set([])
            while len(tag_set) < numseq:
                num_tags_left = numseq - len(tag_set)
                new_tags = [''.join(choice(tag_alphabet_list,size=tag_length)) \
                    for i in range(num_tags_left)]
                tag_set = tag_set.union(new_tags)

            df = seqs_df.copy()
            df.loc[:,'ct'] = 1
            df.loc[:,'tag'] = list(tag_set)

        # If not simulating tags, list only unique seqs w/ corresponding counts
        else:
            seqs_counts = seqs_df[seq_col].value_counts()
            df = seqs_counts.reset_index()
            df.columns = [seq_col,'ct']

        # Convert into valid dataset dataframe and return
        self.output_df = qc.validate_dataset(df,fix=True)
        print(self.output_df.head())


    def seq2arr(self,seq,seq_dict):
        '''Change base pairs to numbers'''
        return np.array([seq_dict[let] for let in seq])

    def arr2seq(self,arr,inv_dict):
        '''Change numbers back into base pairs.'''
        return ''.join([inv_dict[num] for num in arr])

    def _input_check(self):
        """
        Check all parameter values for correctness

        """
        # check if wtseq is valid
        check(isinstance(self.wtseq,str),'type(wtseq) = %s; must be a string ' % type(self.wtseq))

        # check if mutrate is valid
        check(isinstance(self.mutrate, float), 'type(mutrate) = %s; must be a float ' % type(self.mutrate))

        # check if numseq is valid
        check(isinstance(self.numseq, int), 'type(numseq) = %s; must be a float ' % type(self.numseq))

        # check if dicttype is valid
        check(isinstance(self.dicttype, str), 'type(dicttype) = %s; must be a string ' % type(self.dicttype))

        # check if probarr is valid
        check(isinstance(self.probarr, np.ndarray), 'type(probarr) = %s; must be an np.ndarray ' % type(self.probarr))

        # check if tags is valid
        check(isinstance(self.tags, bool), 'type(tags) = %s; must be an boolean ' % type(self.tags))

        # check if tag_length is valid
        check(isinstance(self.tag_length, bool), 'type(tag_length) = %s; must be an int ' % type(self.tag_length))
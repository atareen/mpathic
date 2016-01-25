#!/usr/bin/env python
'''This script will profile several of the functions in the sortseq package,
sort the results by cumulative time spent on each function and then print the
results to file. The 'main' function is the script that is being targeted.
The ones that are currently targeted are profile_info using the nsb estimator,
learn_matrix using LS, learn_matrix using IM and 5 iterations, and predictiveinfo.'''

from __future__ import division
import argparse
import numpy as np
import sys
import pandas as pd
import sst.qc as qc
import sst.io as io
import sst.profile_ct as profile_ct
import pdb
from sst import SortSeqError
import cProfile
import sst.profile_info as profile_info

#load in data sets for the test, we will just use the sort-seq crp-wt set

df = io.load_dataset(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                           'data/sortseq/crp-wt.txt'))
model_df = io.load_dataset(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                           'data/sortseq/crp-wt/test_old'))

#Profile profile_info
stats_fn = 'Profile_profile_info'
stats_fn_hr = 'Profile_profile_info_hr'
cProfile.run('''profile_info.main(df,method='nsb')''',stats_fn)

#Reformat and print to human readable profile
p = pstats.Stats(stats_fn,stream=stats_fn_hr)
pstats.strip_dirs()
p.sort_stats('cumtime')
p.print_stats()


#profile learn_matrix lm=LS
stats_fn = 'Profile_learn_matrix_LS'
stats_fn_hr = 'Profile_learn_matrix_LS_hr'
cProfile.run('''learn_matrix.main(df,'dna','LS')''',stats_fn)

#Reformat and print to human readable profile
p = pstats.Stats(stats_fn,stream=stats_fn_hr)
pstats.strip_dirs()
p.sort_stats('cumtime')
p.print_stats()

#profile learn_matrix lm=IM
stats_fn = 'Profile_learn_matrix_IM'
stats_fn_hr = 'Profile_learn_matrix_IM_hr'
cProfile.run('''learn_matrix.main(df,'dna','IM',iterations=5)''',stats_fn)

#Reformat and print to human readable profile
p = pstats.Stats(stats_fn,stream=stats_fn_hr)
pstats.strip_dirs()
p.sort_stats('cumtime')
p.print_stats()

#profile predictiveinfo
stats_fn = 'Profile_predictiveinfo'
stats_fn_hr = 'Profile_predictiveinfo_hr'
cProfile.run('''predictiveinfo.main(df,model_df)''',stats_fn)

#Reformat and print to human readable profile
p = pstats.Stats(stats_fn,stream=stats_fn_hr)
pstats.strip_dirs()
p.sort_stats('cumtime')
p.print_stats()

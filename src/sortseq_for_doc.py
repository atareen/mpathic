#!/usr/bin/env python2.7

''' Primary function for MPAthic.ools. Currently supports: 

simulate_library
simulate_sublib
simulate_MPAthic
simulate_selection
simulate_mpra
'''

from __future__ import division
import numpy as np
import scipy as sp
import argparse
import sys
import csv

# Create argparse parser. 
parser = argparse.ArgumentParser()

# All functions can specify and output file. Default is stdout.
parser.add_argument('-o','--out',default=False,help='Output location/type, by default it writes to standard output, if a file name is supplied it will write to a text file')

# Add various subcommands individually viva subparsers
subparsers = parser.add_subparsers()

# preprocess
import MPAthic.preprocess as preprocess
preprocess.add_subparser(subparsers)

#profile_mutrate
import MPAthic.profile_mut as profile_mut
profile_mut.add_subparser(subparsers)

#profile_mutrate
import MPAthic.profile_ct as profile_ct
profile_ct.add_subparser(subparsers)

#profile_mutrate
import MPAthic.profile_freq as profile_freq
profile_freq.add_subparser(subparsers)

#learn_model
import MPAthic.learn_model as learn_model
learn_model.add_subparser(subparsers)

#predictiveinfo
import MPAthic.predictiveinfo as predictiveinfo
predictiveinfo.add_subparser(subparsers)

#profile_info
import MPAthic.profile_info as profile_info
profile_info.add_subparser(subparsers)

#Scan
import MPAthic.scan_model as scan_model
scan_model.add_subparser(subparsers)

#simualte_library
import MPAthic.simulate_library as simulate_library
simulate_library.add_subparser(subparsers)

#simulate_sort
import MPAthic.simulate_sort as simulate_sort
simulate_sort.add_subparser(subparsers)

#evaluate_model

#simulate_sort
import MPAthic.evaluate_model as evaluate_model
evaluate_model.add_subparser(subparsers)

# #simulate_evaluate
# import MPAthic.simulate_evaluate as simulate_evaluate
# simulate_evaluate.add_subparser(subparsers)

#simulate_sort
import MPAthic.simulate_expression as simulate_expression
simulate_expression.add_subparser(subparsers)

# Final incantiation needed for this to work










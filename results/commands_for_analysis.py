#!/usr/bin/env python

from __future__ import division
import os
#Our standard Modules
import argparse
import numpy as np
import scipy as sp
import sys
#Our miscellaneous functions
import pandas as pd
import MPAthic.utils as utils
from sklearn import linear_model
'''commands to run all analysis. WARNING, this will take ~ 30 hours total.
Commands should probably be run individually'''

'''MCMC analysis'''
#learn CRP models
MPAthic learn_model -lm IM -i crp_models/crp-wt_formatted.txt -o crp-wt_MCMC_crp -s 3 -e 25
MPAthic learn_model -lm LS -i crp_models/crp-wt_formatted.txt -o crp-wt_LS_crp -s 3 -e 25
MPAthic learn_model -lm ER -i crp_models/crp-wt_formatted.txt -o crp-wt_ER_crp -s 3 -e 25
MPAthic learn_model -lm IM -i crp_models/full-wt_formatted.txt -o full-wt_MCMC_crp -s 3 -e 25
MPAthic learn_model -lm LS -i crp_models/full-wt_formatted.txt -o full-wt_LS_crp -s 3 -e 25
MPAthic learn_model -lm ER -i crp_models/full-wt_formatted.txt -o full-wt_ER_crp -s 3 -e 25
MPAthic learn_model -lm IM -i crp_models/full-500_formatted.txt -o full-500_MCMC_crp -s 3 -e 25
MPAthic learn_model -lm LS -i crp_models/full-500_formatted.txt -o full-500_LS_crp -s 3 -e 25
MPAthic learn_model -lm ER -i crp_models/full-500_formatted.txt -o full-500_ER_crp -s 3 -e 25
MPAthic learn_model -lm IM -i crp_models/full-150_formatted.txt -o full-150_MCMC_crp -s 3 -e 25
MPAthic learn_model -lm LS -i crp_models/full-150_formatted.txt -o full-150_LS_crp -s 3 -e 25
MPAthic learn_model -lm ER -i crp_models/full-150_formatted.txt -o full-150_ER_crp -s 3 -e 25
MPAthic learn_model -lm IM -i crp_models/full-0_formatted.txt -o full-0_MCMC_crp -s 3 -e 25
MPAthic learn_model -lm LS -i crp_models/full-0_formatted.txt -o full-0_LS_crp -s 3 -e 25
MPAthic learn_model -lm ER -i crp_models/full-0_formatted.txt -o full-0_ER_crp -s 3 -e 25

#learn CRP neighbor models
MPAthic learn_model -lm IM -i crp_models/crp-wt_formatted.txt -o crp-wt_MCMC_crp_NBR -s 3 -e 25 -mt NBR
MPAthic learn_model -lm IM -i crp_models/full-wt_formatted.txt -o full-wt_MCMC_crp_NBR -s 3 -e 25 -mt NBR
MPAthic learn_model -lm IM -i crp_models/full-500_formatted.txt -o full-500_MCMC_crp_NBR -s 3 -e 25 -mt NBR
MPAthic learn_model -lm IM -i crp_models/full-150_formatted.txt -o full-150_MCMC_crp_NBR -s 3 -e 25 -mt NBR
MPAthic learn_model -lm IM -i crp_models/full-0_formatted.txt -o full-0_MCMC_crp_NBR -s 3 -e 25 -mt NBR

#learn RNAP models
MPAthic learn_model -lm IM -i rnap_models/rnap-wt_formatted.txt -o rnap-wt_MCMC_rnap -s 37 -e 71
MPAthic learn_model -lm LS -i rnap_models/rnap-wt_formatted.txt -o rnap-wt_LS_rnap -s 37 -e 71
MPAthic learn_model -lm ER -i rnap_models/rnap-wt_formatted.txt -o rnap-wt_ER_rnap -s 37 -e 71
MPAthic learn_model -lm IM -i rnap_models/full-wt_formatted.txt -o full-wt_MCMC_rnap -s 37 -e 71
MPAthic learn_model -lm LS -i rnap_models/full-wt_formatted.txt -o full-wt_LS_rnap -s 37 -e 71
MPAthic learn_model -lm ER -i rnap_models/full-wt_formatted.txt -o full-wt_ER_rnap -s 37 -e 71
MPAthic learn_model -lm IM -i rnap_models/full-500_formatted.txt -o full-500_MCMC_rnap -s 37 -e 71
MPAthic learn_model -lm LS -i rnap_models/full-500_formatted.txt -o full-500_LS_rnap -s 37 -e 71
MPAthic learn_model -lm ER -i rnap_models/full-500_formatted.txt -o full-500_ER_rnap -s 37 -e 71
MPAthic learn_model -lm IM -i rnap_models/full-150_formatted.txt -o full-150_MCMC_rnap -s 37 -e 71
MPAthic learn_model -lm LS -i rnap_models/full-150_formatted.txt -o full-150_LS_rnap -s 37 -e 71
MPAthic learn_model -lm ER -i rnap_models/full-150_formatted.txt -o full-150_ER_rnap -s 37 -e 71
MPAthic learn_model -lm IM -i rnap_models/full-0_formatted.txt -o full-0_MCMC_rnap -s 37 -e 71
MPAthic learn_model -lm LS -i rnap_models/full-0_formatted.txt -o full-0_LS_rnap -s 37 -e 71
MPAthic learn_model -lm ER -i rnap_models/full-0_formatted.txt -o full-0_ER_rnap -s 37 -e 71

#learn RNAP neighbor models
MPAthic learn_model -lm IM -i rnap_models/crp-wt_formatted.txt -o crp-wt_MCMC_crp_NBR -s 37 -e 71 -mt NBR
MPAthic learn_model -lm IM -i rnap_models/full-wt_formatted.txt -o full-wt_MCMC_crp_NBR -s 37 -e 71 -mt NBR
MPAthic learn_model -lm IM -i rnap_models/full-500_formatted.txt -o full-500_MCMC_crp_NBR -s 37 -e 71 -mt NBR
MPAthic learn_model -lm IM -i rnap_models/full-150_formatted.txt -o full-150_MCMC_crp_NBR -s 37 -e 71 -mt NBR
MPAthic learn_model -lm IM -i rnap_models/full-0_formatted.txt -o full-0_MCMC_crp_NBR -s 37 -e 71 -mt NBR

#learn DMS models of the two data sets
MPAthic learn_model -lm IM -i dms/dms_1_formatted -o dms_1_MCMC
MPAthic learn_model -lm LS -i dms/dms_1_formatted -o dms_1_LS
MPAthic learn_model -lm ER -i dms/dms_1_formatted -o dms_1_ER
MPAthic learn_model -lm IM -i dms/dms_2_formatted -o dms_2_MCMC
MPAthic learn_model -lm LS -i dms/dms_2_formatted -o dms_2_LS
MPAthic learn_model -lm ER -i dms/dms_2_formatted -o dms_2_ER

#learn mpra models 
MPAthic learn_model -lm IM -i mpra/CRE_100uM_ds_formatted -o CRE_100uM_ds_MCMC
MPAthic learn_model -lm LS -i mpra/CRE_100uM_ds_formatted -o CRE_100uM_ds_LS
MPAthic learn_model -lm ER -i mpra/CRE_100uM_ds_formatted -o CRE_100uM_ds_ER
MPAthic learn_model -lm IM -i mpra/CRE_100uM_test_formatted -o CRE_100uM_test_MCMC
MPAthic learn_model -lm LS -i mpra/CRE_100uM_test_formatted -o CRE_100uM_test_LS
MPAthic learn_model -lm ER -i mpra/CRE_100uM_test_formatted -o CRE_100uM_test_ER

#learn mpra Neighbor models
MPAthic learn_model -lm IM -i mpra/CRE_100uM_ds_formatted -o CRE_100uM_ds_MCMC_NBR -mt NBR
MPAthic learn_model -lm IM -i mpra/CRE_100uM_test_formatted -o CRE_100uM_test_MCMC_NBR -mt NBR
'''calculate the predictive information'''

#CRP models predictive info
models = ['crp-wt_MCMC_crp','full-wt_MCMC_crp','full-500_MCMC_crp','full-150_MCMC_crp','full-0_MCMC_crp']
modeltype = ['_MCMC','_IM','_LS']
datasets = ['crp_models/crp-wt_formatted.txt','crp_models/full-wt_formatted.txt','crp_models/full-500_formatted.txt','crp_models/full-150_formatted.txt','crp_models/full-0_formatted.txt']
for i in models:
    for mt in modeltype:
        for z in datasets:
            outname = 'info_' + i + z 
            os.system('''MPAthic predictiveinfo -m %s -ds %s -o %s''' % (i + mt,z,'MI_' + i + mt + '_' + z))
        
#rnap models predictive info
models = ['dms_1','dms_2']
modeltype = ['_MCMC','_IM','_LS']
datasets = ['dms/dms_1_formatted.txt','dms/dms_2_formatted.txt']

for i in models:
    for mt in modeltype:
        for z in datasets:
            outname = 'info_' + i + z 
            os.system('''MPAthic predictiveinfo -m %s -ds %s -o %s''' % (i + mt,z,'MI_' + i + mt + '_' + z))  

#dms models predictive info

models = ['rnap-wt_MCMC_rnap','full-wt_MCMC_rnap','full-500_MCMC_rnap','full-150_MCMC_rnap','full-0_MCMC_rnap']
modeltype = ['_MCMC','_IM','_LS']
datasets = ['rnap_models/rnap-wt_formatted.txt','rnap_models/full-wt_formatted.txt','rnap_models/full-500_formatted.txt','rnap_models/full-150_formatted.txt','rnap_models/full-0_formatted.txt']

for i in models:
    for mt in modeltype:
        for z in datasets:
            outname = 'info_' + i + z 
            os.system('''MPAthic predictiveinfo -m %s -ds %s -o %s''' % (i + mt,z,'MI_' + i + mt + '_' + z))      


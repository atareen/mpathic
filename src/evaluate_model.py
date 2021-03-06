'''A script which adds a predicted energy column to an input table. This is
    generated based on a energy model the user provides.'''
from __future__ import division
'''
from mpathic.src import Models
from mpathic.src import utils
from mpathic.src.utils import ControlledError, handle_errors, check
from mpathic.src import qc
from mpathic.src import io_local as io
from mpathic.src import fast
'''
import Models as Models
import utils as utils
from utils import ControlledError, handle_errors, check
import qc as qc
import io_local as io
import fast

import pandas as pd

class EvaluateModel:

    """

    Parameters
    ----------

    dataset_df: (pandas dataframe)
        Input dataset data frame

    model_df: (pandas dataframe)
        Model dataframe

    left: (int)
        Seq position at which to align the left-side of the model. \n
        Defaults to position determined by model dataframe.

    right: (int)
        Seq position at which to align the right-side of the model. \n
        Defaults to position determined by model dataframe.

    """

    @handle_errors
    def __init__(self,
                 dataset_df,
                 model_df,
                 left=None,
                 right=None):

        # set attributes
        self.dataset_df = dataset_df
        self.model_df = model_df
        self.left = left
        self.right = right

        self.out_df = None

        # validate parameters
        self._input_checks()
        self.dataset_with_values = None

        seqtype, modeltype = qc.get_model_type(model_df)
        seqcol = qc.seqtype_to_seqcolname_dict[seqtype]

        # The following could be moved to input checks
        if not ((self.left is None) or (self.right is None)):
            raise ControlledError('Cannot set both left and right at same time.')

        if not (self.left is None):
            start = self.left
            end = start + model_df.shape[0] + (1 if modeltype == 'NBR' else 0)
        elif not (self.right is None):
            end = self.right
            start = end - model_df.shape[0] - (1 if modeltype == 'NBR' else 0)
        else:
            start = model_df['pos'].values[0]
            end = model_df['pos'].values[-1] + (2 if modeltype == 'NBR' else 1)

        #assert start < end
        check(start < end, "start = %d must be < end " % start)

        # Validate start and end positions
        seq_length = len(self.dataset_df[seqcol][0])
        if start < 0:
            raise ControlledError('Invalid start=%d' % start)
        if end > seq_length:
            raise ControlledError('Invalid end=%d for seq_length=%d' % (end, seq_length))

        # select target sequence region
        out_df = self.dataset_df.copy()
        out_df.loc[:, seqcol] = out_df.loc[:, seqcol].str.slice(start, end)

        # Create model object of correct type
        if modeltype == 'MAT':
            mymodel = Models.LinearModel(model_df)
        elif modeltype == 'NBR':
            mymodel = Models.NeighborModel(model_df)
        else:
            raise ControlledError('Unrecognized model type %s' % modeltype)

        # Compute values
        out_df['val'] = mymodel.evaluate(out_df)

        # Validate dataframe and return
        self.dataset_with_values = qc.validate_dataset(out_df, fix=True)
        self.out_df = qc.validate_dataset(out_df, fix=True)

    def _input_checks(self):

        # dataset_df validation
        if self.dataset_df is None:
            raise ControlledError(
                " The Evaluate Model class requires pandas dataframe as input dataframe. Entered dataset_df was 'None'.")

        elif self.dataset_df is not None:
            check(isinstance(self.dataset_df, pd.DataFrame),
                  'type(dataset_df) = %s; must be a pandas dataframe ' % type(self.dataset_df))

        # validate dataset
        check(pd.DataFrame.equals(self.dataset_df, qc.validate_dataset(self.dataset_df)),
              " Input dataframe failed quality control, \
              please ensure input dataset has the correct format of an mpathic dataframe ")

        # model validation
        if self.model_df is None:
            raise ControlledError(
                " The Evaluate Model class requires pandas dataframe as input model dataframe. Entered model_df was 'None'.")

        elif self.model_df is not None:
            check(isinstance(self.model_df, pd.DataFrame),
                  'type(model_df) = %s; must be a pandas dataframe ' % type(self.model_df))

        # validate dataset
        check(pd.DataFrame.equals(self.model_df, qc.validate_model(self.model_df)),
              " Model dataframe failed quality control, \
                                please ensure input model dataframe has the correct format of an mpathic dataframe ")

        # check that left is an integer
        check(isinstance(self.left, int),
              'type(left) = %s; must be of type int ' % type(self.left))

        # check that right is an integer
        check(isinstance(self.right, int),
              'type(right) = %s; must be of type int ' % type(self.right))

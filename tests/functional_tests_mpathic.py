from __future__ import print_function   # so that print behaves like python 3.x not a special lambda statement
import mpathic as mpa
import numpy as np

global_success_counter = 0
global_fail_counter = 0

# Common success and fail lists
bool_fail_list = [0, -1, 'True', 'x', 1]
bool_success_list = [False, True]

# helper method for functional test_for_mistake
def test_for_mistake(func, *args, **kw):
    """
    Run a function with the specified parameters and register whether
    success or failure was a mistake

    parameters
    ----------

    func: (function or class constructor)
        An executable function to which *args and **kwargs are passed.

    return
    ------

    None.
    """

    global global_fail_counter
    global global_success_counter

    # print test number
    test_num = global_fail_counter + global_success_counter
    print('Test # %d: ' % test_num, end='')
    #print('Test # %d: ' % test_num)

    # Run function
    obj = func(*args, **kw)
    # Increment appropriate counter
    if obj.mistake:
        global_fail_counter += 1
    else:
        global_success_counter += 1


def test_parameter_values(func,
                          var_name=None,
                          fail_list=[],
                          success_list=[],
                          **kwargs):
    """
    Tests predictable success & failure of different values for a
    specified parameter when passed to a specified function

    parameters
    ----------

    func: (function)
        Executable to test. Can be function or class constructor.

    var_name: (str)
        Name of variable to test. If not specified, function is
        tested for success in the absence of any passed parameters.

    fail_list: (list)
        List of values for specified variable that should fail

    success_list: (list)
        List of values for specified variable that should succeed

    **kwargs:
        Other keyword variables to pass onto func.

    return
    ------

    None.

    """

    # If variable name is specified, test each value in fail_list
    # and success_list
    if var_name is not None:

        # User feedback
        print("Testing %s() parameter %s ..." % (func.__name__, var_name))

        # Test parameter values that should fail
        for x in fail_list:
            kwargs[var_name] = x
            test_for_mistake(func=func, should_fail=True, **kwargs)

        # Test parameter values that should succeed
        for x in success_list:
            kwargs[var_name] = x
            test_for_mistake(func=func, should_fail=False, **kwargs)

        print("Tests passed: %d. Tests failed: %d.\n" %
              (global_success_counter, global_fail_counter))

    # Otherwise, make sure function without parameters succeeds
    else:

        # User feedback
        print("Testing %s() without parameters." % func.__name__)

        # Test function
        test_for_mistake(func=func, should_fail=False, **kwargs)


def test_simulate_library():

    # test default parameters
    test_parameter_values(func=mpa.simulate_library_class)

    # test wtseq
    test_parameter_values(func=mpa.simulate_library_class, var_name='wtseq', fail_list=[3, 1.0,"XxX",False,""],
                          success_list=["ATTCCGAGTA", "ATGTGTAGTCGTAG"])
    # test mutation rate
    test_parameter_values(func=mpa.simulate_library_class,var_name='mutrate',fail_list=[1.1,2,-1,0],success_list=[0.5,0.1])

    # test numseq
    test_parameter_values(func=mpa.simulate_library_class,var_name='numseq',fail_list=['x',-1,0,0.5],success_list=[1,2,3,100])

    # test dicttype
    #test_parameter_values(func=mpa.simulate_library_class(wtseq=wtseq_dna),var_name='dicttype',fail_list=['x',1,True],success_list=['dna','rna','protein'])
    test_parameter_values(func=mpa.simulate_library_class, var_name='dicttype',
                          fail_list=['x', 1, True], success_list=['dna','rna','protein'])

    # Note *** Need valid example of probarr to test ***
    # test probarr
    test_parameter_values(func=mpa.simulate_library_class,var_name='probarr',fail_list=[1,1.0,"x",[1,2,3]],success_list=[None])

    # tags
    test_parameter_values(func=mpa.simulate_library_class,var_name='tags',fail_list=[None,-1,3.9],success_list=[True,False])

    # tag_length
    test_parameter_values(func=mpa.simulate_library_class, var_name='tag_length', fail_list=[None, -1, 3.9],
                          success_list=[3, 200])


def test_mpathic_io():

    bad_file_arg_example_1 = "../../mpathic/MPAthic_tests/input/dataset_bad_badseqs.txt"
    bad_file_arg_example_2 = "../../mpathic/MPAthic_tests/input/dataset_bad_badcounts.txt"

    good_file_arg_example_1 =  "../../mpathic/MPAthic_tests/input/dataset_crp.txt"


    # test parameter file args
    test_parameter_values(func=mpa.io.load_dataset,var_name='file_arg',fail_list=[bad_file_arg_example_1,bad_file_arg_example_2],success_list=[good_file_arg_example_1])


#test_simulate_library()
test_mpathic_io()
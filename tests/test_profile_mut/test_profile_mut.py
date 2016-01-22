#!/usr/bin/env python
import unittest
import sst.io as io
import sst.qc as qc
import sst.profile_mut as profile_mut
import glob

class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_profile_mut_total_err(self):
        """ Test the ability of sst.profile_mut to compute mutation rates based on total count values
        """

        print '\nIn test_profile_mut_total_err...'
        library_files = glob.glob('library_*.txt')
        library_files += glob.glob('dataset_*.txt')
        for file_name in library_files:
            print '\t%s ='%file_name,
            description = file_name.split('_')[-1].split('.')[0]
            executable = lambda: profile_mut.main(io.load_dataset(file_name),err=True)

            # If good, then profile_mut.main should produce a valid df
            if '_good' in file_name:
                try:
                    df = executable()
                    qc.validate_profile_mut(df)
                    out_file = 'profile_mut_total_err_%s.txt'%description
                    io.write(df,out_file)
                    io.load_profile_mut(out_file)
                    print 'good.'
                except:
                    print 'bad (ERROR).'
                    raise

            # If bad, then profile_mut.main should raise TypeError
            elif '_bad' in file_name:
                try:
                    self.assertRaises(TypeError,executable)
                    print 'badtype.'
                except:
                    print 'good (ERROR).'
                    raise

            # There are no other options
            else:
                raise TypeError('Unrecognized class of file_name.')


    def test_profile_mut_bin_noerr(self):
        """ Test the ability of sst.profile_mut to compute mutation rates
        """

        print '\nIn test_profile_mut_bin_noerr_...'
        library_files = glob.glob('library_*.txt')
        library_files += glob.glob('dataset_*.txt')
        good_bin_num = 2
        bad_bin_num = 5
        for file_name in library_files:
            print '\t%s ='%file_name,
            description = file_name.split('_')[-1].split('.')[0]
            executable = lambda:\
                profile_mut.main(io.load_dataset(file_name),bin=good_bin_num,err=False)
            print '(bin=%d)'%good_bin_num,

            # If bad or library, then profile_mut.main should raise TypeError
            if ('_bad' in file_name) or ('library' in file_name):
                try:
                    self.assertRaises(TypeError,executable)
                    print 'badtype,',
                except:
                    print 'good (ERROR).'
                    raise

            # If good, then profile_mut.main should produce a valid df
            elif ('_good' in file_name) or ('dataset' in file_name):
                try:
                    df = executable()
                    qc.validate_profile_mut(df)
                    out_file = 'profile_mut_bin_noerr_%s.txt'%description
                    io.write(df,out_file)           # Test writing
                    io.load_profile_mut(out_file)   # Test loading
                    print 'good,',

                except:
                    print 'bad (ERROR).'
                    raise

            # There are no other options
            else:
                raise TypeError('Unrecognized class of file_name.')

            # Should always raise an error if bin num is too large
            executable = lambda:\
                profile_mut.main(io.load_dataset(file_name),bin=bad_bin_num)
            print '(bin=%d)'%bad_bin_num,
            try:
                self.assertRaises(TypeError,executable)
                print 'badtype.'
            except:
                print 'good (ERROR).'
                raise


    def test_profile_mut_seqslicing(self):
        """ Test the ability of sst.profile_mut to slice sequences properly, and to raise the correct errors
        """

        print '\nIn test_profile_mut_seqslicing...'
        library_files = glob.glob('library_*.txt')
        library_files += glob.glob('dataset_*.txt')
        for file_name in library_files:
            print '\t%s ='%file_name,
            description = file_name.split('_')[-1].split('.')[0]
            executable_good1 =\
                lambda: profile_mut.main(io.load_dataset(file_name),\
                    start=2,end=10)
            executable_good2 =\
                lambda: profile_mut.main(io.load_dataset(file_name),\
                    end=10)
            executable_good3 =\
                lambda: profile_mut.main(io.load_dataset(file_name),\
                    end=2)
            executable_nopro =\
                lambda: profile_mut.main(io.load_dataset(file_name),\
                    start=50,end=60)
            executable_bad1 =\
                lambda: profile_mut.main(io.load_dataset(file_name),\
                    start=-1)
            executable_bad2 =\
                lambda: profile_mut.main(io.load_dataset(file_name),\
                    end=100)
            executable_bad3 =\
                lambda: profile_mut.main(io.load_dataset(file_name),\
                    start=20,end=10)

            # If good, then sequences will be valid
            if 'good' in file_name:
                try:
                    df = executable_good1()
                    io.write(df,'profile_mut_splice2-10_%s.txt'%description)
                    executable_good2()
                    executable_good3()
                    self.assertRaises(TypeError,executable_bad1)
                    self.assertRaises(TypeError,executable_bad2)
                    self.assertRaises(TypeError,executable_bad3)
                    if '_pro' in file_name:
                        self.assertRaises(TypeError,executable_nopro)
                    else:
                        df = executable_nopro()
                    print 'ok.'
                except:
                    print 'ok (ERROR).'
                    raise

            # If bad, then profile_mut.main should raise TypeError
            elif '_bad' in file_name:
                try:
                    self.assertRaises(TypeError,executable_good1)
                    self.assertRaises(TypeError,executable_good2)
                    self.assertRaises(TypeError,executable_good3)
                    self.assertRaises(TypeError,executable_nopro)
                    self.assertRaises(TypeError,executable_bad1)
                    self.assertRaises(TypeError,executable_bad2)
                    self.assertRaises(TypeError,executable_bad3)
                    print 'ok.'
                except:
                    print 'not ok (ERROR).'
                    raise

            # There are no other options
            else:
                raise TypeError('Unrecognized class of file_name.')


if __name__ == '__main__':
    unittest.main()
		
			

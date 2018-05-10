MPAthic: Massively Parallel Assays 
==================================
*Quantitative modeling of sequence-function relationships for massively parallel assays*

Written by Ammar Tareen, William T. Ireland, and [Justin B. Kinney][kinneylab]   
Current version: 0.01.01  

Citation:  
Ireland WT, Kinney JB (2016) *MPAthic: quantitative modeling of sequence-function relationships for massively parallel assays.* bioRxiv doi:10.1101/054676

Please address questions or problems regarding this software to [Justin B. Kinney][kinneylab] at jkinney@cshl.edu.

## Overview

MPAthic is a software package for analyzing data from a variety massively parallel assays, including Sort-Seq assays, Massively Parallel Reporter assays, and Deep Mutational Scanning assays. MPAthic is a python API. Usage and details can be found in [documentation][documentation]. The accompanying preprint can be found here: [accompanying preprint][preprint].

## Requriements

MPAthic is written in Python 2.9.7. It has been verified to work on Linux and Mac OS X. Installation currently requires a number of other Python packages:

* Babel==2.5.3
* backports.functools-lru-cache==1.5
* biopython==1.71
* certifi==2018.4.16
* chardet==3.0.4
* cvxopt==1.1.9
* cycler==0.10.0
* Cython==0.28.1
* docutils==0.14
* idna==2.6
* imagesize==1.0.0
* kiwisolver==1.0.1
* MarkupSafe==1.0
* matplotlib==2.2.2
* mpmath==1.0.0
* numpy==1.14.2
* packaging==17.1
* pandas==0.22.0
* Pygments==2.2.0
* pymc==2.3.6
* pyparsing==2.2.0
* python-dateutil==2.7.2
* pytz==2018.4
* requests==2.18.4
* scikit-learn==0.19.1
* scipy==1.0.1
* six==1.11.0
* sklearn==0.0
* snowballstemmer==1.2.1
* subprocess32==3.2.7
* typing==3.6.4
* urllib3==1.22
* weblogo==3.6.0


## Installation

MPAthic can be installed from PyPI by executing

```
pip install mpathic
```

After installation, test the functionality of all methods by running

```python
import mpathic 
mpathic.demo()
```

<!--

## Documentation

The commands used to perform the analysis in Ireland & Kinney (2016) are described in [analysis.md](analysis.md). Documentation on each of the MPAthic functions is provided [here][documentation].

## Quick start guide

Below are the commands described in the "Overview" section of the [Supplemental Information of Ireland and Kinney (2016)](http://biorxiv.org/content/early/2016/05/21/054676.figures-only). These commands provide a quick entry into the capabilities of MPAthic. To execute them, first change to the [examples](examples/) directory, which contains the necessary inpupt files [true_model.txt](examples/true_model.txt) and [genome_ecoli.fa](examples/genome_ecoli.fa). 

#### Simulating data

Simualte a library of binding sites for the CRP transcription factor:
```
mpathic simulate_library -w TAATGTGAGTTAGCTCACTCAT -n 100000 -m 0.24 -o library.txt
```

Simulate a Sort-Seq experiment using a model ([true_model.txt](examples/true_model.txt)) of CRP-DNA affinity:
```
mpathic simulate_sort -m true_model.txt -n 4 -i library.txt -o dataset.txt
```

#### Computing summary statistics

Compute a mutation profile of the simluated library:
```
mpathic profile_mut -i library.txt -o mutprofile.txt
```

Compute the occurance frequency of each base at each position in the library:
```
mpathic profile_freq -i library.txt -o freqprofile.txt
```

Compute an information profile (a.k.a information footprint) from the simulated data:
```
mpathic profile_info --err -i dataset.txt -o infoprofile.txt
```

#### Inferring quantitative models

Infer a matrix model for CRP from the simulated data:
```
mpathic learn_model -lm LS -mt MAT -i dataset.txt -o matrix_model.txt
```

Infer a neighbor model for CRP from the simulated data:
```
mpathic learn_model -lm LS -mt NBR -i dataset.txt -o neighbor_model.txt
```

#### Evaluating models

Evaluate the inferred matrix model on all sites in the dataset:
```
mpathic evaluate_model -m matrix_model.txt -i dataset.txt -o dataset_with_values.txt
```

Scan the *Escherichia coli* genome ([genome_ecoli.fa](examples/genome_ecoli.fa)) using the inferred matrix model:
```
mpathic scan_model -n 100 -m matrix_model.txt -i genome_ecoli.fa -o genome_sites.txt
```

Compute the predictive information of the inferred matrix model and the true model on the simulated data:
```
mpathic predictiveinfo -m matrix_model.txt -ds dataset.txt
mpathic predictiveinfo -m true_model.txt -ds dataset.txt
```

-->


[documentation]: http://mpathic.readthedocs.io/en/latest/
[github]: https://github.com/atareen/mpathic
[preprint]: http://biorxiv.org/content/early/2016/05/21/054676
[kinneylab]: http://kinneylab.labsites.cshl.edu/



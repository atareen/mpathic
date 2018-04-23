========
Model
========

We being by loading NumPy, PyPlot, SUFTware::

    import numpy as np
    import matplotlib.pyplot as plt
    import suftware as sw

    # Enable interactive plotting
    plt.ion()


Next we simulate data from a Gamma distribution::

    # Generate data from a Gamma distribution
    np.random.seed(0)
    data = np.random.gamma(shape=5, scale=1, size=100)
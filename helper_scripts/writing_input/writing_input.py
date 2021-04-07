import numpy as np
def write_input(small_ions, small_lattice):
    init_ions = np.loadtxt(small_ions, usecols=[2, 3, 4, 5])
    init_lattice = np.loadtxt(small_lattice)

    


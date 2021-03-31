import numpy as np
def read_momenta(filename, bandnum):
	print(np.fromfile(filename).reshape(1, bandnum, bandnum, 3))


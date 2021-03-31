import numpy as np
def rpcompare(Efile, pfile, nbands, band1, band2):
	#data = np.loadtxt(filename, skiprows=6)

	strengths = np.array([])

	data = np.loadtxt(Efile, skiprows=6)
	num_excitations = np.shape(data)[0]
	print("Number of excitations is: ", num_excitations)

	excitation_index = -1
	for i in range(num_excitations):
		if (data[:, 1][i]==band1 and data[:, 2][i]==band2):
			excitation_index = i
	if (excitation_index==-1):
		print("No such excitation")
		#Exception("The excitation you were looking for does not exist")

	pdata = np.fromfile(pfile, dtype = complex).reshape(1, 3, nbands, nbands).swapaxes(2, 3)
	pdata_short = np.zeros((nbands, nbands))
	for b in range(nbands):
		for c in range(nbands):
			pdata_short[b, c] = np.abs(pdata[0, 0, b, c])**2+ np.abs(pdata[0, 1, b, c])**2+ np.abs(pdata[0, 2, b, c])**2

	##The R^2 matrix element

	print("The index of the proposed excitaiton is: ", excitation_index)
	print("R^2 matrix element from DFT: ", data[excitation_index, 6])

	print("band1: ", data[excitation_index, 1], "   band2:    ", data[excitation_index, 2], "    transition_energy:   ", data[excitation_index, 3])

	print("R^2 matrix element from p transformation from DFT:  ", pdata_short[band1, band2]/((data[excitation_index, 3])**2))


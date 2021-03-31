import matplotlib.pyplot as plt
import numpy as np
def oscillator_strength(filename):
	data = np.loadtxt(filename, skiprows=6)
	fig, ax = plt.subplots()
	ax.plot(data[:, 3]*27.2, 2/3*data[:, 3]*data[:, 6])
	ax.set_xlabel('Transition Energy (eV)')
	ax.set_ylabel('Oscillator Strength')
	plt.show()
	print("Check oscillator strength sum rule: ", np.sum(2/3*data[:, 3]*data[:, 6]))


def oscillator_strength_convergence(filenames):
	strengths = np.array([])
	for file in filenames:
		data = np.loadtxt(file, skiprows=6)
		print(np.sum(2/3*data[:, 3]*data[:, 6]))
		strengths = np.append(strengths, np.sum(2/3*data[:, 3]*data[:, 6]))
	
	print(strengths)
	print(np.diff(strengths))
	fig, (ax1, ax2) = plt.subplots(ncols=2)
	ax1.plot(strengths)
	#ax.plot(data[:, 3]*27.2, 2/3*data[:, 3]*data[:, 6])
	ax2.plot(np.diff(strengths))
	ax1.set_xlabel('Iteration (Increasing Empty Band Numbers)')
	ax1.set_ylabel('Oscillator Strength Sum')
	ax2.set_xlabel('Iteration')
	ax2.set_ylabel('Diff of Oscillator Strength Sum')
	plt.show()


def oscillator_strength_convergence2(filename):
	data = np.loadtxt(filename, skiprows=6)
	strengths = np.array([])
	num_excitations = np.shape(data)[0]
	print("Number of possible excitations is: ", num_excitations)
	for i in range(num_excitations):
		strengths = np.append(strengths, np.sum(2/3*data[0:i, 3]*data[0:i, 6]))

	return strengths

def oscillator_strengths_momentum(efilename, pfilename, nbands, starting_band=1, sumband1=1, sumband2=2):
	
	energies = np.fromfile(efilename)
	data = np.fromfile(pfilename, dtype = complex).reshape(1, 3, nbands, nbands).swapaxes(2, 3)
	#data_short = np.sum(np.abs(data[0, ...])**2, axis = 0 )
	data_short = np.zeros((nbands, nbands))
	for b in range(0, nbands):
		for c in range(0, nbands):
			data_short[b, c] = np.abs(data[0, 0, b, c])**2+ np.abs(data[0, 1, b, c])**2+ np.abs(data[0, 2, b, c])**2 

	#print(data_short)
	starting_band_p = data_short[starting_band, :]
	
	f=0	
	for i in range(sumband1, sumband2):
		if (i != starting_band):
			f = f + 2/3*starting_band_p[i]/(energies[i]-energies[starting_band])
	#print("Oscillator Strength is: ", f)
	#print(starting_band_p)		
	#return starting_band_p
	return f


def oscillator_strengths_momentum_convergence(efilename, pfilename, nbands, starting_band=1):
	energies = np.fromfile(efilename)
	data = np.fromfile(pfilename, dtype = complex).reshape(1, 3, nbands, nbands).swapaxes(2, 3)
        #data_short = np.sum(np.abs(data[0, ...])**2, axis = 0 )
	data_short = np.zeros((nbands, nbands))
	for b in range(0, nbands):
		for c in range(0, nbands):
			data_short[b, c] = np.abs(data[0, 0, b, c])**2+ np.abs(data[0, 1, b, c])**2+ np.abs(data[0, 2, b, c])**2

        #print(data_short)
	starting_band_p = data_short[starting_band, :]

	fs = np.zeros(nbands)
	for sumband2 in range(nbands):
		f=0
		for i in range(1, sumband2):
			if (i != starting_band):
				f = f + 2/3*starting_band_p[i]/(energies[i]-energies[starting_band])
		fs[sumband2] = f
	#print("Oscillator Strength is: ", f)
	#print(starting_band_p)
	#return starting_band_p
	return fs






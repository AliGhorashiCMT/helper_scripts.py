import matplotlib.pyplot as plt
import numpy as np
def oscillator_strength(filename):
	data = np.loadtxt(filename, skiprows=6)
	fig, ax = plt.subplots()
	ax.plot(data[:, 3]*27.2, 2/3*data[:, 3]*data[:, 6])
	ax.set_xlabel('Transition Energy (eV)')
	ax.set_ylabel('Oscillator Strength')
	plt.show()

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

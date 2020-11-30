#This code creates random numbers using "random" function of python "NumPy" module. The structure of random number can be set as is required. Here we will generate "uniform" random numbers (which have uniform distribution)and "normal" random numbers (which have normal or Gaussian distribution).
#We also use "Matplotlib" module to plot histograms

import numpy
import matplotlib.pyplot as plt

#Now let's generate 100000 random (uniform) data points (floats) between 0.0 and 5.0
x = numpy.random.uniform(0.0,5.0,100000)

#Now let's plot a histogram
plt.hist(x,100)#it plots histogram with 100 bars (bins)
plt.title('Uniform distribution')
plt.xlabel('x')
plt.ylabel('Entries')
plt.show()

#Generate 100000 random (normal or Gaussian distributed) data points (floats) with mean 5.0 and SD 1.0
y = numpy.random.normal(5.0,1.0,100000)
plt.hist(y,100,histtype='step')#histtype is used to change histogram type between 'bar', 'barstacked', 'step', 'stepfilled'.
plt.title('Gaussian (Normal) distribution')
plt.xlabel('data')
plt.ylabel('Entries')
plt.show()

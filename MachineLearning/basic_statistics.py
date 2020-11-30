#This code gives some examples of how to calulate basic statistical quantities like, mean, median, mode, standard deviation, variance, and percentile.
#It mostly uses python module "NumPy" but mode uses "SciPy"

import numpy #for mean, median, sd, variance, and percentile
from scipy import stats #for mode

#consider an array of data

x = [10,12,9,8,11,10,15,17,19,20,15,14,22,21,12,11,15]

#calculate mean
Mean = numpy.mean(x)
print('Mean of the given distribution is: ', Mean)

#calculate median
Median = numpy.median(x)
print('Median of the given distribution is: ', Median)

#calculate mode
Mode = stats.mode(x)
print('Mode of the given distribution is: ', Mode)#It returns the most probable data point and it's number of occurance

#calculate standard deviation
SD = numpy.std(x)
print('Standard deviation of the given distributin is: ', SD)

#calculate variance
Var = numpy.var(x)
print('Variance of the given distribution is: ', Var)

#calculate percentile
Per = numpy.percentile(x,70)
print('70th percentile of the given data is: ', Per)

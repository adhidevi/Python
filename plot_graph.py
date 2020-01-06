import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

infile = pd.read_csv('summary.txt', sep = '\t')
my_columns = infile.iloc[:,[1,6]]
print(my_columns)
my_X = infile.iloc[:,1]
my_Y = infile.iloc[:,6]
yerr = infile.iloc[:,7]
print(my_X, my_Y, yerr)
plt.grid()#activate or deactivate grid before plotting#
#plt.semilogy()#activate or deactivate axis log scale before plotting#
plt.errorbar(my_X, my_Y, yerr=yerr, fmt = 'bo', label = 'Various PreAmp', errorevery = 1)
plt.xlabel('HV')
plt.ylabel('nonLin')
plt.title('nonLin VS HV')
plt.legend()
plt.show()
plt.savefig('./plots/plot_graph.png')

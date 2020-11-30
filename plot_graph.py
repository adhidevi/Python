import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

infile = pd.read_csv('summary.txt', sep = '\t')
my_columns = infile.iloc[:,[1,6]]
print(my_columns)
my_X = infile.iloc[:,1]
my_Y = infile.iloc[:,6]
plt.grid()#activate or deactivate grid before plotting#
#plt.semilogy()#activate or deactivate axis log scale before plotting#
plt.plot(my_X, my_Y, 'bo', label = 'Various PreAmp')
plt.xlabel('HV')
plt.ylabel('nonLin')
plt.title('nonLin VS HV')
plt.legend()
plt.savefig('../plots/plot_graph.pdf')
plt.show()

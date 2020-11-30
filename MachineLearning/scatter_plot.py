#This is a simple function to make a scatter plot
import numpy#for random numbers
import matplotlib.pyplot as plt#for plotting
#It needs two arrays of the same size
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
print('Size of array x is: ',len(x))
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
print('Size of array y is: ',len(y))
plt.scatter(x,y,color='r',marker='*')
plt.title('A simple scatter plot')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()

#Let's create our data set using random number generator
x_value = numpy.random.normal(3.0,1.0,100000)#Mean = 3.0, SD = 1.0, entries = 100000
y_value = numpy.random.normal(6.0,2.0,100000)
plt.scatter(x_value,y_value,marker='D',color='b',s=1)
plt.title('Scatter plot using random numbers')
plt.xlabel('x_value')
plt.ylabel('y_value')
plt.show()

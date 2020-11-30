#This is a script to perform linear regression for a given data set
#Regression is used to find the relationship between variables
#In Machine Learning, and in statistical modeling, that relationship is used to make prediction of the future outcome
#In linear regression we draw a straight line through a given set of data-points. The straight line defines the relationship between the variables and can be used to predict future values.

from scipy import stats
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
print('x has '+str(len(x))+' data points')
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
print('y has '+str(len(x))+' data points')
plt.scatter(x,y)#plot scatter plot between y and x

#define some variables needed for regression line
slope, intercept, r, p, std_err = stats.linregress(x,y)
def f(x):#Define a function that uses the slope and intercept values to return a new value. The new value represents where on the y-axis the corresponding x value will be placed.
    return slope*x+intercept
mymodel=list(map(f,x))
plt.plot(x,mymodel)

plt.show()

#It is important to know how the relationship between the values of the x-axis and the values of the y-axis is, if there are no relationship the linear regression can not be used to predict anything.
#The relationship - the coefficient of correlation - is called "r".
#The "r" value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.
#When feeded the values of x and y correctly, "SciPy" module computes the value of "r".
#To get the coefficient simply do "print(r)".

print('The correlation coefficient is: ',r)
print(slope)

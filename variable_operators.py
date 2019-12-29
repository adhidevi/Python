a = 3
b = 4
add = a+b
print('The sum of a and b is: ', add)
sub = a-b
print('The difference of a and b is: ', sub)
times = a*b
print('The product of a and b is: ', times)
divide = a/b
print('a divide by b is: ', divide)
reminder = b%a
print('reminder of b divide by a is: ', reminder)
power = a**b
print('a power b is: ', power)
gt = a>b
print('a is greater than b: ', gt)
if(gt):
	print('a greater than b is True')
else:
	print('a greater than b is False')
lt = a<b
print('a is less than b: ', lt)
if(lt):
	print('a less than b is True')
else:
	print('a less than b is False')
#let's define some new variables
c = 'cool'
d = 3
e = True
print('a == d or c and e is: ', (a == d and d == c) or e)

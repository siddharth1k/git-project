#Solve the equation ax^2+bx+c=0
# X= (-b+/-sqrt(b^2-4ac))/2a
import cmath
a = float(input('Enter the value for a:'))
b = float(input('Enter the value for b:'))
c = float(input('Enter the value for c:'))

d= (b**2-4*a*c)/2*a
x= -b+cmath.sqrt(d)
y=  b+cmath.sqrt(d)

print('the solution the two values is {0} and {1}'.format(x,y))


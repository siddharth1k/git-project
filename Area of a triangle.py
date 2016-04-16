# Area of a triangle
# formula for area of a triangle = herons formula
# s=(a+b+c)/2
# Area= Sqauare root of s(s-a)(s-b)(s-c)




a = float(input('Enter the length of the first side:'))
b = float(input('Enter the length of the second side:'))
c = float(input('Enter the length of the third side:'))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

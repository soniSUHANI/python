a = int(input("enter first side of triangle: "))
b = int(input("enter second side of triangle: "))
c = int(input("enter third side of triangle : "))
s = (a +b +c)/2
ar = (s*(s-a)*(s-b)*(s-c))**(0.5)
print("the area of the triangle is: ",ar)

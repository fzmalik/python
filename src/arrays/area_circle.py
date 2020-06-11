def circle(r):
	a = 3.14*r*r
	return a
	
R = input("Enter the radius of circle : ")
R = int(R)
c = circle(R)
print("Area of circle : ",c)
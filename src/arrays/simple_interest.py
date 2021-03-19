def si(p,r,t):
	si = (p*r*t)/100
	return si
	
principle = input("enter the principle amount ")
rate = input("enter the  rate in %")	
time = input("enter the time in years")
principle = int(principle)
rate = int(rate)
time = int(time)
s = si(principle,rate,time)
print("simple intrest ",s)
def CI(x,y,z):
	ci = x*(pow((1+y/100),z))
	return ci

p = input("principle amount ")
r = input("rate in %")
t = input("time in year ")
p = int(p)
r = int(r)
t = int(t)
cpi = CI(p,r,t)
print("compound intrest :",cpi)
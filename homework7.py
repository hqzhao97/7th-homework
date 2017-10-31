import pylab as pl 
import math
timestep=0.0001
x0=1
y0=0
z0=0
time=0
r=25
b=8/3
sig=10

X=[]
Y=[]
Z=[]
totaltime=[]

X.append(x0)
Y.append(y0)
Z.append(z0)
totaltime.append(time)

x=x0
y=y0
z=z0
xx=x
yy=y
zz=z

while time<100:
	xx=x
	yy=y
	zz=z
	x=xx+sig*(yy-xx)*timestep
	y=yy+(-xx*zz+r*xx-yy)*timestep
	z=zz+(xx*yy-b*zz)*timestep
	time+=timestep
	X.append(x)
	Y.append(y)
	Z.append(z)
	totaltime.append(time)
pl.plot(X,Z)
pl.xlabel('x')
pl.ylabel('z')
pl.show
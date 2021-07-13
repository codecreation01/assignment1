#area of circle

from math import pi
radius=float(input("enter the radius"))
area=pi*radius*radius
print("area of the circle is:"+area)

#file extension

fn=input("enter the file name")
f=fn.split(".")
print("extension of the file is:"+f[-1])

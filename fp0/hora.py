tempo=float(input("Introduza um tempo em segundo:"))
h1= tempo/3600
h=int(h1)
a=h1-h
m1=a*60
m=int(m1)
b=m1-m
s1=b*60
s=int(s1)
print("{:02d}:{:02d}:{:02d}".format(h, m, s))

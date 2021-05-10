class Students:

    school="ellll"
    def __init__(self , m1 ,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m3+self.m2)/3





s1=Students(23,78,89)
s2=Students(56,89,90)

print(s2.avg())
print(s1.avg())


if s1.avg() > s2.avg():
    print("s1 is topper")
else:
   print ("s2 is topper")

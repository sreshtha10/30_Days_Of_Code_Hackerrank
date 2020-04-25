class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
    def computeDifference(self):
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                c = abs(a[i]-a[j])
                if c >self.maximumDifference:
                    self.maximumDifference = c
    


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

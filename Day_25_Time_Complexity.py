t = int(input())
while(t>0):
    prime  = True
    n = int(input())
    for i in range(2,int(pow(n,0.5))+1):
        if(n%i == 0):
            prime = False
    if(n == 1):
        prime = False
    if(prime == True):
        print("Prime")
    else:
        print("Not prime")
    t -= 1

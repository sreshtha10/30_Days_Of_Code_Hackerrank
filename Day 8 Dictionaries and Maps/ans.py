data = dict()
n = int(input())
for i in range(0,n):
    x = input().split()
    data[x[0]] = x[1]
search = []
i = 0
while i<n:
    y = input()
    search.append(y)
    if search[i] in data:
        print(search[i]+'='+data[search[i]])
    else:
        print('Not found')
    i+=1

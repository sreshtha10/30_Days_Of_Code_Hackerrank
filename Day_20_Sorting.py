n = int(input())
a = list(map(int, input().split()))
swaps = 0
t = 0
while t < n:
    for i in range(1,n):
        if a[i-1] > a[i]:
            swaps += 1
            temp = a[i-1]
            a[i-1] = a[i]
            a[i] = temp
        else:
            continue
    t += 1
print('Array is sorted in '+str(swaps)+' swaps.')
print('First Element: '+str(a[0]))
print('Last Element: '+str(a[n-1]))

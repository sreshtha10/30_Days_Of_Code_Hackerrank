import re
n = int(input())
details = []
emails = []
while n >0:
    detail = input().split()
    email = detail[1]
    emails.append(email)
    details.append(detail)
    n -= 1
for i in range(len(details)-1):
    for i in range(len(details)-1):
        if details[i][0] > details[i+1][0]:
            temp = details[i]
            details[i] = details[i+1]
            details[i+1] = temp
for i in range(len(details)):
    match = re.search(r'\w*@gmail.com',details[i][1])
    if match:
        print(details[i][0])


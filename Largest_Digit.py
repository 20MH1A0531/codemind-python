n=int(input())
s=0
while n>0:
    r=n%10
    if s<r:
        s=r
    n=n//10
print(s)

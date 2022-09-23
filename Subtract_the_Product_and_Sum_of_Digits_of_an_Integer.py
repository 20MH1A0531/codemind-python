n=int(input())
s=0
m=1
while n>0:
    r1=n%10
    s+=r1
    m*=r1
    n=n//10
print(m-s)
    
def pfs(n):
    fs=0
    for i in range(1,n):
        if n%i==0:
            fs+=i
    return fs
a=int(input())
b=int(input())
if pfs(b)==a and pfs(a)==b:
    print('Amicable')
else:
    print('Not Amicable')
    
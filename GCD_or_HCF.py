n1,n2=map(int,input().split())
while(n2!=0):
    if(n2>=n1):
        n2=n2%n1
    else:
        n1,n2=n2,n1
print(n1)
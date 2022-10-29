def is_happy(n):
    rem = sum = 0
    while(n > 0):    
        rem = n%10    
        sum = sum + (rem*rem)   
        n = n//10
    return sum   
n=int(input())
f=n
while(f!=1 and f!=4):
    f=is_happy(f)
if(f==1):
    print('True')
else:
    print('False')

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def next_prime(n,x):
    while is_prime(n)==False:
        n+=x
    return n
t=int(input())
for i in range(t):
    n=int(input())
    pp=next_prime(n,-1)
    np=next_prime(n,1)
    if n - pp <= np - n:
        print(pp)
    else:
        print(np)
        
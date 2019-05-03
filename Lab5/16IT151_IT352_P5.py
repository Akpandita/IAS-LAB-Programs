import math
def SieveOfEratosthenes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    for p in range(2, n): 
        if prime[p]: 
            if n%p==0:
                return p,n//p
    return 0,0
s=int(input('Enter the Cipher Text:'))
n=int(input('Enter the value of N:'))
e=int(input('Enter the value of E:'))
p,q=SieveOfEratosthenes(n)
if p==0:
    print("N not a product of two primes")
    exit(0)
else:
    phi=(p-1)*(q-1)
    if math.gcd(phi,e)>1:
        print("phi and e are not coprimes")
        exit(0)
output=""
output_arr=[]
x=s
partials=[]
while(1):
    y=pow(x,e)%n
    partials.append(y)
    if y==s:
        break
    x=y
print('Partails:-',partials)
print('Plain Text:-')
print(x)

ciphertext=""
print('Validating Output')
y=pow(x,e)%n
ciphertext=y
print(ciphertext)

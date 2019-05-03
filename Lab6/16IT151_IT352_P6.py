import math

def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return -1
      
e=int(input('Enter the value of e:- '))
r=int(input('Enter the value of r:- '))
s=input()
p=int(input('Enter the value of p:- '))
q=int(input('Enter the value of q:- '))
n=p*q
cnt=1
r_inv=modInverse(r,n)
if r_inv==-1:
        print("r_inv cannot be found")
        exit(0)
phi=(p-1)*(q-1)
while(1):
    if (cnt*phi+1)%e==0:
        d=(cnt*phi+1)//e
        break
    elif cnt>100000:
        print("Not possible to find d")
        exit(0)
    cnt+=1
number=math.log(n,2)
packet_size=math.floor(number//8)
print(packet_size)

leng=len(s)
for i in range(0,leng,packet_size):
    pack=""
    for j in range(packet_size):
    	if i+j<leng:
        	pack+=hex(ord(s[i+j])).split('x')[-1]
    m=int(pack,16)
    print("packet "+str(i//packet_size)+" :-")
    print("message:- ",m)
    m_bar=(m*pow(r,e))%n
    print("m_bar(encrypted message after blind attack):- ",m_bar)
    st_bar=pow(m_bar,d)%n
    print("st_bar(blind signature):- ",st_bar)
    st=(st_bar*r_inv)%n
    print("st:- (signature)",st)
    print("st power e mod n",pow(st,e)%n)
    print("m",m)
    if m==pow(st,e)%n:
    	print('Verified!!')
    st=hex(st).split('x')[-1]
    readable=""
    for j in range(0,len(st),2):
    	if j+2 < len(st):
    		readable+=chr(int(st[j:j+2],16))
    	else:
    		readable+=chr(int(st[j:],16))
    print("Human readable form:-",readable)
    


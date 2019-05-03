from tkinter import *
import math

def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return -1

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

def CCT():
    global screen3
    screen3=Toplevel(screen)
    screen3.title("CCT")
    screen3.geometry("500x700")

    global e
    global r
    global s
    global p
    global q
    global e_entry
    global r_entry
    global s_entry
    global p_entry
    global q_entry
    
    e=StringVar()
    r=StringVar()
    s=StringVar()
    p=StringVar()
    q=StringVar()
    Label(screen3, text="Please enter details *").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="e *").pack()
    e_entry = Entry(screen3, textvariable=e)
    e_entry.pack()
    Label(screen3, text="r *").pack()
    r_entry = Entry(screen3, textvariable=r)
    r_entry.pack()
    Label(screen3, text="s *").pack()
    s_entry = Entry(screen3, textvariable=s)
    s_entry.pack()
    Label(screen3, text="p *").pack()
    p_entry = Entry(screen3, textvariable=p)
    p_entry.pack()
    Label(screen3, text="q *").pack()
    q_entry = Entry(screen3, textvariable=q)
    q_entry.pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Submit",width="10", height="1",command=evaluateCct).pack()

def evaluateCct():
    e1=int(e.get())
    r1=int(r.get())
    s1=str(s.get())
    p1=int(p.get())
    q1=int(q.get())
    n=p1*q1
    cnt=1
    r_inv=modInverse(r1,n)
    if r_inv==-1:
        print("r_inv cannot be found")
        exit(0)
    phi=(p1-1)*(q1-1)
    while(1):
        if (cnt*phi+1)%e1==0:
            d=(cnt*phi+1)//e1
            break
        elif cnt>100000:
            print("Not possible to find d")
            exit(0)
        cnt+=1
    number=math.log(n,2)
    packet_size=math.floor(number//8)
    print(packet_size)
    ans=""
    leng=len(s1)
    Label(screen3,text="").pack()
    Label(screen3,text="PlainText:-",bg="white",width="300",height="2").pack()
    for i in range(0,leng,packet_size):
        pack=""
        for j in range(packet_size):
            if i+j<leng:
                pack+=hex(ord(s1[i+j])).split('x')[-1]
        m=int(pack,16)
        print("packet "+str(i//packet_size)+" :-")
        print("ciphertext:- ",m)
        m_bar=(m*pow(r1,e1))%n
        print("message by the attacker:- ",m_bar)
        st_bar=pow(m_bar,d)%n
        print("message by the system:- ",st_bar)
        st=(st_bar*r_inv)%n
        print("plaintext:- ",st)
        if m==pow(st,e1)%n:
            print('Verified!!')
        st1=st
        st=hex(st).split('x')[-1]
        readable=""
        for j in range(0,len(st),2):
            if j+2 < len(st):
                print(chr(int(st[j:j+2],16))+" ",end='')
            else:
                print(chr(int(st[j:],16)))
        print("Human readable form:-",readable)
        Label(screen3,text="packet no "+str(i//2+1)+" Plaintext:-",bg="white",width="300",height="2").pack()
        Label(screen3,text=str(st1),bg="grey",width="300",height="2",font=("Calibri",13)).pack()
    
    e_entry.delete(0,END)
    r_entry.delete(0,END)
    s_entry.delete(0,END)
    p_entry.delete(0,END)
    q_entry.delete(0,END)


def BSA():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("BSA")
    screen1.geometry("500x700")

    global e
    global r
    global s
    global p
    global q
    global e_entry
    global r_entry
    global s_entry
    global p_entry
    global q_entry
    
    e=StringVar()
    r=StringVar()
    s=StringVar()
    p=StringVar()
    q=StringVar()
    Label(screen1, text="Please enter details *").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="e *").pack()
    e_entry = Entry(screen1, textvariable=e)
    e_entry.pack()
    Label(screen1, text="r *").pack()
    r_entry = Entry(screen1, textvariable=r)
    r_entry.pack()
    Label(screen1, text="s *").pack()
    s_entry = Entry(screen1, textvariable=s)
    s_entry.pack()
    Label(screen1, text="p *").pack()
    p_entry = Entry(screen1, textvariable=p)
    p_entry.pack()
    Label(screen1, text="q *").pack()
    q_entry = Entry(screen1, textvariable=q)
    q_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Submit",width="10", height="1",command=evaluateBsa).pack()

def evaluateBsa():
    e1=int(e.get())
    r1=int(r.get())
    s1=str(s.get())
    p1=int(p.get())
    q1=int(q.get())
    n=p1*q1
    cnt=1
    r_inv=modInverse(r1,n)
    if r_inv==-1:
        print("r_inv cannot be found")
        exit(0)
    phi=(p1-1)*(q1-1)
    while(1):
        if (cnt*phi+1)%e1==0:
            d=(cnt*phi+1)//e1
            break
        elif cnt>100000:
            print("Not possible to find d")
            exit(0)
        cnt+=1
    number=math.log(n,2)
    packet_size=math.floor(number//8)
    print(packet_size)
    ans=""
    leng=len(s1)
    Label(screen1,text="").pack()
    Label(screen1,text="PlainText:-",bg="white",width="300",height="2").pack()
    for i in range(0,leng,packet_size):
        pack=""
        for j in range(packet_size):
            if i+j<leng:
                pack+=hex(ord(s1[i+j])).split('x')[-1]
        m=int(pack,16)
        print("packet "+str(i//packet_size)+" :-")
        print("message:- ",m)
        m_bar=(m*pow(r1,e1))%n
        print("m_bar(encrypted message after blind attack):- ",m_bar)
        st_bar=pow(m_bar,d)%n
        print("st_bar(blind signature):- ",st_bar)
        st=(st_bar*r_inv)%n
        print("st:- (signature)",st)
        print("st power e mod n",pow(st,e1)%n)
        print("m",m)
        if m==pow(st,e1)%n:
            print('Verified!!')
        st1=st
        st=hex(st).split('x')[-1]
        readable=""
        for j in range(0,len(st),2):
            if j+2 < len(st):
                readable+=chr(int(st[j:j+2],16))
            else:
                readable+=chr(int(st[j:],16))
        print("Human readable form:-",readable)
        Label(screen1,text="packet no "+str(i//2+1)+" Signature:-",bg="white",width="300",height="2").pack()
        Label(screen1,text=str(st1),bg="grey",width="300",height="2",font=("Calibri",13)).pack()
    
    e_entry.delete(0,END)
    r_entry.delete(0,END)
    s_entry.delete(0,END)
    p_entry.delete(0,END)
    q_entry.delete(0,END)
    
def RSA():
    global screen2
    screen2=Toplevel(screen)
    screen2.title("RSA")
    screen2.geometry("500x700")

    global ciphertext
    global n
    global e
    global ciphertext_entry
    global n_entry
    global e_entry
    
    ciphertext=StringVar()
    n=StringVar()
    e=StringVar()
    Label(screen2, text="Please enter details *").pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Ciphertext Text *").pack()
    ciphertext_entry = Entry(screen2, textvariable=ciphertext)
    ciphertext_entry.pack()
    Label(screen2, text="N *").pack()
    n_entry = Entry(screen2, textvariable=n)
    n_entry.pack()
    Label(screen2, text="E *").pack()
    e_entry = Entry(screen2, textvariable=e)
    e_entry.pack()
    Button(screen2, text="Submit",width="10", height="1",command=evaluatersa).pack()

def evaluatersa():
    ciphertext1=int(ciphertext.get())
    n1=int(n.get())
    e1=int(e.get())
    
    p,q=SieveOfEratosthenes(n1)
    if p==0:
        print("N not a product of two primes")
        exit(0)
    else:
        phi=(p-1)*(q-1)
        if math.gcd(phi,e1)>1:
            print("phi and e are not coprimes")
            exit(0)
    output=""
    output_arr=[]
    x=ciphertext1
    partials=[]
    while(1):
        y=pow(x,e1)%n1
        partials.append(y)
        if y==ciphertext1:
            break
        x=y
    print('Plain Text:-')
    print(x)
    Label(screen2,text="").pack()
    Label(screen2,text="PlainText:-",bg="white",width="300",height="2").pack()
    Label(screen2,text=str(x),bg="grey",width="300",height="2",font=("Calibri",13)).pack()
    
    ciphertext_entry.delete(0,END)
    n_entry.delete(0,END)
    e_entry.delete(0,END)

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Encryption Algorithms")
    Label(text="Encryption Algorithms",bg="grey", width="300", height="2", font=("Calibri",13)).pack()
    Label(text="").pack()
    Button(text="BSA",width="30", height="2",command=BSA).pack()
    Label(text="").pack()
    Button(text="RSA",width="30", height="2",command=RSA).pack()
    Label(text="").pack()
    Button(text="CCT",width="30", height="2",command=CCT).pack()

    screen.mainloop()

main_screen()

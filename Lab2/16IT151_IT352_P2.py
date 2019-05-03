s=input()
if len(s)<8:
    print('Error: Given input string less than 8')
else:
    s=s.replace(' ','')
    if len(s)<8:
        s=s+' '*(8-len(s))
    print('select a choice: 1 or 2')
    choice=int(input())
    if choice==1:
        s=s[:8]
    else:
        s=s[len(s)-8:]
    s2=[]
    for i in range(8):
        s3=bin(ord(s[i]))[2:]
        s3='0'*(8-len(s3))+s3
        for j in range(8):
            s2.append(s3[j])
    PC1=[[57,49,41,33,25,17,9],
         [1,58,50,42,34,26,18],
         [10,2,59,51,43,35,27],
         [19,11,3,60,52,44,36],
         [63,55,47,39,31,23,15],
         [7,62,54,46,38,30,22],
         [14,6,61,53,45,37,29],
         [21,13,5,28,20,12,4]
        ]
    PC2=[[14,17,11,24,1,5],
         [3,28,15,6,21,10],
         [23,19,12,4,26,8],
         [16,7,27,20,13,2],
         [41,52,31,37,47,55],
         [30,40,51,45,33,48],
         [44,49,39,56,34,53],
         [46,42,50,36,29,32]
        ]
    out_pc1=[]
    f=open("Round-key.txt","+w")
    for i in range(56):
        out_pc1.append(0)
    for i in range(8):
        for j in range(7):
            out_pc1[i*7+j]=s2[PC1[i][j]-1]
    print("output of PC1:- ",end='')
    print(''.join(out_pc1))
    left=out_pc1[:28]
    right=out_pc1[28:]
    for i in range(1,17):
        if i==1 or i==2 or i==9 or i==16:
            left=left[1:]+left[:1]
            right=right[1:]+right[:1]
        else:
            left=left[2:]+left[:2]
            right=right[2:]+right[:2]
        out_shift=left[:]+right[:]
        out_pc2=[]
        for j in range(48):
            out_pc2.append(0)
        for k in range(8):
            for j in range(6):
                out_pc2[k*6+j]=out_shift[PC2[k][j]-1]
        print("round"+str(i)+": ",end='')
        f.write("round"+str(i)+": ")
        x=''.join(out_pc2)
        print(x)
        f.write(x)
        f.write("\n")
    f.close()

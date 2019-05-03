#taking input string
s=input("Enter the input:-").strip()
if len(s)>40:
	exit('Length greater than 40 bytes')
key=input("Enter the key:-")
if len(key)!=8:
	exit('Key not equal to 8 bytes')
key2=[]
for j in range(8):
    s1=bin(ord(key[j]))[2:]
    rem=8-len(s1)
    s1='0'*rem+s1
    for k in range(8):
        key2.append(s1[k])
key2=''.join(key2)
keys=[]
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
for i in range(56):
    out_pc1.append(0)
for i in range(8):
    for j in range(7):
        out_pc1[i*7+j]=key2[PC1[i][j]-1]
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
    x=''.join(out_pc2)
    keys.append(x)

init_perm=[[0 for i in range(8)] for j in range(8)]
fini_perm=[[0 for i in range(8)] for j in range(8)]

#making initial permutation
for i in range(7,-1,-1):
    if i==7:
        for j in range(4,8):
            init_perm[j][i]=2*(j-4)+1
            init_perm[j-4][i]=2*(j-3)
    else:
        for j in range(4,8):
            init_perm[j][i]=init_perm[j][i+1]+8
            init_perm[j-4][i]=init_perm[j-4][i+1]+8

#making final permutation
for i in range(0,8,2):
    for j in range(7,-1,-1):
        if i==0 and j==7:
            fini_perm[j][i]=33
        elif j==7:
            fini_perm[j][i]=fini_perm[j][i-2]+8
        else:
            fini_perm[j][i]=fini_perm[j+1][i]+1
        fini_perm[j][i+1]=fini_perm[j][i]-32

len_str=len(s)
if len(s)%8!=0:
    rem_spaces=8-len(s)%8
    s=s+' '*(rem_spaces)

print("\ninitial bits of all the characters:-\n")

print("[",end='')

#feeding initial string to initial permutation table
output_init=[]
new_len=len(s)
for i in range(new_len//8):
    s1=s[i*8:(i+1)*8]
    arr1=[]
    for j in range(8):
        arr1.append(ord(s1[j]))
    arr2=[]
    for j in range(8):
        s1=bin(arr1[j])[2:]
        rem=8-len(s1)
        s1='0'*rem+s1
        print(s1+", ",end='')
        for k in range(8):
            arr2.append(s1[k])
    arr3=[0]*65
    output_init.append([])
    for j in range(8):
        for k in range(8):
            arr3[j*8+k+1]=arr2[init_perm[j][k]-1]
    for j in range(1,65):
        output_init[i].append(arr3[j])
print("]")

init_arr=[]
for i in range(new_len//8):
    init_arr.append(''.join(output_init[i]))

print("\nIntermediate output beween IP AND ROUNDS:-\n")
print(init_arr)

expansion=[32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9,10,11,12,13,
           12,13,14,15,16,17,
           16,17,18,19,20,21,
           20,21,22,23,24,25,
           24,25,26,27,28,29,
           28,29,30,31,32, 1]

sboxs=[[14, 4,13, 1, 2,15,11, 8, 3,10, 6,12, 5, 9, 0, 7,
        0,15, 7, 4,14, 2,13, 1,10, 6,12,11, 9, 5, 3, 8,
        4, 1,14, 8,13, 6, 2,11,15,12, 9, 7, 3,10, 5, 0,
       15,12, 8, 2, 4, 9, 1, 7, 5,11, 3,14,10, 0, 6,13],
       [15, 1, 8,14, 6,11, 3, 4, 9, 7, 2,13,12, 0, 5,10,
         3,13, 4, 7,15, 2, 8,14,12, 0, 1,10, 6, 9,11, 5,
         0,14, 7,11,10, 4,13, 1, 5, 8,12, 6, 9, 3, 2,15,
        13, 8,10, 1, 3,15, 4, 2,11, 6, 7,12, 0, 5,14, 9],
       [10, 0, 9,14, 6, 3,15, 5, 1,13,12, 7,11, 4, 2, 8,
        13, 7, 0, 9, 3, 4, 6,10, 2, 8, 5,14,12,11,15, 1,
        13, 6, 4, 9, 8,15, 3, 0,11, 1, 2,12, 5,10,14, 7,
         1,10,13, 0, 6, 9, 8, 7, 4,15,14, 3,11, 5, 2,12],
       [ 7,13,14, 3, 0, 6, 9,10, 1, 2, 8, 5,11,12, 4,15,
        13, 8,11, 5, 6,15, 0, 3, 4, 7, 2,12, 1,10,14, 9,
        10, 6, 9, 0,12,11, 7,13,15, 1, 3,14, 5, 2, 8, 4,
         3,15, 0, 6,10, 1,13, 8, 9, 4, 5,11,12, 7, 2,14],
       [ 2,12, 4, 1, 7,10,11, 6, 8, 5, 3,15,13, 0,14, 9,
        14,11, 2,12, 4, 7,13, 1, 5, 0,15,10, 3, 9, 8, 6,
         4, 2, 1,11,10,13, 7, 8,15, 9,12, 5, 6, 3, 0,14,
        11, 8,12, 7, 1,14, 2,13, 6,15, 0, 9,10, 4, 5, 3],
       [12, 1,10,15, 9, 2, 6, 8, 0,13, 3, 4,14, 7, 5,11,
        10,15, 4, 2, 7,12, 9, 5, 6, 1,13,14, 0,11, 3, 8,
         9,14,15, 5, 2, 8,12, 3, 7, 0, 4,10, 1,13,11, 6,
         4, 3, 2,12, 9, 5,15,10,11,14, 1, 7, 6, 0, 8,13],
       [ 4,11, 2,14,15, 0, 8,13, 3,12, 9, 7, 5,10, 6, 1,
        13, 0,11, 7, 4, 9, 1,10,14, 3, 5,12, 2,15, 8, 6,
         1, 4,11,13,12, 3, 7,14,10,15, 6, 8, 0, 5, 9, 2,
         6,11,13, 8, 1, 4,10, 7, 9, 5, 0,15,14, 2, 3,12],
       [13, 2, 8, 4, 6,15,11, 1,10, 9, 3,14, 5, 0,12, 7,
         1,15,13, 8,10, 3, 7, 4,12, 5, 6,11, 0,14, 9, 2,
         7,11, 4, 1, 9,12,14, 2, 0, 6,10,13,15, 3, 5, 8,
         2, 1,14, 7, 4,10, 8,13,15,12, 9, 0, 3, 5, 6,11]
       ]

pbox=[15, 6,19,20,28,11,27,16, 0,14,22,25, 4,17,30, 9,
       1, 7,23,13,31,26, 2, 8,18,12,29, 5,21,10, 3,24]


f=open("Output-of-Program-4.txt","+w")
init2_arr=[]
for i in range(new_len//8):
    arr1=init_arr[i]
    for j in range(16):
        if j==0:
            li=arr1[:32]
            ri=arr1[32:]
            #print('Before operations:-')
            f.write('Before operations:-'+'\n')
            #print('left:',''.join(li)+'   ',end='')
            f.write('left: '+''.join(li)+'   ')
            #print('right',''.join(ri))
            f.write('right '+''.join(ri))
        exp_out=[]
        for k in range(48):
            exp_out.append(ri[expansion[k]-1])
        xor_out=[]
        for k in range(48):                          
            if keys[j][k]==exp_out[k]:
                xor_out.append('0')
            else:
                xor_out.append('1')
        sbox_out=[]
        for k in range(8):
            s1=xor_out[k*6:(k+1)*6]
            x=int(s1[0]+s1[5],2)
            y=int(''.join(s1[1:5]),2)
            out=sboxs[k][16*x+y]
            out=bin(out)[2:]
            if len(out)!=4:
                out='0'*(4-len(out))+out
            sbox_out.append(out)
        sbox_out=''.join(sbox_out)
        pbox_out=[]
        for k in range(32):
            pbox_out.append(sbox_out[pbox[k]])
        xor2_out=[]
        for k in range(32):
            if li[k]==pbox_out[k]:
                xor2_out.append('0')
            else:
                xor2_out.append('1')
        li=ri
        ri=xor2_out[:]
        #print('chunk '+str(i+1)+' Round '+str(j+1)+":-")
        f.write('chunk '+str(i+1)+' Round '+str(j+1)+":-")
        f.write('\n')
        #print('left:',''.join(li)+'   ',end='')
        f.write('left:'+' '+''.join(li)+'   ')
        f.write('\n')
        #print('right:',''.join(ri))
        f.write('right:'+' '+''.join(ri))
        f.write('\n')
    combi=ri[:]+li[:]
    init2_arr.append(combi)
 
print('\nfinal output with swapping:-')
for i in range(new_len//8):
    print(''.join(init2_arr[i]))

output_fini=[]
for i in range(new_len//8):
    arr2=init2_arr[i]
    arr3=[0]*65
    for j in range(8):
        for k in range(8):
            arr3[j*8+k+1]=arr2[fini_perm[j][k]-1]
    output_fini.append([])
    for j in range(1,65):
        output_fini[i].append(arr3[j])
print("\nOutput after final permutation")
f.write("\nOutput after final permutation\n")
for i in range(new_len//8):
    print(''.join(output_fini[i]))
    f.write(''.join(output_fini[i]))
    f.write('\n')
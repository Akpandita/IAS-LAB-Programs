#taking input string
s=input("Enter the input:-").replace(' ','')

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
    for j in range(8):
        arr1=output_init[i][j*8:(j+1)*8]
        init_arr.append(''.join(arr1))

print("\nIntermediate output beween IP AND FP:-\n")
print(init_arr)
init_arr=''.join(init_arr)

output_fini=[]
for i in range(new_len//8):
    arr2=init_arr[i*64:(i+1)*64]
    arr3=[0]*65
    for j in range(8):
        for k in range(8):
            arr3[j*8+k+1]=arr2[fini_perm[j][k]-1]
    output_fini.append([])
    for j in range(1,65):
        output_fini[i].append(arr3[j])

output_str=""
for i in range(new_len//8):
    for j in range(64):
        if j%8==0:
            s1=""
            s1+=output_fini[i][j]
        elif j%8==7:
            s1+=output_fini[i][j]
            output_str+=chr(int(s1,2))
        else:
            s1+=output_fini[i][j]
print("\nFinal Output:-\n")
print(output_str)
        
        

def maxsequence(list):
    max=0
    z=0
    sublist = []
    while(1):
        for i in range(len(list)):
            sum = 0
            z=z+1
            for j in range(i+1-z):
                sum = list[j-1+z] + sum
                sublist.append(list[j - 1 + z])
                if(sum>max):
                    max=sum
                    del sublist[j-1+z]
        if(z==len(list)):
            break
    return max,sublist
list=[]
while (1):
    a= input("dwse num:")
    if(a=="exit"):
        break
    else:
        list.append(int(a))
b= maxsequence(list)
print (b)
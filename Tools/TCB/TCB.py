from itertools import groupby
###
# find consecutive numbers
def FCN(index_one):
    index_one_sort = sorted(index_one)  
    conti_list=[]
    fun = lambda x: x[1]-x[0]
    for k, g in groupby(enumerate(index_one_sort), fun):
        l1 = [j for i, j in g]
        if len(l1) > 1:
            scop = str(min(l1)) + '-' + str(max(l1))
        else:
            scop = l1[0]
        conti_list.append(scop)
    return conti_list
###
for num in range(1000000):
    num+=1
    num2_list=list(bin(num)[2:])
    index_one=[]
    for i in range(len(num2_list)):
        if num2_list[i] == "1":
            i2=len(num2_list)-i-1
            index_one.append(i2)
    conti_list=FCN(index_one)
    index_TCB=[]
    for j in range(len(conti_list)):
        j2=str(conti_list[j])
        if "-" in j2:
            j2_spilt=j2.split("-")
            index_TCB.append([int(j2_spilt[1])+1,int(j2_spilt[0])])
        else:
            index_TCB.append(int(j2))
    # print(index_TCB)
    check_num=0
    shifter_str=""
    for k in range(len(index_TCB)-1,-1,-1):
        k2=str(index_TCB[k])
        if ("[" in k2) or ("]" in k2):
            k3=k2[1:-1].split(",")
            str_k=" N << %d - N << %d"%(int(k3[0]),int(k3[1]))
            check_num=check_num+2**int(k3[0])-2**int(k3[1])
        else:
            str_k=" N << %s"%k2
            check_num=check_num+2**(int(k2))
        shifter_str=shifter_str+" +"+str_k
    # print("N * %d =%s"%(num,shifter_str[2:]))
    # print("check=",check_num)
    if num != check_num:
        print("Something happend!!!")
        print("N * %d =%s"%(num,shifter_str[2:]))
        print("check=",check_num)
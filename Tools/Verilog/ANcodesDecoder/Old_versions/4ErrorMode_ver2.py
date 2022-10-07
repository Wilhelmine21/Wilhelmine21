# Error model 
    # 1. Uni_FAC 
        # Unidirectional / Fully asymmetric channel model 
    # 2. Alter_FAC
        # Alternative-direction / Fully asymmetric channel model 
    # 3. BER 
        # Bit Error Rate model
    # 4. AWE
        # Arithmetic Weight Error model

# input number--->auto find A---> mode select ---> correction 
    #---> auto write verilog ---> auto VCD
import numpy as np
import os
import time
####---------------------------------------------------------####
def Bin2Dec(bit, Bin):
    A=0
    Bin=list(Bin)
    Bin.reverse()
    for i in range(0,bit):
        A=Bin[i]*2**(i)+A
    return A
####----------------------####
def Dec2Bin(bit, Dec):
    binrandom0 = bin(Dec)
    d1=binrandom0[2:]                   #ex.1111
    h2=d1.zfill(bit)                    #ex.00001111
    data=list(h2)                       #turn to list: ex.['0', '0', '0', '0', '1', '1', '1', '1']
    arrayh=np.array(data)               #ex.['0' '0' '0' '0' '1' '1' '1' '1']
    arrayh=arrayh.astype(int)           #del'' ex.[0 0 0 0 1 1 1 1]
    return arrayh
####-----------------------table-----------------------------####
#One-way error:Uni or Alter
def TableOne(module):  
    Ra=[0]*(module-1) #R:1-46
    Ta=[0]*module
    Ra_array=np.array(Ra)
    Ta_array=np.array(Ta)
    Ra_array[0]=1  #R:1
    for i in range(1,module-1):#1-45(<-扣掉R:1)
        Ra_array[i]=(Ra_array[i-1]*2) % module
        Ta_array[Ra_array[i]]=i
    return Ra_array,Ta_array
####----------------------####
#Two-way error:AWE or BER
def TableTwo(module):  
    Ra=[0]*(module-1) #R:1-46
    Ta=[0]*module
    Sa=[0]*module
    Ra_array=np.array(Ra)
    Ta_array=np.array(Ta)
    Sa_array=np.array(Sa)
    Ra_array[0]=1
    for i in range(1,module-1): #1-45(<-扣掉R:1)
        Ra_array[int((module-1)/2)]=(module-1)
        #Ra_array[23]=46
        Ra_array[i]=(Ra_array[i-1]*2) % module
        if(i<((module-1)/2)):
            Ta_array[Ra_array[i]]=i
            Sa_array[Ra_array[i]]=0
        else:
            Ta_array[Ra_array[i]]=i-((module-1)/2)
            Sa_array[Ra_array[i]]=1
    Sa_array[1]=0
    Sa_array[(module-1)]=1
    return Ra_array,Ta_array,Sa_array
####------------------Auto-Find-A----------------------------####
def FindA(mode,rang2):
    Two_A=[]
    Two_A_bit=[]
    Two_cbit=[]
    Two_cbit_N=[]
    One_A=[]
    One_A_bit=[]
    One_cbit=[]
    One_cbit_N=[]    
    rang1=7
    for module in range(rang1,(rang2+1)):
            Ra_array,Ta_array,Sa_array=TableTwo(module)
            Ra2_array,Ta2_array=TableOne(module)
            module_2=bin(module)[2:]
            module_len=len(module_2)
            count=0
            for i in range(1, module):
                if i in Ra_array:
                    count+=1
            check=set(Ra_array)
            if count == (module-1) and len(Ra_array) == len(check):
                Two_A.append(module)
                maxT=max(Ta_array)
                cbit=maxT+1
                Two_cbit.append(cbit)
                cbitN=cbit-module_len
                Two_cbit_N.append(cbitN)
                Two_A_bit.append(module_len)         
            count2=0
            for i2 in range(1, module):
                if i2 in Ra2_array:
                    count2+=1
            check2=set(Ra2_array)
            if count2 == (module-1) and len(Ra2_array) == len(check2):
                One_A.append(module)
                maxT2=max(Ta2_array)
                cbit2=maxT2+1
                One_cbit.append(cbit2)
                cbitN2=cbit2-module_len
                One_cbit_N.append(cbitN2)
                One_A_bit.append(module_len)
    #################################################
    #the same bit of A select which can correct more 
    bitA=Two_A_bit[-1] +1
    Two_A_bit_len=len(Two_A_bit)
    Two_A_most=[]
    for j in range(0,bitA): #Value content
        t1=[]
        for k in range(0,Two_A_bit_len):#Array position    
            if Two_A_bit[k]==j:
                t1.append(Two_A[k])
        if len(t1) > 1:
            t1max=max(t1)
            Two_A_most.append(t1max)
        elif len(t1) == 1:
            Two_A_most.append(t1[0])
    Two_A_most_cbitN=[]
    for g in range(0,len(Two_A_most)):
        t2=Two_A_most[g]
        Two_most_index=Two_A.index(t2)
        t3=Two_cbit_N[Two_most_index]
        Two_A_most_cbitN.append(t3)
    #################################################
    bitA_One=One_A_bit[-1] +1
    One_A_bit_len=len(One_A_bit)
    One_A_most=[]
    for j1 in range(0,bitA_One):
        t1One=[]
        for k1 in range(0,One_A_bit_len):   
            if One_A_bit[k1]==j1:
                t1One.append(One_A[k1])
        if len(t1One) > 1:
            t1maxOne=max(t1One)
            One_A_most.append(t1maxOne)
        elif len(t1One) == 1:
            One_A_most.append(t1One[0])
    One_A_most_cbitN=[]
    for g1 in range(0,len(One_A_most)):
        t2One=One_A_most[g1]
        One_most_index=One_A.index(t2One)
        t3One=One_cbit_N[One_most_index]
        One_A_most_cbitN.append(t3One)
    #################################################
    if mode == 1:
        print('\n-------------Find an available A-------------')
        print('雙向錯誤可用的A(%d~%d)=%s'%(rang1,rang2,Two_A))
        print('可更正bit數(N)=',Two_cbit_N)
        print('\n單向錯誤可用的A(7~100)=',One_A)
        print('可更正bit數(N)=',One_cbit_N)
        return Two_A,Two_cbit_N,One_A,One_cbit_N
    #################################################
    else:
        print('\n-------------Find the most appropriate A-------------')
        print("雙向錯誤最合適的A=",Two_A_most)
        print("雙向錯誤可更正bit數(N)=",Two_A_most_cbitN)
        print("\n單向錯誤最合適的A=",One_A_most)
        print("單向錯誤可更正bit數(N)=",One_A_most_cbitN)
        return Two_A_most,Two_A_most_cbitN,One_A_most,One_A_most_cbitN
####----------------------####
def AutoFindA(mode,A,cbitN):    
    N=int(input('Input a number(N):'))
    N_2=bin(N)[2:]
    N_2_len=len(N_2)
    print('N的Bit數=',N_2_len) 
    if mode == 1 :
        print('----------Two-way error mode----------')
        Two_A=A
        Two_cbit_N=cbitN
        if N_2_len in Two_cbit_N: #剛好有對應的樹
            x_Two=Two_cbit_N.index(N_2_len)
            findA_Two=Two_A[x_Two]
            print('適合的A=',findA_Two)
            print('可更正的bit數(N)=',Two_cbit_N[x_Two])
            return N,findA_Two,Two_cbit_N[x_Two]
        else:   #大於Nbit的最小數
            Two_cbit_N_a=np.array(Two_cbit_N)
            index_Two=(np.abs(Two_cbit_N_a-N_2_len)).argmin()
            findA2_Two=Two_A[index_Two]
            if N_2_len < index_Two :
                print('適合的A=',findA2_Two)
                print('可更正的bit數(N)=',Two_cbit_N[index_Two])
                return N,findA2_Two,Two_cbit_N[index_Two]
            else:
                findA3_Two=Two_A[(index_Two+1)]
                print('適合的A=',findA3_Two)
                print('可更正的bit數(N)=',Two_cbit_N[(index_Two+1)])
                return N,findA3_Two,Two_cbit_N[(index_Two+1)]
    else :
        print('----------One-way error mode----------')
        One_A=A
        One_cbit_N=cbitN
        if N_2_len in One_cbit_N: #剛好有對應的樹
            x_One=One_cbit_N.index(N_2_len)
            findA_One=One_A[x_One]
            print('適合的A=',findA_One)
            print('可更正的bit數(N)=',One_cbit_N[x_One])
            return N,findA_One,One_cbit_N[x_One]
        else:   #大於Nbit的最小數
            One_cbit_N_a=np.array(One_cbit_N)
            index_One=(np.abs(One_cbit_N_a-N_2_len)).argmin()
            findA2_One=One_A[index_One]
            if N_2_len < index_One :
                print('適合的A=',findA2_One)
                print('可更正的bit數(N)=',One_cbit_N[index_One])
                return N,findA2_One,One_cbit_N[index_One]
            else:
                findA3_One=One_A[(index_One+1)]
                print('適合的A=',findA3_One)    
                print('可更正的bit數(N)=',One_cbit_N[(index_One+1)])
                return N,findA3_One,One_cbit_N[(index_One+1)]
####------------------Error-----------------------------####
def errorGenTwo(bitAN,module,N):
    AN=module*N
    AN2=bin(AN)[2:]
    AN2_0=AN2.zfill(bitAN)
    AN2_0List=list(AN2_0)
    ebit=np.random.randint(0,bitAN)
    ebitp=bitAN-(ebit+1)
    if AN2_0List[ebit] == '0':
        AN2_0List[ebit] = '1'
    else:
        AN2_0List[ebit] = '0'
    ANe2=''.join(AN2_0List)
    ANe=int(ANe2,2)
    print('\n---------Original Data-------------')
    print('Correct N=',N)
    print('Correct AN=',AN)
    print('Correct AN(2)=',AN2)
    print('module=',module)
    print('\n------Random error generation------')
    print('Error bit=',ebitp)
    print('Error AN=',ANe)
    print('Error AN(2)=',ANe2)
    return ANe,ANe2,ebit
####----------------------####
def errorGenLH(bitAN,module,N):
    cnt=0
    AN=module*N
    AN2=bin(AN)[2:]
    AN2_0=AN2.zfill(bitAN)
    AN2_0List=list(AN2_0)
    while cnt < 1:
        ebit=np.random.randint(0,bitAN)
        ebitp=bitAN-(ebit+1)
        if AN2_0List[ebit] == '0':
            AN2_0List[ebit] = '1'
            cnt+=1
    
    ANe2=''.join(AN2_0List)
    ANe=int(ANe2,2)
    print('\n---------Original Data-------------')
    print('Correct N=',N)
    print('Correct AN=',AN)
    print('Correct AN(2)=',AN2)
    print('module=',module)
    print('\n------Random error generation------')
    print('Error bit=',ebitp)
    print('Error AN=',ANe)
    print('Error AN(2)=',ANe2)
    return ANe,ANe2,ebit
####----------------------####
def errorGenHL(bitAN,module,N):
    cnt=0
    AN=module*N
    AN2=bin(AN)[2:]
    AN2_0=AN2.zfill(bitAN)
    AN2_0List=list(AN2_0)
    while cnt < 1:
        ebit=np.random.randint(0,bitAN)
        ebitp=bitAN-(ebit+1)
        if AN2_0List[ebit] == '1':
            AN2_0List[ebit] = '0'
            cnt+=1
    
    ANe2=''.join(AN2_0List)
    ANe=int(ANe2,2)
    print('\n---------Original Data-------------')
    print('Correct N=',N)
    print('Correct AN=',AN)
    print('Correct AN(2)=',AN2)
    print('module=',module)
    print('\n------Random error generation------')
    print('Error bit=',ebitp)
    print('Error AN=',ANe)
    print('Error AN(2)=',ANe2)
    return ANe,ANe2,ebit   
####------------------correction-----------------------------#### 
def CorrectTwo(bit,data,module,Ra_array,Ta_array,Sa_array):
    R=data % module
    print('\n----------CorrectTwo----------')
    for i in range(1,bit):
        databin=Dec2Bin(bit, data)
        bitint=int(bit)
        #if no int(bit) #when bit=36, 2^bit=0
        #I do not know why.
        pow2Bit=pow(2,bitint)
        if data < pow2Bit:              
            if(R==0):
                final_answer=int(data/module)
                final_answer_bin=Dec2Bin(bit, final_answer)
                print('There is no error.')
                #print('final_answer_bin=',final_answer_bin)
                return final_answer_bin
            elif R in Ra_array:   
                errorbit=Ta_array[R]
                print('Error is in',errorbit,'bit')
                #print('It was\n',databin)
                data_B2D=Bin2Dec(bit,databin)
                errValue=2**(errorbit)
                #print('error value=2**(%d)=%d'%(errorbit,errValue))
                if(Sa_array[R]==0):
                    if(errValue>data_B2D):
                        print('Error cannot be detected.')
                        #print('databin=',databin)
                        return databin
                        break
                    else:
                        print('------Error come from Addition.------')
                        dec_data=data_B2D-errValue
                else:
                    if(data_B2D+errValue > 2**bit):
                        print('Error cannot be detected.')
                        #print('databin=',databin)
                        return databin
                        break
                    else:
                        print('------Error come fromr Subtraction.------')
                        dec_data=data_B2D+errValue
                        #print('dec_data===',dec_data)
                #############################
                if(dec_data % module==0):
                    final_answer=int(dec_data/module)
                    print('final_answer=',final_answer)
                    final_answer_bin=Dec2Bin(bit, final_answer)
                    return final_answer_bin
                else:
                    #print('mod=',dec_data % module)#更正後餘數
                    #print('R=',R)#更正前餘數
                    print('Error cannot be detected.')
                    #print('databin=',databin)
                    return databin
        else:                                   #超過範圍直接輸出
                #print('R=',R)
                print('Error cannot be detected')
                #print('databin=',databin)
                return databin
####----------------------#### direction: 1->LH ,others->HL # Bug, No USE!
def CorrectUni(bit,data,module,Ra_array,Ta_array,direction):
    if direction == 1:
        R=data % module
        print('\n----------CorrectLH----------')
    else:
        R=module-(data % module)
        print('\n----------CorrectHL----------')
    for i in range(1,bit):
        databin=Dec2Bin(bit, data)
        bitint=int(bit)
        #if no int(bit) #when bit=36, 2^bit=0
        #I do not know why.
        pow2Bit=pow(2,bitint)
        if data < pow2Bit:              
            if(R==0):
                final_answer=int(data/module)
                final_answer_bin=Dec2Bin(bit, final_answer)
                print('There is no error.')
                #print('final_answer_bin=',final_answer_bin)
                return final_answer_bin
            elif R in Ra_array:   
                errorbit=Ta_array[R]
                print('Error is in',errorbit,'bit')
                #print('It was\n',databin)
                errorbit_computer=bit-(errorbit+1)
                if databin[errorbit_computer]==1:
                    databin[errorbit_computer]=0
                else:
                    databin[errorbit_computer]=1
                #print("更改後\n",databin)
                dec_data=Bin2Dec(bit, databin)
                #print(dec_data)
                #############################
                if(dec_data % module==0):
                    final_answer=int(dec_data/module)
                    print('final_answer=',final_answer)
                    final_answer_bin=Dec2Bin(bit, final_answer)
                    return final_answer_bin
                else:
                    #print('mod=',dec_data % module)#更正後餘數
                    #print('R=',R)#更正前餘數
                    print('Error cannot be detected.')
                    #print('databin=',databin)
                    return databin
        else:                                   #超過範圍直接輸出
                #print('R=',R)
                print('---Error cannot be detected')
                #print('databin=',databin)
                return databin
####----------------------####
def CorrectLH(bit,data,module,Ra_array,Ta_array):
    R=data % module
    print('\n----------CorrectLH----------')
    for i in range(1,bit):
        databin=Dec2Bin(bit, data)
        bitint=int(bit)
        #if no int(bit) #when bit=36, 2^bit=0
        #I do not know why.
        pow2Bit=pow(2,bitint)
        if data < pow2Bit:              
            if(R==0):
                final_answer=int(data/module)
                final_answer_bin=Dec2Bin(bit, final_answer)
                print('There is no error.')
                #print('final_answer_bin=',final_answer_bin)
                return final_answer_bin
            elif R in Ra_array:   
                errorbit=Ta_array[R]
                print('Error is in',errorbit,'bit')
                #print('It was\n',databin)
                errorbit_computer=bit-(errorbit+1)
                if databin[errorbit_computer]==1:
                    databin[errorbit_computer]=0
                else:
                    databin[errorbit_computer]=1
                #print("更改後\n",databin)
                dec_data=Bin2Dec(bit, databin)
                #print(dec_data)
                #############################
                if(dec_data % module==0):
                    final_answer=int(dec_data/module)
                    print('final_answer=',final_answer)
                    final_answer_bin=Dec2Bin(bit, final_answer)
                    return final_answer_bin
                else:
                    #print('mod=',dec_data % module)#更正後餘數
                    #print('R=',R)#更正前餘數
                    print('Error cannot be detected.')
                    #print('databin=',databin)
                    return databin
        else:                                   #超過範圍直接輸出
                #print('R=',R)
                print('---Error cannot be detected')
                #print('databin=',databin)
                return databin
####----------------------####
def CorrectHL(bit,data,module,Ra_array,Ta_array):
    Re=data % module
    #print('餘數=',Re)
    R=module -  Re
    #print('模數-餘數=',R)
    print('\n----------CorrectHL----------')
    for i in range(1,bit):
        databin=Dec2Bin(bit, data)
        #print('data=',data)
        #print('bit=',bit)
        bitint=int(bit)
        #if no int(bit) #when bit=36, 2^bit=0
        #I do not know why.
        pow2Bit=pow(2,bitint)
        #print('2**bit=',pow2Bit)
        if data < pow2Bit:              
            if(R==0):
                final_answer=int(data/module)
                final_answer_bin=Dec2Bin(bit, final_answer)
                print('There is no error.')
                #print('final_answer_bin=',final_answer_bin)
                return final_answer_bin
            elif R in Ra_array:   
                errorbit=Ta_array[R]
                print('Error is in',errorbit,'bit')
                #print('It was\n',databin)
                errorbit_computer=bit-(errorbit+1)
                if databin[errorbit_computer]==1:
                    databin[errorbit_computer]=0
                else:
                    databin[errorbit_computer]=1
                #print("更改後\n",databin)
                dec_data=Bin2Dec(bit, databin)
                #print(dec_data)
                #############################
                if(dec_data % module==0):
                    final_answer=int(dec_data/module)
                    print('final_answer=',final_answer)
                    final_answer_bin=Dec2Bin(bit, final_answer)
                    return final_answer_bin
                else:
                    #print('mod=',dec_data % module)#更正後餘數
                    #print('R=',R)#更正前餘數
                    print('Error cannot be detected.')
                    #print('databin=',databin)
                    return databin
        else:                                   #超過範圍直接輸出
                #print('R=',R)
                print('---Error cannot be detected---')
                #print('databin=',databin)
                return databin
####------------------txt-or-verilog-------------------------#### 
def AWE_veri(N,module,Ta_array,Sa_array):
    fver= time.strftime("%Y%m%d_%H%M", time.localtime())
    AWEFolder='files\\AWE_'+fver
    Path=autoCreatFolder(AWEFolder)
    module_str=str(module)
    Nstr=str(N)
    Pathlist=Path.split('\\')
    lenPath=len(Pathlist)
    Rpath='./'+Pathlist[lenPath-2]+'/'+Pathlist[lenPath-1]
    fn=Rpath+'/ANdecoder_AWE_'+module_str+'_for_N_'+Nstr+'.v'
    bitIN=int((module-1)/2)      #可更正bit數
    bitMod=len(bin(module)[2:])  #mod的bit數
    bit1=bitIN*2 # and gate output +1 output
    bitN=bitIN-bitMod
    print('---------------開始寫檔案---------------')
    print('可更正AN的bit數=',bitIN,'\nmod的bit數=',bitMod,'\nand gate數=',bit1,'\n可更正N的bit數=',bitN)
    f = open(fn, "w")
    f.write("// File Name: %s/ANdecoder_AWE_%s_for_N_%s.v\n"%(Rpath,module_str,Nstr))
    f.write("// module= %d\n// 可更正AN的bit數= %d\n// mod的bit數= %d\n// 可更正N的bit數= %d\n"%(module,bitIN,bitMod,bitN))
    f.write("\nmodule ANdecoder(numX, out);\n")
    f.write("input [%d:0] numX;\n"%(bitIN-1))
    if (bitN-1) == 0:
        f.write("output out;\n")
    else:
        f.write("output [%d:0] out;\n" %(bitN-1))  
    f.write("wire [%d:0] mod_tri;\n"%(bitMod-1))
    f.write("wire [%d:0] not_mod_tri;\n"%(bitMod-1))
    f.write("wire [%d:0] error_bit;\n"%(bitIN-1))
    f.write("wire [%d:0] and_out;\n"%(bit1-1))
    f.write("wire add;\n" )
    
    f.write("wire [%d:0] AN;\n"%(bitIN-1))
    # mod R
    f.write("\nassign mod_tri = numX %% %d;\n"%module)
    #Inv
    f.write("\n//not gate")
    for j in range(0,bitMod):
        f.write("\nnot not_%d(not_mod_tri[%d], mod_tri[%d]);"%(j,j,j) )
    #And
    f.write("\n//and gate")
    for k in range(1,module):
       iLen=len(str(bin(module)[2:]))
       f.write("\nand and_%d("%k)
       f.write("and_out[%d], "%(k-1))
       k2=bin(k)[2:]
       k2_0=k2.zfill(iLen)
       ############
       k2_arr=list(str(k2_0))
       k2_arr.reverse()
       k2Tran=[]
       for x in range(0, iLen):
           if k2_arr[x] == '1' :
                k2Tran.append('mod_tri[%d],'%x)
           else :
                k2Tran.append('not_mod_tri[%d],'%x)
       k2Tran2=" ".join(k2Tran)
       k2Tran3=k2Tran2[:-1]
       f.write("%s);"%k2Tran3)
       ##############
    #Or
    f.write("\n//or gate")
    err2=[0]*bitIN
    for y in range(0,bitIN):
        f.write("\nor or_%d(error_bit[%d], "%(y,y))
        orList=[]
        err1=[] #-1 =>S=1
        for t in range(1,module):
            #and gate編碼從0開始
            if  Ta_array[t] == y:
                 orList.append('and_out[%d],'%(t-1))
                 orList2=" ".join(orList)
                 if  Sa_array[t] == 1:
                #bit對應   #順序其實沒差              
                     err2[y]=(t-1)
        orList3=orList2[:-1]
        f.write("%s);"%orList3)
    #Or=>-1 => output=1 => +errbit ; if not => -errbit
    f.write("\nor or_%d(add, "%bitIN)
    for ebit in range(0,bitIN): #0-5
        err1.append('and_out[%d],'%err2[ebit])
        err1_2=" ".join(err1)
    err1t=err1_2[:-1]
    f.write("%s);"%err1t)        
    f.write("\n\nassign AN = (add==0) ? numX-error_bit : numX+error_bit;\n" )
    f.write("\nassign out = AN / %d;\n"%module)
    f.write("\nendmodule")
    f.close()
    #tb
    fn2=Rpath+'/ANdecoder_AWE_'+module_str+'_tb_for_N_'+Nstr+'.v'
    f2 = open(fn2, "w")
    f2.write("// File Name: %s\n"%fn2)
    f2.write("// module= %d\n// N= %d\n"%(module,N))
    f2.write("\nmodule ANdecoder_tb;\n")
    f2.write("reg [%d:0] numX;\n"%(bitIN-1))
    if (bitN-1) == 0:
        f2.write("wire out;\n")
    else:
        f2.write("wire [%d:0] out;\n" %(bitN-1))
    f2.write("\nANdecoder D0(numX, out);\ninitial begin\n")
    f2.write("$dumpfile(\"%s/A%dN%d.vcd\"); \n$dumpvars(0, ANdecoder_tb);\n"%(Rpath,module,N))  
    f2.write("\nnumX=%d'd0;\n"%bitIN)
    #error
    print('\n---------------開始生成tb所需的Data---------------')
    for t1 in range(0,5):
        print('\n###Data %d 生成###'%(t1+1))
        #tN=np.random.randint(0,2**bitN)
        tANe,tANe2,tebit=errorGenTwo(bitIN,module,N)
        #tebitp=bitIN-(tebit+1) #人看的bit
        #取R
        #R=tANe%module
        #f2.write("\n//ANe=%d, R=%d, ebit=%d"%(tANe,R,tebitp))
        f2.write("#10 numX=%d'd%d;\n"%(bitIN,tANe))
    f2.write("\n#10 $finish;\nend\nendmodule\n")
    f2.close()
    print('\n---------------寫檔案完成---------------')
    print('%s has been generated.\n'%fn)
    print('%s has been generated.\n'%fn2) 
    fvcd=Path+'\\A'+module_str+'N'+Nstr+'.vcd'
    fo=Path+'\\A'+module_str+'N'+Nstr+'.out'
    return fn,fn2,fvcd,fo
####----------------------####
def BER_veri(N,module,Ta_array,Sa_array):
    fver= time.strftime("%Y%m%d_%H%M", time.localtime())
    BERFolder='files\\BER_'+fver
    Path=autoCreatFolder(BERFolder)
    module_str=str(module)
    Nstr=str(N)
    Pathlist=Path.split('\\')
    lenPath=len(Pathlist)
    Rpath='./'+Pathlist[lenPath-2]+'/'+Pathlist[lenPath-1]
    fn=Rpath+'/ANdecoder_BER_'+module_str+'_for_N_'+Nstr+'.v'
    bitIN=int((module-1)/2)      #可更正bit數
    bitMod=len(bin(module)[2:])  #mod的bit數
    bit1=bitIN*2 # and gate output +1 output
    bitN=bitIN-bitMod
    print('---------------開始寫檔案---------------')
    print('可更正AN的bit數=',bitIN,'\nmod的bit數=',bitMod,'\nand gate數=',bit1,'\n可更正N的bit數=',bitN)
    f = open(fn, "w")
    f.write("// File Name: %s\n"%fn)
    f.write("// module= %d\n// 可更正AN的bit數= %d\n// mod的bit數= %d\n// 可更正N的bit數= %d\n"%(module,bitIN,bitMod,bitN))
    f.write("\nmodule ANdecoder(numX, out);\n")
    f.write("input [%d:0] numX;\n"%(bitIN-1))
    if (bitN-1) == 0:
        f.write("output out;\n")
    else:
        f.write("output [%d:0] out;\n" %(bitN-1))
    f.write("wire [%d:0] mod_tri;\n"%(bitMod-1))
    f.write("wire [%d:0] not_mod_tri;\n"%(bitMod-1))
    f.write("wire [%d:0] error_bit;\n"%(bitIN-1))
    f.write("wire [%d:0] and_out;\n"%(bit1-1))
    
    f.write("wire [%d:0] AN;\n"%(bitIN-1))
    
    # mod R
    f.write("\nassign mod_tri = numX %% %d;\n"%module)
    #Inv
    f.write("\n//not gate")
    for j in range(0,bitMod):
        f.write("\nnot not_%d(not_mod_tri[%d], mod_tri[%d]);"%(j,j,j) )
    #And
    f.write("\n//and gate")
    for k in range(1,module):
       iLen=len(str(bin(module)[2:]))
       f.write("\nand and_%d("%k)
       f.write("and_out[%d], "%(k-1))
       k2=bin(k)[2:]
       k2_0=k2.zfill(iLen)
       ############
       k2_arr=list(str(k2_0))
       k2_arr.reverse()
       k2Tran=[]
       for x in range(0, iLen):
           if k2_arr[x] == '1' :
                k2Tran.append('mod_tri[%d],'%x)
           else :
                k2Tran.append('not_mod_tri[%d],'%x)
       k2Tran2=" ".join(k2Tran)
       k2Tran3=k2Tran2[:-1]
       f.write("%s);"%k2Tran3)
       ##############
    #Or
    f.write("\n//or gate")
    err2=[0]*bitIN
    for y in range(0,bitIN):
        f.write("\nor or_%d(error_bit[%d], "%(y,y))
        orList=[]
        # err1=[] #-1 =>S=1
        for t in range(1,module):
            #and gate編碼從0開始
            if  Ta_array[t] == y:
                 orList.append('and_out[%d],'%(t-1))
                 orList2=" ".join(orList)
                 if  Sa_array[t] == 1:
                #bit對應   #順序其實沒差              
                     err2[y]=(t-1)
        orList3=orList2[:-1]
        f.write("%s);"%orList3)     
    f.write("\n//xor gate")
    for xo in range(0,bitIN):
        f.write('\nxor xor_%d(AN[%d],error_bit[%d],numX[%d]);'%(xo,xo,xo,xo))
    f.write("\nassign out = AN / %d;\n"%module)
    f.write("\nendmodule")
    f.close()  
    #tb
    fn2=Rpath+'/ANdecoder_BER_'+module_str+'_tb_for_N_'+Nstr+'.v'
    f2 = open(fn2, "w")
    f2.write("// File Name: %s\n"%fn2)
    f2.write("// module= %d\n// N= %d\n"%(module,N))
    f2.write("\nmodule ANdecoder_tb;\n")
    f2.write("reg [%d:0] numX;\n"%(bitIN-1))
    if (bitN-1) == 0:
        f2.write("wire out;\n")
    else:
        f2.write("wire [%d:0] out;\n" %(bitN-1))
    
    f2.write("\nANdecoder D0(numX, out);\ninitial begin\n")
    f2.write("$dumpfile(\"%s/A%dN%d.vcd\"); \n$dumpvars(0, ANdecoder_tb);\n"%(Rpath,module,N))  
    f2.write("\nnumX=%d'd0;\n"%bitIN)
    #error
    print('\n---------------開始生成tb所需的Data---------------')
    for t1 in range(0,5):
        print('\n###Data %d 生成###'%(t1+1))
        #tN=np.random.randint(0,2**bitN)
        tANe,tANe2,tebit=errorGenTwo(bitIN,module,N)
        #tebitp=bitIN-(tebit+1) #人看的bit
        #取R
        #R=tANe%module
        f2.write("\n#10 numX=%d'd%d;"%(bitIN,tANe))
    f2.write("\n#10 $finish;\nend\nendmodule\n")
    f2.close()
    print('\n---------------寫檔案完成---------------')
    print('%s has been generated.\n'%fn)
    print('%s has been generated.\n'%fn2) 
    fvcd=Path+'\\A'+module_str+'N'+Nstr+'.vcd'
    fo=Path+'\\A'+module_str+'N'+Nstr+'.out'
    return fn,fn2,fvcd,fo   
####----------------------####
def Alter_veri(N,module,Ta_array):
    fver= time.strftime("%Y%m%d_%H%M", time.localtime())
    AlterFolder='files\\Alter_'+fver
    Path=autoCreatFolder(AlterFolder)
    module_str=str(module)
    Nstr=str(N)
    Pathlist=Path.split('\\')
    lenPath=len(Pathlist)
    Rpath='./'+Pathlist[lenPath-2]+'/'+Pathlist[lenPath-1]
    fn=Rpath+'/ANdecoder_Alter_'+module_str+'_for_N_'+Nstr+'.v'
    bitIN=(module-1)     #可更正bit數
    bitMod=len(bin(module)[2:])  #mod的bit數
    bitN=bitIN-bitMod
    print('---------------開始寫檔案---------------')
    print('可更正AN的bit數=',bitIN,'\nmod的bit數=',bitMod,'\n可更正N的bit數=',bitN)
    f = open(fn, "w")
    f.write("// File Name: %s\n"%fn)
    f.write("// module= %d\n// 可更正AN的bit數= %d\n// mod的bit數= %d\n// 可更正N的bit數= %d\n"%(module,bitIN,bitMod,bitN))
    f.write("\nmodule ANdecoder(numX, out);\n")
    f.write("input [%d:0] numX;\n"%(bitIN-1))
    if (bitN-1) == 0:
        f.write("output out;\n")
    else:
        f.write("output [%d:0] out;\n" %(bitN-1))  
    
    f.write("wire [%d:0] mod_tri;\n"%(bitMod-1))
    f.write("wire [%d:0] not_mod_tri;\n"%(bitMod-1))
    #f.write("wire [%d:0] error_bit1;\n"%(bitIN-1))
    f.write("wire [%d:0] R;\n"%(bitIN-1))
    f.write("wire [%d:0] notR;\n"%(bitIN-1))
    f.write("wire [%d:0] out1;\n"%(bitIN-1))
    
    #f.write("wire [%d:0] error_bit2;\n"%(bitIN-1))
    f.write("wire [%d:0] out2;\n"%(bitIN-1))
    f.write("wire [%d:0] check;\n"%(bitMod-1))
    
    f.write("wire [%d:0] AN;\n" %(bitIN-1))    
    
    # mod R
    f.write("\nassign mod_tri = numX %% %d;\n"%module)
    # Inv
    f.write("\n//not0 gate")
    for j1 in range(0,bitMod):
        f.write("\nnot not0_%d(not_mod_tri[%d], mod_tri[%d]);"%(j1,j1,j1) )
    # And0
    #f.write("\n//and0 gate")
    #for k in range(1,module): #EX: i=13 => 1-12
    #   iLen=len(str(bin(module)[2:]))
    #   f.write("\nand and0_%d("%k)
    #   ebit=Ta_array[k]
    #   f.write("error_bit1[%d], "%ebit)
    #   k2=bin(k)[2:]
    #   k2_0=k2.zfill(iLen)
    #   k2_arr=list(str(k2_0))
    #   k2_arr.reverse()
    #   k2Tran=[]
    #   for x in range(0, iLen):
    #       if k2_arr[x] == '1' :
    #            k2Tran.append('mod_tri[%d],'%x)
    #       else :
    #            k2Tran.append('not_mod_tri[%d],'%x)
    #   k2Tran2=" ".join(k2Tran)
    #   k2Tran3=k2Tran2[:-1]
    #   f.write("%s);"%k2Tran3)
    
    # And
    f.write("\n//and gate")
    for k in range(1,module): #EX: i=13 => 1-12
       iLen=len(str(bin(module)[2:]))
       f.write("\nand and0_%d(R[%d], "%(k,(k-1)))
       ebit=Ta_array[k]
       #f.write("error_bit1[%d], "%ebit)
       k2=bin(k)[2:]
       k2_0=k2.zfill(iLen)
       k2_arr=list(str(k2_0))
       k2_arr.reverse()
       k2Tran=[]
       for x in range(0, iLen):
           if k2_arr[x] == '1' :
                k2Tran.append('mod_tri[%d],'%x)
           else :
                k2Tran.append('not_mod_tri[%d],'%x)
       k2Tran2=" ".join(k2Tran)
       k2Tran3=k2Tran2[:-1]
       f.write("%s);"%k2Tran3)
   
    # xor0 改成not+and
    #f.write("\n//XOR gate")
    #for x1 in range(0,bitIN):
        #f.write("\nxor xor_%d(out1[%d],error_bit1[%d], numX[%d]);"%(x1,x1,x1,x1) )
    #    ebit=Ta_array[(x1+1)]
    #    f.write("\nxor xor_%d(out1[%d],R[%d], numX[%d]);"%(x1,x1,ebit,x1) )
    

    # Not
    f.write("\n//not1 gate")
    for j0 in range(0,bitIN):
        f.write("\nnot not1_%d(notR[%d], R[%d]);"%(j0,j0,j0) ) 
    # And1 # R&numX對應
    f.write("\n//and1 gate")
    for j3 in range(0,bitIN):
        ebit=Ta_array[(j3+1)]
        f.write("\nand and1_%d(out1[%d], notR[%d], numX[%d]);"%(ebit,ebit,j3,ebit))
    # xor1 
    #0727 改or gate
    f.write("\n//or gate")
    for x1 in range(0,bitIN):
        xxx=module-(x1+1)
        ebit2=Ta_array[xxx]
        f.write("\nor or_%d(out2[%d], "%(ebit2,ebit2))
        f.write("R[%d], "%x1)
        f.write("numX[%d]);"%ebit2)
    
    f.write("\n//check")
    f.write("\nassign check = out1 %% %d;"%module)
    f.write("\nassign AN = (check == %d'd0) ? out1 : out2;"%bitMod)
    f.write("\nassign out = AN / %d;"%module)
    f.write("\nendmodule")
    f.close()    
    #tb
    fn2=Rpath+'/ANdecoder_Alter_'+module_str+'_tb_for_N_'+Nstr+'.v'
    f2 = open(fn2, "w")
    f2.write("// File Name: %s\n"%fn2)
    f2.write("// module= %d\n// N= %d\n"%(module,N))
    f2.write("\nmodule ANdecoder_tb;\n")
    f2.write("reg [%d:0] numX;\n"%(bitIN-1))
    if (bitN-1) == 0:
        f2.write("wire out;\n")
    else:
        f2.write("wire [%d:0] out;\n" %(bitN-1))
 
    f2.write("\nANdecoder D0(numX, out);\ninitial begin\n")
    f2.write("$dumpfile(\"%s/A%dN%d.vcd\"); \n$dumpvars(0, ANdecoder_tb);\n"%(Rpath,module,N))  
    f2.write("\nnumX=%d'd0;\n"%bitIN)
    #error
    print('\n---------------開始生成tb所需的Data---------------')
    for t1 in range(0,3):
        print('\n###Data %d 生成###'%(t1+1))
        f2.write("\n//error 0->1")
        tANe,tANe2,tebit=errorGenLH(bitIN,module,N)
        #tebitp=bitIN-(tebit+1) #人看的bit
        #取R
        #R=tANe%module
        f2.write("\n#10 numX=%d'd%d;"%(bitIN,tANe))
    for t2 in range(3,6):
        print('\n###Data %d 生成###'%(t2+1))
        f2.write("\n//error 1->0")
        tANe,tANe2,tebit=errorGenHL(bitIN,module,N)
        #取R
        #R=tANe%module
        f2.write("\n#10 numX=%d'd%d;"%(bitIN,tANe))
    
    f2.write("\n#10 $finish;\nend\nendmodule\n")
    f2.close()
    print('\n---------------寫檔案完成---------------')
    print('%s has been generated.\n'%fn)
    print('%s has been generated.\n'%fn2) 
    fvcd=Path+'\\A'+module_str+'N'+Nstr+'.vcd'
    fo=Path+'\\A'+module_str+'N'+Nstr+'.out'
    return fn,fn2,fvcd,fo
####----------------------####
def Uni_LH_veri(N,module,Ta_array):
    fver= time.strftime("%Y%m%d_%H%M", time.localtime())
    UniLHFolder='files\\Uni_LH_'+fver
    Path=autoCreatFolder(UniLHFolder)
    module_str=str(module)
    Nstr=str(N)
    Pathlist=Path.split('\\')
    lenPath=len(Pathlist)
    Rpath='./'+Pathlist[lenPath-2]+'/'+Pathlist[lenPath-1]
    fn=Rpath+'/ANdecoder_Uni_LH_'+module_str+'_for_N_'+Nstr+'.v'
    bitIN=module-1      #可更正bit數
    bitMod=len(bin(module)[2:])  #mod的bit數
    bitN=bitIN-bitMod
    print('---------------開始寫檔案---------------')
    print('可更正AN的bit數=',bitIN,'\nmod的bit數=',bitMod,'\n可更正N的bit數=',bitN)
    f = open(fn, "w")
    f.write("// File Name: %s\n"%fn)
    f.write("// module= %d\n// 可更正AN的bit數= %d\n// mod的bit數= %d\n// 可更正N的bit數= %d\n"%(module,bitIN,bitMod,bitN))
    f.write("\nmodule ANdecoder(numX, out);\n")
    f.write("input [%d:0] numX;\n"%(bitIN-1))
    if (bitN-1) == 0:
        f.write("output out;\n")
    else:
        f.write("output [%d:0] out;\n" %(bitN-1))
    f.write("wire [%d:0] mod_tri;\n"%(bitMod-1))
    f.write("wire [%d:0] not_mod_tri;\n"%(bitMod-1))
    f.write("wire [%d:0] error_bit;\n"%(bitIN-1))
    f.write("wire [%d:0] not_error_bit;\n"%(bitIN-1))
    f.write("wire [%d:0] AN;"%(bitIN-1))
    
    # mod R
    f.write("\nassign mod_tri = numX %% %d;\n"%module)
    #Inv
    f.write("\n//not0 gate")
    for j1 in range(0,bitMod):
        f.write("\nnot not0_%d(not_mod_tri[%d], mod_tri[%d]);"%(j1,j1,j1) )
    #And
    f.write("\n//and0 gate")
    for k in range(1,module): #EX: i=13 => 1-12
       iLen=len(str(bin(module)[2:]))
       f.write("\nand and0_%d("%k)
       ebit=Ta_array[k]
       f.write("error_bit[%d], "%ebit)
       k2=bin(k)[2:]
       k2_0=k2.zfill(iLen)
       k2_arr=list(str(k2_0))
       k2_arr.reverse()
       k2Tran=[]
       for x in range(0, iLen):
           if k2_arr[x] == '1' :
                k2Tran.append('mod_tri[%d],'%x)
           else :
                k2Tran.append('not_mod_tri[%d],'%x)
       k2Tran2=" ".join(k2Tran)
       k2Tran3=k2Tran2[:-1]
       f.write("%s);"%k2Tran3)
    # xor
    #f.write("\n//XOR gate")
    #for x1 in range(0,bitIN):
    #    f.write("\nxor xor_%d(AN[%d],error_bit[%d], numX[%d]);"%(x1,x1,x1,x1) )
    
    # not
    f.write("\n//not1 gate")
    for x1 in range(0,bitIN):
        f.write("\nnot not1_%d(not_error_bit[%d],error_bit[%d]);"%(x1,x1,x1) )
    # and
    f.write("\n//and1 gate")
    for x2 in range(0,bitIN):
        f.write("\nand and1_%d(AN[%d],not_error_bit[%d], numX[%d]);"%(x2,x2,x2,x2) )
    f.write("\n\nassign out = AN / %d;\n"%module)
    f.write("\nendmodule")
    f.close()
    #tb
    fn2=Rpath+'/ANdecoder_Uni_LH_'+module_str+'_tb_for_N_'+Nstr+'.v'
    f2 = open(fn2, "w")
    f2.write("// File Name: %s\n"%fn2)
    f2.write("// module= %d\n// N= %d\n"%(module,N))
    f2.write("\nmodule ANdecoder_tb;\n")
    f2.write("reg [%d:0] numX;\n"%(bitIN-1))
    if (bitN-1) == 0:
        f2.write("wire out;\n")
    else:
        f2.write("wire [%d:0] out;\n" %(bitN-1))
    f2.write("\nANdecoder D0( numX, out);\ninitial begin\n")
    f2.write("$dumpfile(\"%s/A%dN%d.vcd\"); \n$dumpvars(0, ANdecoder_tb);\n"%(Rpath,module,N))  
    f2.write("\nnumX=%d'd0;\n"%bitIN)
    #error
    print('\n---------------開始生成tb所需的Data---------------')
    for t1 in range(0,5):
        print('\n###Data %d 生成###'%(t1+1))
        #tN=np.random.randint(0,2**bitN)
        tANe,tANe2,tebit=errorGenLH(bitIN,module,N)
        #tebitp=bitIN-(tebit+1) #人看的bit
        #取R
        #R=tANe%module
        f2.write("\n#10 numX=%d'd%d;"%(bitIN,tANe))
    f2.write("\n#10 $finish;\nend\nendmodule\n")
    f2.close()
    print('\n---------------寫檔案完成---------------')
    print('%s has been generated.\n'%fn)
    print('%s has been generated.\n'%fn2) 
    fvcd=Path+'\\A'+module_str+'N'+Nstr+'.vcd'
    fo=Path+'\\A'+module_str+'N'+Nstr+'.out'
    return fn,fn2,fvcd,fo
####---------------------------------------------------------####
def Uni_HL_veri(N,module,Ta_array):
    fver= time.strftime("%Y%m%d_%H%M", time.localtime())
    UniHLFolder='files\\Uni_HL_'+fver
    Path=autoCreatFolder(UniHLFolder)
    module_str=str(module)
    Nstr=str(N)
    Pathlist=Path.split('\\')
    lenPath=len(Pathlist)
    Rpath='./'+Pathlist[lenPath-2]+'/'+Pathlist[lenPath-1]
    fn=Rpath+'/ANdecoder_Uni_HL_'+module_str+'_for_N_'+Nstr+'.v'
    bitIN=module-1      #可更正bit數
    bitMod=len(bin(module)[2:])  #mod的bit數
    bitN=bitIN-bitMod
    print('---------------開始寫檔案---------------')
    print('可更正AN的bit數=',bitIN,'\nmod的bit數=',bitMod,'\n可更正N的bit數=',bitN)
    f = open(fn, "w")
    f.write("// File Name: %s\n"%fn)
    f.write("// module= %d\n// 可更正AN的bit數= %d\n// mod的bit數= %d\n// 可更正N的bit數= %d\n"%(module,bitIN,bitMod,bitN))
    f.write("\nmodule ANdecoder(numX, out);\n")
    f.write("input [%d:0] numX;\n"%(bitIN-1))
    if (bitN-1) == 0:
        f.write("output out;\n")
    else:
        f.write("output [%d:0] out;\n" %(bitN-1))
    f.write("wire [%d:0] mod_tri;\n"%(bitMod-1))
    f.write("wire [%d:0] not_mod_tri;\n"%(bitMod-1))
    f.write("wire [%d:0] error_bit;\n"%(bitIN-1))
    
    f.write("wire [%d:0] AN;"%(bitIN-1))
    
    # mod R
    f.write("\nassign mod_tri = numX %% %d;\n"%module)
    #Inv
    f.write("\n//not gate")
    for j1 in range(0,bitMod):
        f.write("\nnot not_%d(not_mod_tri[%d], mod_tri[%d]);"%(j1,j1,j1) )
    #And
    f.write("\n//and gate")
    for k in range(1,module): #EX: i=13 => 1-12
       iLen=len(str(bin(module)[2:]))
       f.write("\nand and_%d("%k)
       ebit=Ta_array[(module-k)]
       f.write("error_bit[%d], "%ebit)
       k2=bin(k)[2:]
       k2_0=k2.zfill(iLen)
       k2_arr=list(str(k2_0))
       k2_arr.reverse()
       k2Tran=[]
       for x in range(0, iLen):
           if k2_arr[x] == '1' :
                k2Tran.append('mod_tri[%d],'%x)
           else :
                k2Tran.append('not_mod_tri[%d],'%x)
       k2Tran2=" ".join(k2Tran)
       k2Tran3=k2Tran2[:-1]
       f.write("%s);"%k2Tran3)
    # xor #0727 改成or gate(驗證成功)
    f.write("\n//or gate")
    for x1 in range(0,bitIN):
        f.write("\nor or_%d(AN[%d],error_bit[%d], numX[%d]);"%(x1,x1,x1,x1) )
    f.write("\nassign out = AN / %d;\n"%module)
    f.write("\nendmodule")
    f.close()
    #tb
    fn2=Rpath+'/ANdecoder_Uni_HL_'+module_str+'_tb_for_N_'+Nstr+'.v'
    f2 = open(fn2, "w")
    f2.write("// File Name: %s\n"%fn2)
    f2.write("// module= %d\n// N= %d\n"%(module,N))
    f2.write("\nmodule ANdecoder_tb;\n")
    f2.write("reg [%d:0] numX;\n"%(bitIN-1))
    if (bitN-1) == 0:
        f2.write("wire out;\n")
    else:
        f2.write("wire [%d:0] out;\n" %(bitN-1))
    f2.write("\nANdecoder D0(numX, out);\ninitial begin\n")
    f2.write("$dumpfile(\"%s/A%dN%d.vcd\"); \n$dumpvars(0, ANdecoder_tb);\n"%(Rpath,module,N))  
    f2.write("\nnumX=%d'd0;\n"%bitIN)
    #error
    print('\n---------------開始生成tb所需的Data---------------')
    for t1 in range(0,5):
        print('\n###Data %d 生成###'%(t1+1))
        #tN=np.random.randint(0,2**bitN)
        tANe,tANe2,tebit=errorGenHL(bitIN,module,N)
        #tebitp=bitIN-(tebit+1) #人看的bit
        #取R
        #R=tANe%module
        f2.write("\n#10 numX=%d'd%d;"%(bitIN,tANe))
    f2.write("\n#10 $finish;\nend\nendmodule\n")
    f2.close()
    print('\n---------------寫檔案完成---------------')
    print('%s has been generated.\n'%fn)
    print('%s has been generated.\n'%fn2) 
    fvcd=Path+'\\A'+module_str+'N'+Nstr+'.vcd'
    fo=Path+'\\A'+module_str+'N'+Nstr+'.out'
    return fn,fn2,fvcd,fo
####------------------iverilog-------------------------------####
def autoVCD(fn,ftb,fvcd,fo):
    os.system('iverilog -o %s %s %s'%(fo,fn,ftb))
    os.system('vvp -n %s'%fo)
    os.system('gtkwave -T auto.tcl %s'%fvcd)
####---------------------------------------------------------####
def autoCreatFolder(newFolder):
    path = os.path.abspath('.')
    newPath = path + '\\' + newFolder
    if not os.path.isdir(newPath):
        os.mkdir(newPath)
    return newPath
######
n=1
VerilogFolder = 'files'
autoCreatFolder(VerilogFolder)

while n > 0:
    DescriptionA='Ex: The length of the number entered = 4 bit\n\t以AWE mode 來舉例: Mode 1=> A=19, 可更正4bit的N\n\t\t\t   Mode 2=> A=29, 可更正9bit的N'
    print(DescriptionA)
    selA=input('mode 1 ---> Find an available A\nmode 2 ---> Find the most appropriate A\nPlease select a mode:')
    if selA == 'exit':
        print('\nExit the program.')
        break
    elif selA.isdigit():
        selA=int(selA)
    else:
        print('\nPlease re-select mode!')
    rang2=100
    '''
    # Choose the range of A: 1~range2
    
    #rang2=input('Please enter the range of A:')
    #if rang2.isdigit():
    #    rang2=int(rang2)
    #else:
    #    print('\nSomething went wrong!')
    #    print('Please re-select mode!')
    #    continue
    '''
    if selA == 1:
        Two_A,Two_cbit_N,One_A,One_cbit_N=FindA(1,rang2)
        Description_Error_Model='''\nmodel 1 ---> Unidirectional Fully Asymmetric Channel model
model 2 ---> Alternative-direction Fully Asymmetric Channel model
model 3 ---> BER model\nmodel 4 ---> AWE model'''
        print(Description_Error_Model)
        selMode=input('Choose model:')
        if selMode == 'exit':
            print('\nExit the program.\n')
            break
        elif selMode.isdigit():
            selMode=int(selMode)
        else:
            print('Please re-select model!\n')
            continue
        #Uni FAC: Error will only occur in unidirectional.
        if selMode == 1:
            N1,findA_One1,cbitN_One1=AutoFindA(1,One_A,One_cbit_N)
            Ra_array1,Ta_array1=TableOne(findA_One1)
            #error
            direction1=int(input('1.LH 2.HL \ndirection:'))
            bitAN1=cbitN_One1+len(bin(findA_One1)[2:])
            if direction1 == 1:
                ANe1,ANe1_2,ebit1=errorGenLH(bitAN1,findA_One1,N1)
            elif direction1 == 2:
                ANe1,ANe1_2,ebit1=errorGenHL(bitAN1,findA_One1,N1)
            else:
                print('No this mode!')
                continue
            #correct
            if direction1 == 1:
                correct1_2=CorrectLH(bitAN1,ANe1,findA_One1,Ra_array1,Ta_array1)
            else:
                correct1_2=CorrectHL(bitAN1,ANe1,findA_One1,Ra_array1,Ta_array1)
                
            correct1=Bin2Dec(bitAN1, correct1_2)
            if correct1 == N1:
                print('\nCorrect ^_^\n')
            else:
                print('\nFail~ q_q\n')
            #txt
            wr_txt1=int(input('Write the verilog file or not?\n 1---> Yes.\n 2---> No.\nPlease select:'))
            if wr_txt1 == 1:
                if direction1 == 1:
                    fn,fn2,fvcd,fo=Uni_LH_veri(N1,findA_One1,Ta_array1)
                else:
                    fn,fn2,fvcd,fo=Uni_HL_veri(N1,findA_One1,Ta_array1)
            else:
                print('---It won\'t write any files.---')
                break
            #auto VCD
            print('---------Auto Verification---------')
            autoVCD(fn,fn2,fvcd,fo)
            print('The file has been authenticated.')
            break
        #Alter FAC: You can‘t know in advance which is error’s direction.
        elif selMode == 2:
            N,findA_One,cbitN_One=AutoFindA(1,One_A,One_cbit_N)
            Ra_array,Ta_array=TableOne(findA_One)
            #error
            direction=np.random.randint(1,3)
            bitAN=cbitN_One+len(bin(findA_One)[2:])
            if direction == 1:
                ANe,ANe2,ebit=errorGenLH(bitAN,findA_One,N)
            elif direction == 2:
                ANe,ANe2,ebit=errorGenHL(bitAN,findA_One,N)
            else:
                print('No this mode!')
                continue
            #correct
            correct2=CorrectUni(bitAN,ANe,findA_One,Ra_array,Ta_array,direction)
            correct=Bin2Dec(bitAN, correct2)
            if correct == N:
                print('\nCorrect ^_^\n')
            else:
                print('\nFail~ q_q\n')
            #txt
            wr_txt=int(input('Write the verilog file or not?\n 1---> Yes.\n 2---> No.\nPlease select:'))
            if wr_txt == 1:
                fn,fn2,fvcd,fo=Alter_veri(N,findA_One,Ta_array)
            else:
                print('---It won\'t write any files.---')
                break
            #auto VCD
            print('---------Auto Verification---------')
            autoVCD(fn,fn2,fvcd,fo)
            print('The file has been authenticated.')
            break
        #BER
        elif selMode == 3:
            N,findA_Two,cbitN_Two=AutoFindA(1,Two_A,Two_cbit_N)
            Ra_array,Ta_array,Sa_array=TableTwo(findA_Two)
            #error
            bitAN=cbitN_Two+len(bin(findA_Two)[2:])
            ANe,ANe2,ebit=errorGenTwo(bitAN,findA_Two,N)
            #correct
            correct2=CorrectTwo(bitAN,ANe,findA_Two,Ra_array,Ta_array,Sa_array)
            correct=Bin2Dec(bitAN, correct2)
            if correct == N:
                print('\nCorrect ^_^\n')
            else:
                print('\nFail~ q_q\n')
            #txt
            wr_txt=int(input('Write the verilog file or not?\n 1---> Yes.\n 2---> No.\nPlease select:'))
            if wr_txt == 1:
                fn,fn2,fvcd,fo=BER_veri(N,findA_Two,Ta_array,Sa_array)
            else:
                print('---It won\'t write any files.---')
                break
            #auto VCD
            print('---------Auto Verification---------')
            autoVCD(fn,fn2,fvcd,fo)
            print('The file has been authenticated.')
            break
        #AWE: The error maybe come from addition or subtraction.
        elif selMode == 4:
            N,findA_Two,cbitN_Two=AutoFindA(1,Two_A,Two_cbit_N)
            Ra_array,Ta_array,Sa_array=TableTwo(findA_Two)
            #error
            bitAN=cbitN_Two+len(bin(findA_Two)[2:])
            ANe,ANe2,ebit=errorGenTwo(bitAN,findA_Two,N)
            #correct
            correct2=CorrectTwo(bitAN,ANe,findA_Two,Ra_array,Ta_array,Sa_array)
            correct=Bin2Dec(bitAN, correct2)
            if correct == N:
                print('\nCorrect ^_^\n')
            else:
                print('\nFail~ q_q\n')
            #txt
            wr_txt=int(input('Write the verilog file or not?\n 1---> Yes.\n 2---> No.\nPlease select:'))
            if wr_txt == 1:
                fn,fn2,fvcd,fo=AWE_veri(N,findA_Two,Ta_array,Sa_array)
            else:
                print('---It won\'t write any files.---')
                break
            #auto VCD
            print('---------Auto Verification---------')
            autoVCD(fn,fn2,fvcd,fo)
            print('The file has been authenticated.')
            break
        else:
            print('\nNo this mode!\nExit the program.\n')
            break
        ################################################# 
    elif selA == 2:
        Two_A_most,Two_A_most_cbitN,One_A_most,One_A_most_cbitN=FindA(2,rang2)
        Description_Error_Model='''\nmodel 1 ---> Uni-direction Fully Asymmetric Channel model
model 2 ---> Alternative-direction Fully Asymmetric Channel model
model 3 ---> BER model\nmodel 4 ---> AWE model'''
        print(Description_Error_Model)
        selMode=input('Choose model:')
        if selMode == 'exit':
            print('\nExit the program.\n')
            break
        elif selMode.isdigit():
            selMode=int(selMode)
        else:
            print('Please re-select model!\n')
            continue
        #Uni FAC
        if selMode == 1:
            N,findA_One,cbitN_One=AutoFindA(1,One_A_most,One_A_most_cbitN)
            Ra_array,Ta_array=TableOne(findA_One)
            #error
            direction=int(input('1.LH 2.HL \ndirection:'))
            bitAN=cbitN_One+len(bin(findA_One)[2:])
            if direction == 1:
                ANe,ANe2,ebit=errorGenLH(bitAN,findA_One,N)
            elif direction == 2:
                ANe,ANe2,ebit=errorGenHL(bitAN,findA_One,N)
            else:
                print('No this mode!')
                continue
            #correct
            if direction == 1:
                correct2=CorrectLH(bitAN,ANe,findA_One,Ra_array,Ta_array)
            else:
                correct2=CorrectHL(bitAN,ANe,findA_One,Ra_array,Ta_array)
            correct=Bin2Dec(bitAN, correct2)
            if correct == N:
                print('\nCorrect ^_^\n')
            else:
                print('\nFail~ q_q\n')
            #txt
            wr_txt=int(input('Write the verilog file or not?\n 1---> Yes.\n 2---> No.\nPlease select:'))
            if wr_txt == 1:
                if direction == 1:
                    fn,fn2,fvcd,fo=Uni_LH_veri(N,findA_One,Ta_array)
                else:
                    fn,fn2,fvcd,fo=Uni_HL_veri(N,findA_One,Ta_array)
            else:
                print('---It won\'t write any files.---')
                break
            #auto VCD
            print('---------Auto Verification---------')
            autoVCD(fn,fn2,fvcd,fo)
            print('The file has been authenticated.')
            break
        #Alter FAC
        elif selMode == 2:
            N,findA_One,cbitN_One=AutoFindA(1,One_A_most,One_A_most_cbitN)
            Ra_array,Ta_array=TableOne(findA_One)
            #error
            direction=np.random.randint(1,3)
            bitAN=cbitN_One+len(bin(findA_One)[2:])
            if direction == 1:
                ANe,ANe2,ebit=errorGenLH(bitAN,findA_One,N)
            elif direction == 2:
                ANe,ANe2,ebit=errorGenHL(bitAN,findA_One,N)
            else:
                print('No this mode!')
                continue
            #correct
            correct2=CorrectUni(bitAN,ANe,findA_One,Ra_array,Ta_array,direction)
            correct=Bin2Dec(bitAN, correct2)
            if correct == N:
                print('\nCorrect ^_^\n')
            else:
                print('\nFail~ q_q\n')
            #txt
            wr_txt=int(input('Write the verilog file or not?\n 1---> Yes.\n 2---> No.\nPlease select:'))
            if wr_txt == 1:
                fn,fn2,fvcd,fo=Alter_veri(N,findA_One,Ta_array)
            else:
                print('---It won\'t write any files.---')
                break
            #auto VCD
            print('---------Auto Verification---------')
            autoVCD(fn,fn2,fvcd,fo)
            print('The file has been authenticated.')
            break
        #BER
        elif selMode == 3:
            N,findA_Two,cbitN_Two=AutoFindA(1,Two_A_most,Two_A_most_cbitN)
            Ra_array,Ta_array,Sa_array=TableTwo(findA_Two)
            #error
            bitAN=cbitN_Two+len(bin(findA_Two)[2:])
            ANe,ANe2,ebit=errorGenTwo(bitAN,findA_Two,N)
            #correct
            correct2=CorrectTwo(bitAN,ANe,findA_Two,Ra_array,Ta_array,Sa_array)
            correct=Bin2Dec(bitAN, correct2)
            if correct == N:
                print('\nCorrect ^_^\n')
            else:
                print('\nFail~ q_q\n')
            #txt
            wr_txt=int(input('Write the verilog file or not?\n 1---> Yes.\n 2---> No.\nPlease select:'))
            if wr_txt == 1:
                fn,fn2,fvcd,fo=BER_veri(N,findA_Two,Ta_array,Sa_array)
            else:
                print('---It won\'t write any files.---')
                break
            #auto VCD
            print('---------Auto Verification---------')
            autoVCD(fn,fn2,fvcd,fo)
            print('The file has been authenticated.')
            break
        #AWE
        elif selMode == 4:
            N,findA_Two,cbitN_Two=AutoFindA(1,Two_A_most,Two_A_most_cbitN)
            Ra_array,Ta_array,Sa_array=TableTwo(findA_Two)
            #error
            bitAN=cbitN_Two+len(bin(findA_Two)[2:])
            ANe,ANe2,ebit=errorGenTwo(bitAN,findA_Two,N)
            #correct
            correct2=CorrectTwo(bitAN,ANe,findA_Two,Ra_array,Ta_array,Sa_array)
            correct=Bin2Dec(bitAN, correct2)
            if correct == N:
                print('\nCorrect ^_^\n')
            else:
                print('\nFail~ q_q\n')
            #txt
            wr_txt=int(input('Write the verilog file or not?\n 1---> Yes.\n 2---> No.\nPlease select:'))
            if wr_txt == 1:
                fn,fn2,fvcd,fo=AWE_veri(N,findA_Two,Ta_array,Sa_array)
            else:
                print('---It won\'t write any files.---')
                break
            #auto VCD
            print('---------Auto Verification---------')
            autoVCD(fn,fn2,fvcd,fo)
            print('The file has been authenticated.')
            break
        
        else:
            print('\nNo this mode!\nExit the program.\n')
            break

        #################################################   
    else:
        print('There don\'t have this mode.\n')
   
   
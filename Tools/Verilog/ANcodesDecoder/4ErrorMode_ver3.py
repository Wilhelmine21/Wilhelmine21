from ver3_def import *
n=1
show_correct_bit=1
rang2=100
# DescriptionA='Ex: The length of the number entered = 4 bit\n\t以AWE mode 來舉例: Mode 1=> A=19, 可更正4bit的N\n\t\t\t   Mode 2=> A=29, 可更正9bit的N'
Description_Error_Model='''\nmodel 1 ---> Uni-direction Fully Asymmetric Channel model
model 2 ---> Alternative-direction Fully Asymmetric Channel model
model 3 ---> BER model\nmodel 4 ---> AWE model'''
VerilogFolder = 'files'
autoCreatFolder(VerilogFolder)

while n > 0:
    # print(DescriptionA)
    Show_A_TEXT(rang2,show_correct_bit)
    selA=input('mode 1 ---> Find an available A\nmode 2 ---> Find the most appropriate A\nPlease select a mode:')
    if selA == 'exit':
        print('\nExit the program.')
        break
    elif selA.isdigit():
        selA=int(selA)
    else:
        print('\nPlease re-select mode!')

    if selA == 1:
        Two_A,Two_cbit_N,One_A,One_cbit_N=FindA(1,rang2)
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
            wr_txt1=int(input('Write the verilog file or not?\t(1---> Yes.  2---> No.)\nPlease select:'))
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
            autoVCD(fn,fn2,fvcd,fo,selMode)
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
            wr_txt=int(input('Write the verilog file or not?\t(1---> Yes.  2---> No.)\nPlease select:'))
            if wr_txt == 1:
                fn,fn2,fvcd,fo=Alter_veri(N,findA_One,Ta_array)
            else:
                print('---It won\'t write any files.---')
                break
            #auto VCD
            print('---------Auto Verification---------')
            autoVCD(fn,fn2,fvcd,fo,selMode)
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
            correct2=CorrectBER(bitAN,ANe,findA_Two,Ra_array,Ta_array,Sa_array)
            correct=Bin2Dec(bitAN, correct2)
            if correct == N:
                print('\nCorrect ^_^\n')
            else:
                print('\nFail~ q_q\n')
            #txt
            wr_txt=int(input('Write the verilog file or not?\t(1---> Yes.  2---> No.)\nPlease select:'))
            if wr_txt == 1:
                fn,fn2,fvcd,fo=BER_veri(N,findA_Two,Ta_array,Sa_array)
            else:
                print('---It won\'t write any files.---')
                break
            #auto VCD
            print('---------Auto Verification---------')
            autoVCD(fn,fn2,fvcd,fo,selMode)
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
            correct2=CorrectAWE(bitAN,ANe,findA_Two,Ra_array,Ta_array,Sa_array)
            correct=Bin2Dec(bitAN, correct2)
            if correct == N:
                print('\nCorrect ^_^\n')
            else:
                print('\nFail~ q_q\n')
            #txt
            wr_txt=int(input('Write the verilog file or not?\t(1---> Yes.  2---> No.)\nPlease select:'))
            if wr_txt == 1:
                fn,fn2,fvcd,fo=AWE_veri(N,findA_Two,Ta_array,Sa_array)
            else:
                print('---It won\'t write any files.---')
                break
            #auto VCD
            print('---------Auto Verification---------')
            autoVCD(fn,fn2,fvcd,fo,selMode)
            print('The file has been authenticated.')
            break
        else:
            print('\nNo this model!\nExit the program.\n')
            break
        ################################################# 
    elif selA == 2:
        Two_A_most,Two_A_most_cbitN,One_A_most,One_A_most_cbitN=FindA(2,rang2)
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
            wr_txt=int(input('Write the verilog file or not?\t(1---> Yes.  2---> No.)\nPlease select:'))
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
            autoVCD(fn,fn2,fvcd,fo,selMode)
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
            wr_txt=int(input('Write the verilog file or not?\t(1---> Yes.  2---> No.)\nPlease select:'))
            if wr_txt == 1:
                fn,fn2,fvcd,fo=Alter_veri(N,findA_One,Ta_array)
            else:
                print('---It won\'t write any files.---')
                break
            #auto VCD
            print('---------Auto Verification---------')
            autoVCD(fn,fn2,fvcd,fo,selMode)
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
            correct2=CorrectBER(bitAN,ANe,findA_Two,Ra_array,Ta_array,Sa_array)
            correct=Bin2Dec(bitAN, correct2)
            if correct == N:
                print('\nCorrect ^_^\n')
            else:
                print('\nFail~ q_q\n')
            #txt
            wr_txt=int(input('Write the verilog file or not?\t(1---> Yes.  2---> No.)\nPlease select:'))
            if wr_txt == 1:
                fn,fn2,fvcd,fo=BER_veri(N,findA_Two,Ta_array,Sa_array)
            else:
                print('---It won\'t write any files.---')
                break
            #auto VCD
            print('---------Auto Verification---------')
            autoVCD(fn,fn2,fvcd,fo,selMode)
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
            correct2=CorrectAWE(bitAN,ANe,findA_Two,Ra_array,Ta_array,Sa_array)
            correct=Bin2Dec(bitAN, correct2)
            if correct == N:
                print('\nCorrect ^_^\n')
            else:
                print('\nFail~ q_q\n')
            #txt
            wr_txt=int(input('Write the verilog file or not?\t(1---> Yes.  2---> No.)\nPlease select:'))
            if wr_txt == 1:
                fn,fn2,fvcd,fo=AWE_veri(N,findA_Two,Ta_array,Sa_array)
            else:
                print('---It won\'t write any files.---')
                break
            #auto VCD
            print('---------Auto Verification---------')
            autoVCD(fn,fn2,fvcd,fo,selMode)
            print('The file has been authenticated.')
            break
        
        else:
            print('\nNo this mode!\nExit the program.\n')
            break

        #################################################   
    else:
        print('There don\'t have this mode.\n')
   
   
# AN codes decoder
* 4 error models
    1. Uni-direction / Fully asymmetric channel model (完全非對稱模型)
        * Error will only occur in uni-direction.事先知道哪一個1->0/0->1
    2. Alternative-direction / Fully asymmetric channel model 
        * 無法事先知道哪一個
        * 莫比烏斯環
    3. Bit Error Rate mode (BER)
        * 這bit從0->1 or 1->0, 但是各有機率
    4. AWE 
        * error come from add or sub.

* Versions
    * v1: 
        * input: ANe, R
        * output: Nc
    * v2:
        * input: ANe
        * output: Nc

* Terminal:
    * Step1:選擇A的模式
        > Ex: The length of the number entered = 4 bit  
        > 以AWE mode 來舉例: Mode 1=> A=19, 可更正4bit的N  
        >                   Mode 2=> A=29, 可更正9bit的N  
        > mode 1 ---> Find an available A          
        > mode 2 ---> Find the most appropriate A  
        >   
        > Please select a mode:1  
        > -------------Find an available A-------------  
        > 雙向錯誤可用的A(7~100)=[7, 11, 13, 19, 23, 29, 37, 47, 53, 59, 61, 67, 71, 79, 83]  
        > 可更正bit數(N)= [0, 1, 2, 4, 6, 9, 12, 17, 20, 23, 24, 26, 28, 32, 34]  
        >   
        > 單向錯誤可用的A(7~100)= [11, 13, 19, 29, 37, 53, 59, 61, 67, 83]  
        > 可更正bit數(N)= [6, 8, 13, 23, 30, 46, 52, 54, 59, 75]  
    
    * Step2:選擇Error models
        > model 1 ---> Unidirectional Fully Asymmetric Channel model  
        > model 2 ---> Alternative-direction Fully Asymmetric Channel model  
        > model 3 ---> BER model  
        > model 4 ---> AWE model
        > Choose model:4
    * Step3:輸入數字並軟體驗證更正能力
        * Step3-1: 輸入數字
            > Input a number(N):13
            > N的Bit數= 4  
            > ----------Two-way error mode----------  
            > 適合的A= 19  
            > 可更正的bit數(N)= 4  
            >  
            > ---------Original Data-------------  
            > Correct N= 13  
            > Correct AN= 247  
            > Correct AN(2)= 11110111  
            > module= 19  
        * Step3-2: 隨機1位元錯誤植入
            > ------Random error generation------  
            > Error bit= 1  
            > Error AN= 245  
            > Error AN(2)= 011110101  
        * Step3-3: AN codes的更正方法(餘數對應錯誤位元)
            > ----------CorrectTwo----------  
            > Error is in 1 bit  
            > ------Error come fromr Subtraction.------  
            > final_answer= 13  
            >   
            > Correct ^_^  
    * Step4:生成解碼器Verilog file
        > Write the verilog file or not?  
        > 1---> Yes.  
        > 2---> No.  
        > Please select:1  
        * Step4-1: 將基本更正資訊寫入
            > ---------------開始寫檔案---------------  
            > 可更正AN的bit數= 9  
            > mod的bit數= 5  
            > and gate數= 18  
            > 可更正N的bit數= 4  
        * Step4-2: 對同一數隨機五次的錯誤植入(tb.v使用)
            > ---------------開始生成tb所需的Data---------------  
            > ###Data 1 生成###  
            >   
            > ---------Original Data-------------  
            > Correct N= 13  
            > Correct AN= 247  
            > Correct AN(2)= 11110111  
            > module= 19  
            > 
            > ------Random error generation------  
            > Error bit= 5  
            > Error AN= 215  
            > Error AN(2)= 011010111  
            > 
            > ###Data 2 生成###  
            > 
            > ---------Original Data-------------  
            > Correct N= 13  
            > Correct AN= 247  
            > Correct AN(2)= 11110111  
            > module= 19  
            > 
            > ------Random error generation------  
            > Error bit= 1  
            > Error AN= 245  
            > Error AN(2)= 011110101  
            > 
            > ###Data 3 生成###  
            > 
            > ---------Original Data-------------  
            > Correct N= 13  
            > Correct AN= 247  
            > Correct AN(2)= 11110111  
            > module= 19  
            > 
            >  ------Random error generation------  
            > Error bit= 3  
            > Error AN= 255  
            > Error AN(2)= 011111111  
            > 
            > ###Data 4 生成###  
            > 
            > ---------Original Data-------------  
            > Correct N= 13  
            > Correct AN= 247  
            > Correct AN(2)= 11110111  
            > module= 19  
            > 
            > ------Random error generation------  
            > Error bit= 2  
            > Error AN= 243  
            > Error AN(2)= 011110011  
            > 
            > ###Data 5 生成###  
            > 
            > ---------Original Data-------------  
            > Correct N= 13  
            > Correct AN= 247  
            > Correct AN(2)= 11110111  
            > module= 19  
            > 
            > ------Random error generation------  
            > Error bit= 6  
            > Error AN= 183  
            > Error AN(2)= 010110111  
        * Step4-3:生成檔案(包含tb)並呼叫iverilog & GTKwave進行驗證
            > ---------------寫檔案完成---------------  
            > ./files/AWE_20221005_1324/ANdecoder_AWE_19_for_N_13.v has been generated.  
            > 
            > ./files/AWE_20221005_1324/ANdecoder_AWE_19_tb_for_N_13.v has been generated.  
            > 
            > ---------Auto Verification---------    
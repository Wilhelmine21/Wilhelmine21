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
        > Please select a mode:2  
        > -------------Find the most appropriate A-------------  
        > 雙向錯誤最合適的A= [7, 13, 29, 61, 83]  
        > 雙向錯誤可更正bit數(N)= [0, 2, 9, 24, 34]  
        > 
        > 單向錯誤最合適的A= [13, 29, 61, 83]  
        > 單向錯誤可更正bit數(N)= [8, 23, 54, 75] 
    * Step2:選擇Error models
        > model 1 ---> Unidirectional Fully Asymmetric Channel model  
        > model 2 ---> Alternative-direction Fully Asymmetric Channel model  
        > model 3 ---> BER model  
        > model 4 ---> AWE model  
        > Choose model:3
    * Step3:輸入數字並軟體驗證更正能力
        * Step3-1: 輸入數字
            > Input a number(N):218
            > N的Bit數= 8  
            > ----------Two-way error mode----------  
            > 適合的A= 61  
            > 可更正的bit數(N)= 24  
            >  
            > ---------Original Data-------------  
            > Correct N= 218  
            > Correct AN= 13298  
            > Correct AN(2)= 11001111110010  
            > module= 61  
        * Step3-2: 隨機1位元錯誤植入
            > ------Random error generation------  
            > Error bit= 2  
            > Error AN= 13302  
            > Error AN(2)= 000000000000000011001111110110  
        * Step3-3: AN codes的更正方法(餘數對應錯誤位元)
            > ----------CorrectTwo----------  
            > Error is in 2 bit  
            > ------Error come from Addition.------  
            > final_answer= 218  
            >   
            > Correct ^_^  
    * Step4:生成解碼器Verilog file
        > Write the verilog file or not?  
        > 1---> Yes.  
        > 2---> No.  
        > Please select:1  
        * Step4-1: 將基本更正資訊寫入
            > ---------------開始寫檔案---------------  
            > 可更正AN的bit數= 30  
            > mod的bit數= 6  
            > and gate數= 60  
            > 可更正N的bit數= 24  
        * Step4-2: 對同一數隨機五次的錯誤植入(tb.v使用)
            > ---------------開始生成tb所需的Data---------------  
            > ###Data 1 生成###  
            >   
            > ---------Original Data-------------  
            > Correct N= 218  
            > Correct AN= 13298  
            > Correct AN(2)= 11001111110010  
            > module= 61  
            > 
            > ------Random error generation------  
            > Error bit= 16  
            > Error AN= 78834  
            > Error AN(2)= 000000000000010011001111110010  
            > 
            > ###Data 2 生成###  
            > 
            > ---------Original Data-------------  
            > Correct N= 218  
            > Correct AN= 13298  
            > Correct AN(2)= 11001111110010    
            > module= 61  
            > 
            > ------Random error generation------  
            > Error bit= 25  
            > Error AN= 33567730  
            > Error AN(2)= 000010000000000011001111110010  
            > 
            > ###Data 3 生成###  
            > 
            > ---------Original Data-------------  
            > Correct N= 218  
            > Correct AN= 13298  
            > Correct AN(2)= 11001111110010  
            > module= 61  
            > 
            >  ------Random error generation------  
            > Error bit= 8  
            > Error AN= 13042  
            > Error AN(2)= 000000000000000011001011110010  
            > 
            > ###Data 4 生成###  
            > 
            > ---------Original Data-------------  
            > Correct N= 218  
            > Correct AN= 13298  
            > Correct AN(2)= 11001111110010  
            > module= 61   
            > 
            > ------Random error generation------  
            > Error bit= 1  
            > Error AN= 13296  
            > Error AN(2)= 000000000000000011001111110000  
            > 
            > ###Data 5 生成###  
            > 
            > ---------Original Data-------------  
            > Correct N= 218  
            > Correct AN= 13298 
            > Correct AN(2)= 11001111110010  
            > module= 61  
            > 
            > ------Random error generation------  
            > Error bit= 29  
            > Error AN= 536884210  
            > Error AN(2)= 100000000000000011001111110010   
        * Step4-3:生成檔案(包含tb)並呼叫iverilog & GTKwave進行驗證
            > ---------------寫檔案完成---------------  
            > ./files/BER_20221005_1405/ANdecoder_BER_61_for_N_218.v has been generated.   
            > 
            > ./files/BER_20221005_1405/ANdecoder_BER_61_tb_for_N_218.v has been generated.  
            > 
            > ---------Auto Verification---------  
            > VCD info: dumpfile ./files/BER_20221005_1405/A61N218.  
            > vcd opened for output.    
            > ./files/BER_20221005_1405/> ANdecoder_BER_61_tb_for_N_218.v:21: $finish called at 60 (1s)  
            > 
            > GTKWave Analyzer v3.3.108 (w)1999-2020 BSI  
            > [0] start time.  
            > [60] end time.  
            > Interpreter id is gtkwave_16260  
            > % WM Destroy  
            > The file has been authenticated.     
* 波形圖驗證:(若為自動顯示，僅會顯示出numx,out兩個訊號，其他需要自行點開)
<img src="2022-10-05 14.07.31.png"></br>  

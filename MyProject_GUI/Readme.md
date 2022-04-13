# This project is about my research.
* I'm [Ting-Yu Chen](https://github.com/Wilhelmine21/Wilhelmine21). 
* I'm from [Test Lab](http://testlab.ncue.edu.tw/tch/), Electronic Engineering, National Changhua University of Education.
* The title of my thesis is **AN Codes LS-PWL-RALUT**.

## I. AN Codes LS-PWL-RALUT
* AN codes --- [wiki](https://en.wikipedia.org/wiki/AN_codes)
* Light Number
* 說明
---
## II. My Project GUI
* 簡介 我做了一個GUI用來展示
* 環境 iVerilog GTKwave
* 版本(Win10, Linux)及附加檔案(for EDA)

###  My Research
<img src="./img/Pasted image 20220413130346.png" width="50%" height="50%"/><img src="./img/Pasted image 20220413130817.png" width="50%" height="50%"/>

* 上圖(左)為Win10版本的GUI, 上圖(右)為Linux(Centos 7)版本的GUI.
* 主要展示 `題目名稱`, `作者名稱`, `實驗室系所學校`和`摘要`
* 下方三個按鈕分別對應不同的project.

* 上方選單File: </br>
	<img src="./img/Pasted image 20220413133333.png" width="50%" height="50%"/>
	* (1) Open file: 開啟舊檔
	* (2) Exit: 關閉程式
	* (3) Quit: 關閉程式並關閉後台 ⬅ 當程式當機時，可由此嘗試關閉.

* 上方選單Help: </br> 
	<img src="./img/Pasted image 20220413133156.png" width="50%" height="50%"/>
	
	* (1) Demo Video: 連接到Youtube的所有功能說明及展示之影片
		* a. Windows 10 version --- [video](https://www.youtube.com/watch?v=kXfVsiijhno)
		* b. Linux (Centos 7) version --- [video](https://www.youtube.com/watch?v=Rb99CHsb28k)
	
	* (2) About: 顯示此程式的相關資訊 </br>
		<img src="./img/Pasted image 20220413134306.png" width="40%" height="40%"/>
---
#### 1. AN codes and decoder
<img src="./img/Pasted image 20220413130543.png" width="40%" height="40%"/>

* 這個Project主要用來生成AN codes解碼器(Verilog file)
* Step 1. 找到可用的A
	* (1) 輸入範圍 
		* 需大於10
	* (2) 選擇錯誤模型
		* Uni HL: 單一錯誤方向之完全非對稱模型(錯誤由1變0)
		* Uni LH: 單一錯誤方向之完全非對稱模型(錯誤由0變1)
		* Alter: 未知錯誤方向之完全非對稱模型
		* BER: Bit Error Rate model
		* AWE: Arithmetic Weight Error model
	* (3) A maybe欄位會展示出範圍內可用的A
* Step 2. 生成Verilog檔案
	* (1) 在Select A輸入想要的A值
		* 此值須為A maybe欄位中出現過的數字
	* (2) 按下`Gen & Show`，即可在select A下方的文字框看見生成的檔案內容 </br>
	<img src="./img/Pasted image 20220413141429.png" width="40%" height="40%"/> </br>
	* (3) 若是看不清楚，可使用上方選單File->Open File... 開啟檔案查看 </br>
	<img src="./img/Pasted image 20220413141620.png" width="40%" height="40%"/> </br>
* Step 3. Verilog 驗證
	* 這個功能使用[iVerilog](http://iverilog.icarus.com)和[GTKwave](http://gtkwave.sourceforge.net)來進行驗證
	* testbench會隨解碼器檔一起生成
		* 對同一個數字做不同bit錯誤 
		* 只要Output的數字一樣即為更正成功
	
		<img src="./img/Pasted image 20220413141506.png" width="40%" height="40%"/>
***
* 上方的選單Help:</br>
 	<img src="./img/Pasted image 20220413141956.png" width="40%" height="40%"/></br>
	* 前兩項會連結到iVerilog和GTKwave的官網
	* 第三項 Error Model Descripton為錯誤模型的簡單說明及電路圖
		* 會根據Error Model選擇的不同而有改變說明</br>
		<img src="./img/Pasted image 20220413142653.png" width="30%" height="30%"/>
		<img src="./img/Pasted image 20220413142534.png" width="50%" height="50%"/><img src="./img/Pasted image 20220413142605.png" width="70%" height="70%"/></br>
	
	* 第四項Video則為AN codes這個project展示與說明的影片
	* 最後About會顯示程式資訊</br>
		<img src="./img/Pasted image 20220413142805.png" width="40%" height="40%"/>
*** 
	
#### 2. ANRCAM
<img src="./img/Pasted image 20220413130605.png" width="50%" height="50%"/></br>
* 這個project透過設定基本參數，對激勵函數做線性分段，搜尋出最少的線段，範圍和輕數斜率等數據
	
---

#### 3. EDA
<img src="./img/Pasted image 20220413130923.png" width="50%" height="50%"/></br>
* 第三個Project是用來做自動化繞線佈局
* 此功能僅能在工作站運行, 因此無windows版本
* 需要額外的檔案 --- `EDA_add_files_GUI.tar`
	* 開始GUI前須先解壓縮此檔案
	
		<img src="./img/Pasted image 20220413144023.png" width="50%" height="50%"/></br>
	* 第一排按鈕
		* Layout: 自動化佈局, 使用`Design Compiler`和`IC Compiler`
		* DRC: Design Rule Check 驗證
		* LVS: Layout Versus schematic 驗證
	* 第二排按鈕
		* About會顯示程式資訊
	
		<img src="./img/Pasted image 20220413144807.png" width="30%" height="30%"/></br>

	*	
		* Open file 開啟舊檔
		* Exit 關閉程式

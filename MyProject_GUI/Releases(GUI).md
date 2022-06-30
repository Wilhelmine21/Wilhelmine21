# Releases

## v4.1 (Windows)
1. 字體大小改變,font=("微軟正黑體",12)
2. messagebox無法改變字型(暫不考慮更改)

## v4.2 (Ubuntu)
1. where指令改成which(For Ubuntu)
2. 無程式圖標(icon)
3. 不指定視窗大小(除了Project-ANcodes: Error Model 說明)

## v4.3 (Centos7)
* 需額外檔案(EDA_add_files_GUI.tar)(For EDA)(本壓縮檔只有執行檔)
1. Font size change, font=("Arial",16)
2. Change all Chinese to English (For Centos7)
3. Use where command
4. Use ncverilog(xmverilog) and nwave
	* ANRCAM_tb use printData=3
	* Something has an problem
	> 1>Failure on Verdi 3-tier licensing, Use nWave -licdebug for more information.
5. NO Program icon (icon)

---
# Version history

## v2.0 : 
* 將說明圖片轉成可包進exe的格式(import base64)

## v2.1 : 
* 將網址改成變數(存在./icon/Link裡)

## v3.0 :
* 競賽 Ver.
1. USE no name / no icon 
2. USE Ncverilog and nWave -> ANcodes v3.0 and ANRCAM v4.0
	* Problem :
		*  source /usr/cad/cadence/CIC/xcelium.cshrc (<- not Auto, need enter)
* ANcodesVersion="v3.0"
	1. USE Ncverilog and nWave(Centos7)
	2. 新增按鍵來開啟圖片
		* bug: 開啟時間太久(待解決)
		* 使用(是/否)來決定開啟方式(GUI/電腦預設)

## v3.1 (未做但可行，效益不大)(參考0429/test.py作法)
* 將按鈕限制只顯示一個toplevel
* 例如:
	* 主視窗的AN codes按鈕會開啟AN Codes and Decoder副視窗
	* 當視窗開啟時不會再開啟第二個一樣的視窗
	* 但程式碼會變長 # (不做)

## v4.0
* TFZ Demo
* 增加講解題目影片Link
	* 方案一: 增加按鈕
		* 問題: 排版及顏色
	* (**USED**)方案二: 題目左鍵點擊(同Github連結方式)

## v4.1 (Windows)
1. 字體大小改變,font=("微軟正黑體",12)
2. messagebox無法改變字型(暫不考慮更改)

## v4.2 (Ubuntu)
1. where指令改成which(For Ubuntu)
2. 無程式圖標(icon)
3. 不指定視窗大小(除了Project-ANcodes: Error Model 說明)

## v4.3 (Centos7)
* 需額外檔案(EDA_add_files_GUI.tar)(For EDA)(本壓縮檔只有執行檔)
1. Font size change, font=("Arial",16)
2. Change all Chinese to English (For Centos7)
3. Use where command
4. Use ncverilog(xmverilog) and nwave
	* ANRCAM_tb use printData=3
	* Something has an problem
	> 1>Failure on Verdi 3-tier licensing, Use nWave -licdebug for more information.
5. NO Program icon (icon)

# <center>GUI --- tkinter</center>
###### * 無法直接在此執行程式，請自行複製貼上成py檔執行

<!-- <font color=aquamarine></font> -->
## 1. 初始化
* 建立視窗
    * <font color=aquamarine>root = Tk()</font>
    * <font color=aquamarine>root.mainloop() <---放最後</font>    
* 相關參數
    * <font color=aquamarine>title()</font>
       * i.e, root.title('簡單猜單字')
    * <font color=aquamarine>geometry("W x H")</font>
       * pixel.
       * i.e, root.geometry('500x200') 
    * <font color=aquamarine>maxsize(W,H)</font>
       * 設定拖曳最大寬度和高度
       * i.e, root.maxsize(500,200)
    * <font color=aquamarine>resizable(True,True)</font> 
       * 設定是否可改視窗大小，(寬度，高度)
        * i.e, root.resizable(True,True)
  
  <!-- <font color=aquamarine></font> -->
## 2. 標籤label
* 相關參數
    * <font color=aquamarine>text</font>
        * 標籤內容，使用"\n"可寫多行
    * <font color=aquamarine>width</font>
        * 標籤寬度，單位:字元
    * <font color=aquamarine>height</font>
        * 標籤高度，單位:字元
    * <font color=aquamarine>bg or background</font>
        * 背景色彩
    * <font color=aquamarine>fg or froeground</font>
        * 字型色彩
    * <font color=aquamarine>font()</font>
        * 可選擇字型與大小
        * <font color=lightcoral>Helvetica字形名稱 / bold粗體 / italic斜體</font>
    * <font color=aquamarine>textvariable</font>
        * 可以設定標籤以變數形式顯示
        * 搭配**X1=IntVar() and textvariable=X1**使用        
    * <font color=aquamarine>image</font>
        * 標籤以圖形顯示     
    * <font color=aquamarine>relief</font>
        * 預設relief=flat，可由此控制標籤的外框            
    * <font color=aquamarine>justify</font>
        * 在多行文件時最後一行的對齊方式
        * LEFT / CENTER / RIGHT
        * 預設: CENTER
  <!-- <font color=aquamarine></font> -->
  
  <!-- <font color=aquamarine></font> -->
* **label(...).pack()**
* pack()用途: 包裝視窗的元件和定位視窗的元件

### 2.1 pack()方法
* <font color=aquamarine>side</font> = TOP / BOTTOM / LEFT / RIGHT
* <font color=aquamarine>padx</font> 增加x軸間距，pixel
* <font color=aquamarine>pady</font> 增加y軸間距，pixel

### 2.2 grid()方法
* (row, column)
<!-- <font color=LightYellow></font> -->
<!-- <font color=aquamarine/lightcoral/orange></font> -->
<table>
  <tbody>
  <tr>
    <th>(<font color=aquamarine>row=0</font>,<font color=lightcoral>column=0</font>) </th>
    <th>(<font color=aquamarine>row=0</font>,<font color=orange>column=1</font>)</th>
    <th>(<font color=aquamarine>row=0</font>,<font color=MediumOrchid>column=2</font>)</th>
  </tr>
  <tr>
    <th>(<font color=LightSkyBlue>row=1</font>,<font color=lightcoral>column=0</font>)</th>
    <th>(<font color=LightSkyBlue>row=1</font>,<font color=orange>column=1</font>)</th>
    <th>(<font color=LightSkyBlue>row=1</font>,<font color=MediumOrchid>column=2</font>)</th>
  </tr>
  <tr>
    <th> (<font color=Gold>row=n</font>,<font color=lightcoral>column=0</font>)</th>
    <th> (<font color=Gold>row=n</font>,<font color=orange>column=1</font>) </th>
    <th>(<font color=Gold>row=n</font>,<font color=MediumOrchid>column=2</font>)</th>
  </tr>
</table>
<!-- | (<font color=aquamarine>row=0</font>,<font color=lightcoral>column=0</font>) | (<font color=aquamarine>row=0</font>,<font color=orange>column=1</font>) | (<font color=aquamarine>row=0</font>,<font color=MediumOrchid>column=2</font>) |
| :----: | :----: | :----: |
| (<font color=LightSkyBlue>row=1</font>,<font color=lightcoral>column=0</font>) | (<font color=LightSkyBlue>row=1</font>,<font color=orange>column=1</font>) | (<font color=LightSkyBlue>row=1</font>,<font color=MediumOrchid>column=2</font>) |
| ... | ... | ... |
| (<font color=Gold>row=n</font>,<font color=lightcoral>column=0</font>) | (<font color=Gold>row=n</font>,<font color=orange>column=1</font>) | (<font color=Gold>row=n</font>,<font color=MediumOrchid>column=2</font>) | -->

* **columnspan**: col合併
* **rowspan**: row合併

### 2.3 place()方法
* 使用x,y直接定位

<!-- <font color=lightcoral></font> -->
## 3. Buttom
* 相關參數
    * <font color=aquamarine>text</font>
        * 功能鈕名稱
    * <font color=aquamarine>width</font>
        * 寬度，單位:字元寬
    * <font color=aquamarine>height</font>
        * 高度，單位:字元高
    * <font color=aquamarine>bg or background</font>
        * 背景色彩
    * <font color=aquamarine>fg or froeground</font>
        * 字型色彩
    * <font color=aquamarine>image</font>
        * 功能鈕上的圖形
    * <font color=aquamarine>command</font>
        * 功能鈕功能
        * 使用<font color=lightcoral>root.destroy</font>可以使GUI介面關閉，同時程式結束
        * 使用<font color=orange>root.quit</font>可以結束python shell內執行的程式，**但視窗繼續執行**(<---好像不行,3/20)  
 
<!-- <font color=aquamarine></font> -->
### 3.1 config()
* <font color=aquamarine>config(option=value)</font>其實是視窗元件的共通方法，透過設定option為bg參數時，可以設定視窗元件的背景顏色         
### 3.2 lambda
* 相同工作但不同參數，可以簡化設定

## 4. 變數類別 Variable Classes
<!-- <font color=aquamarine/lightcoral/orange></font> -->
* x=<font color=aquamarine>Int</font>Var()
    * 整數變數，0
* x=<font color=aquamarine>Double</font>Var()
    * 浮點數變數，0.0
* x=<font color=aquamarine>String</font>Var()
    * 字串變數，""
* x=<font color=aquamarine>Boolean</font>Var()
    * 布林值變數，True 1, False 0
* 可以使用<font color=lightcoral>get()</font>方法<font color=lightcoral>取得</font>變數內容
* 可以使用<font color=orange>set()</font>方法<font color=orange>設定</font>變數內容
  
## 5. 文字方塊 Entry
<!-- <font color=aquamarine/lightcoral/orange></font> -->
* 相關參數
    * <font color=aquamarine>width</font>
        * 寬度，單位:字元寬
    * <font color=aquamarine>height</font>
        * 高度，單位:字元高
    * <font color=aquamarine>bg or background</font>
        * 背景色彩
    * <font color=aquamarine>fg or froeground</font>
        * 字型色彩
    * <font color=aquamarine>state</font>
        * 輸入狀態，預設是<font color=lightcoral>NORMAL</font>表示可以輸入，<font color=orange>DISABLE</font>則是無法輸入
    * <font color=aquamarine>textvariable</font>
        * 文字變數
    * <font color=aquamarine>show</font>
        * 顯示輸入字元
        * i.e, show='*'表示顯示星號，常用在**密碼欄**輸入  

### 5.1 在Entry插入字串
<!-- <font color=aquamarine/lightcoral/orange></font> -->
* 在tkinter模組中，可以使用<font color=aquamarine>insert(index, s)</font>插入字串，會插入在index之前。
* 通常會將其放在<font color=aquamarine>Entry()</font>建立完文字方塊後。
  
### 5.2 在Entry刪除字串
<!-- <font color=aquamarine/lightcoral/orange></font> -->
* 在tkinter模組中，可以使用<font color=aquamarine>delete(first, last=None)</font>刪除Entry內字串。
* <font color=aquamarine>delete(0, END)</font>可以刪除整個字串
  
## 6. 文字區域 Text
<!-- <font color=aquamarine/lightcoral/orange></font> -->
* 相關參數
    * <font color=aquamarine>width</font>
        * 寬度，單位:字元寬
    * <font color=aquamarine>height</font>
        * 高度，單位:字元高
    * <font color=aquamarine>bg or background</font>
        * 背景色彩
    * <font color=aquamarine>fg or froeground</font>
        * 字型色彩
    * <font color=aquamarine>state</font>
        * 輸入狀態，預設是<font color=lightcoral>NORMAL</font>表示可以輸入，<font color=orange>DISABLE</font>則是無法輸入
    * <font color=aquamarine>xscrollcommand</font>
        * 水平卷軸的連結
    * <font color=aquamarine>yscrollcommand</font>
        * 垂直卷軸的連結
    * <font color=aquamarine>wrap</font>
        * 換行參數，預設<font color=lightcoral>CHAR</font>，若輸入資料超出寬度時，必要時會將單字依拼音拆成不同行輸出。
        * 若是<font color=lightcoral>WORD</font>，則不會將單字拆開成不同行輸出。
        * 若為<font color=orange>NONE</font>，不換行，有水平卷軸。  
  
## 7. 卷軸 Scrollbar
<!-- <font color=aquamarine/lightcoral/orange></font> -->
* <font color=aquamarine>scrollbar = Scrollbar(root)</font>
* 以下範例
    * line10> scrollbar.config(command=<font color=lightcoral>text.yview</font>)
        * 觀念同 scrollbar["command"]=text.yview #設定執行方法
    * line11> text.config(<font color=lightcoral>yscrollcommand=scrollbar.set</font>) 
        * 將文字區域與卷軸做連結
 
## 8. 選項鈕 Radiobutton
<!-- <font color=aquamarine/lightcoral/orange></font> -->
* 相關參數
    * <font color=aquamarine>text</font>
        * 選項鈕旁的文字
    * <font color=aquamarine>font</font>
        * 字型        
    * <font color=aquamarine>width</font>
        * 寬度，單位:字元寬
    * <font color=aquamarine>height</font>
        * 高度，單位:字元高
    * <font color=aquamarine>padx</font>
        * 預設是1，可設定選項鈕與文字的間隔
    * <font color=aquamarine>pady</font>
        * 預設是1，可設定選項鈕的上下間距    
    * <font color=aquamarine>value</font>
        * 選項鈕的值，可區分所選取的選項鈕
    * <font color=aquamarine>indicatoron</font>
        * 當值為0，可建立盒子選項鈕   
    * <font color=aquamarine>command</font>
        * 當選項更動，自動執行副函數               
    * <font color=aquamarine>variable</font>
        * 設定或取得目前選取的選項鈕
        * 通常為IntVar or StringVar     

## 9. 核取方塊 Checkbutton
<!-- <font color=aquamarine/lightcoral/orange></font> -->
* 與選項紐差異: <font color=lightcoral>複選</font>
* 相關參數
    * <font color=aquamarine>text</font>
        * 核取方塊旁的文字
    * <font color=aquamarine>font</font>
        * 字型        
    * <font color=aquamarine>width</font>
        * 核取方塊有幾個字元寬
        * 省略時會自行調整為實際寬度
    * <font color=aquamarine>height</font>
        * 核取方塊文字有幾行，預設一行
    * <font color=aquamarine>padx</font>
        * 預設是1，可設定核取方塊與文字的間隔
    * <font color=aquamarine>pady</font>
        * 預設是1，可設定核取方塊的上下間距    
    * <font color=aquamarine>command</font>
        * 當選項更動，自動執行副函數               
    * <font color=aquamarine>variable</font>
        * 設定或取得目前選取的核取方塊
        * 通常為IntVar or StringVar   
## 10. 對話方塊 Messagebox
* from tkinter import messagebox
* 一般提示
    * showinfo(title,message,options)
* <font color=Gold>警告</font>
    * <font color=Gold>showwarning(title,message,options)</font>
* <font color=Red>錯誤</font>
    * <font color=Red>showerror(title,message,options)</font>
* <font color=aquamarine>詢問</font>
    * 回傳值為yes or no
    * <font color=aquamarine>askquestion(title,message,options)</font>
#  
* 顯示確定或取消訊息
    * 回傳值為True or False
    * askokcancel(title,message,options)
#  
* 顯示是或否
    * 回傳值為True or False
    * askyesno(title,message,options)
#  
* 顯示是或否或取消訊息
    * askyesnocancel(title,message,options)
#  
* 顯示重試或取消訊息
    * 回傳值為True or False
    * askyesnocancel(title,message,options)
#  
* **options相關參數**
    * <font color=aquamarine>default constant</font>
        * 預設按鈕是OK、Yes、Retry。
    * <font color=aquamarine>icon(constant)</font>
        * 可設定所顯示的圖示。
        * INFO、ERROR、QUESTION、WARNING四種圖示可以設定。
    * <font color=aquamarine>parent(widget)</font>
        * 指出當對話方塊關閉時，焦點視窗將返回此視窗。
  
## 11. 圖形 PhotoImage
<!-- <font color=aquamarine/lightcoral/orange/LightSteelBlue/LightBlue></font> -->
* 可以應用在許多地方，例如:label、botton、Radiobutton、Text等。
* 在使用前可以用PhotoImage()方法建立此圖形物件，然後再將此物件適度應用在其它視窗元件。
* 語法如下:
    * Photolmage(file="xxx.***gif***")
* 需留意Photolmage早期支援gif，不接受jpg或png。
* 目前已可以支援png。  

### 11.2 圖型與功能鈕應用
* 一般功能鈕是用文字作按鈕名稱
#  
* 若是我們要使用圖形當作按鈕
    * 在Button()內
        * 省略text參數設定
        * 增加image參數設定圖形物件
    #  
    * 若是要圖形和文字並存在功能鈕,需增加參數"compund=xx",
        * xx 可以是LEFT、TOP、RIGH、BOTTOM、CENTER代表圖形在文字的左、上、右、下、中央。  

## 12. 尺度 Scale控制
* 相關參數
    * <font color=aquamarine>from_</font>
        * 尺度範圍值的初值
    * <font color=aquamarine>to</font>
        * 尺度範圍值的末端值
    * <font color=aquamarine>orient</font>
        * 預設是水平尺度，可以設定HORIZONTAL or VERTICAL
    * <font color=aquamarine>command</font>
        * 當選項更動，自動執行副函數 
    * <font color=aquamarine>length</font>
        * 尺度長度，預設是100          

## 13. 功能表 Menu
* 相關參數
    * <font color=aquamarine>activebackground</font>
        * 當滑鼠移置此功能表項目時的背景色彩
    * <font color=aquamarine>bg</font>
        * 背景色彩       
    * <font color=aquamarine>fg</font>
        * 字型色彩
    * <font color=aquamarine>image</font>
        * 功能表項目的圖示
    * <font color=aquamarine>tearoff</font>
        * 功能表上方的分隔線
        * 1:有分隔線，功能表項目從1位置開始放置
        * 0:無分隔線，功能表項目從0位置開始放置
    * <font color=aquamarine>add_cascade()</font>
        * 建立階層式功能表，同時讓子功能項目與父功能表建立連結
    * <font color=aquamarine>add_command()</font>
        * 增加功能表項目
    * <font color=aquamarine>add_separator()</font>
        * 增加分隔線
   

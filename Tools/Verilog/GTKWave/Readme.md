# TCL for GTKWave
## Auto.tcl
```tcl
set display_list [ gtkwave::getDisplayedSignals ]
set filter [list numX out]
gtkwave::addSignalsFromList $filter
gtkwave::/Edit/Highlight_All
gtkwave::/Edit/Data_Format/Decimal
gtkwave::/Time/Zoom/Zoom_Best_Fit
gtkwave::/Edit/UnHighlight_All
```
* Line1: 
    ```tcl
    set display_list [ gtkwave::getDisplayedSignals ]
    ```
    * returns a list of all signals currently on display
* Line2: 
    ```tcl
    set filter [list <SignalName>]
    ```
    * 將想要列出的信號名稱寫出
* Line3: 
    ```tcl
    gtkwave::addSignalsFromList $filter
    ```
    * 將剛剛列出的信號名稱加入波形中
* Line4~7: 
    ```tcl
    gtkwave::/Edit/Highlight_All
    gtkwave::/Edit/Data_Format/Decimal
    gtkwave::/Time/Zoom/Zoom_Best_Fit
    gtkwave::/Edit/UnHighlight_All
    ```
    * 將所有列出的信號改成Decimal顯示並視窗最適化

## Tcl Command Syntax(來自官方文件gtkwave.pdf中附錄E)
* 除了能夠訪問菜單選項（例如，gtkwave::/File/Quit）之外，在 Tcl 腳本中還有更多可用於操作查看器的命令。
### 1. addCommentTracesFromList
* 將CommentTraces添加到查看器
* Syntax: 
    ```tcl
    set num_found [   gtkwave::addCommentTracesFromList list ]
    ```
* 例子: 
    ```tcl
    set clk48 [list]
    lappend clk48 "$facname1"
    lappend clk48 "$facname2"
    ...
    set num_added [ gtkwave::addCommentTracesFromList $clk48 ]
    ```
### 2. addSignalsFromList
* 添加信號到查看器
* Syntax: 
    ```tcl
    set num_found [ gtkwave::addSignalsFromList list ]
    ```
* 例子: 
    ```tcl
    set clk48 [list]
    lappend clk48 "$facname1"
    lappend clk48 "$facname2"
    ...
    set num_added [ gtkwave::addSignalsFromList $clk48 ]
    ```
### 3. deleteSignalsFromList
* 從查看器中刪除信號。 
* 除非在列表中多次指定信號，否則這只會刪除找到的第一個實例。
* Syntax: 
    ```tcl
    set num_deleted [ gtkwave::deleteSignalsFromList list ]
    ```
* 例子: 
    ```tcl
    set clk48 [list]
    lappend clk48 "$facname1"
    lappend clk48 "$facname2"
    ...
    set num_deleted [ gtkwave::deleteSignalsFromList $clk48 ]
    ```
### 4. deleteSignalsFromListIncludingDuplicates
* 從查看器中刪除信號。 
* 這將刪除找到的所有實例，因此無需在列表中多次指定相同的信號。
* Syntax: 
    ```tcl
    set num_deleted [ gtkwave::deleteSignalsFromListIncludingDuplicates list ]
    ```
* 例子: 
    ```tcl
    set clk48 [list]
    lappend clk48 "$facname1"
    lappend clk48 "$facname2"
    ...
    set num_deleted [ gtkwave::deleteSignalsFromListIncludingDuplicates
    $clk48 ]
    ```
### 5. findNextEdge
* 將標記推進到突出顯示信號的下一個邊緣
* Syntax: 
    ```tcl
    set marker_time [ gtkwave::findNextEdge ]
    ```
* 例子: 
    ```tcl
    gtkwave::highlightSignalsFromList "top.clk"
    set time_value [ gtkwave::findNextEdge ]
    puts "time_value: $time_value"    
    ```
### 6. findPrevEdge
* 將標記移動到高亮信號的前一個邊緣
* Syntax: 
    ```tcl
    set marker_time [ gtkwave::findPrevEdge ]
    ```
* 例子: 
    ```tcl
    gtkwave::highlightSignalsFromList "top.clk"
    set time_value [ gtkwave::findPrevEdge ]
    puts "time_value: $time_value"
    ```
### 7. forceOpenTreeNode
* 強制打開信號搜索樹中的一個樹節點並關閉其餘節點。 
* 如果上層未打開，樹將保持關閉，但是一旦上層打開，指定的層次結構將變為打開狀態。 
* 如果 path 缺失或為空字符串，則函數返回 SST 選擇的當前層次結構路徑，如果出錯則返回 -1。
* Syntax: 
    ```tcl
    gtkwave::forceOpenTreeNode hierarchy_path
    ```
   * Returned value:
        * 0 - success
        * 1 - path not found in the tree
        * -1 - SST tree does not exist
* 例子: 
    ```tcl
    set path tb.HDT.cpu
    switch -- [gtkwavetcl::forceOpenTreeNode $path] {
    -1 {puts "Error: SST is not supported here"}
    1 {puts "Error: '$path' was not recorder to dump file"}
    0 {}
    }
    ```
### 8. getArgv
* 返回用於從命令行啟動 gtkwave 的參數列表
* Syntax: 
    ```tcl
    set argvlist [ gtkwave::getArgv ]
    ```
* 例子: 
    ```tcl
    set argvs [ gtkwave::getArgv ]
    puts "$argvs"
    ```
### 9. getBaselineMarker
* 將返回Baseline標記時間的數值
* Syntax: 
    ```tcl
    set baseline_time [ gtkwave::getBaselineMarker ]
    ```
* 例子: 
    ```tcl
    set baseline [ gtkwave::getBaselineMarker ]
    puts "$baseline"
    ```
### 10. getDisplayedSignals
* 返回當前顯示的所有信號的列表
* Syntax: 
    ```tcl
    set display_list [ gtkwave::getDisplayedSignals ]
    ```
* 例子: 
    ```tcl
    set display_list [ gtkwave::getDisplayedSignals ]
    puts "$display_list"
    ```
### 11. getDumpFileName
* 返回已加載轉儲文件的文件名
* Syntax: 
    ```tcl
    set loaded_file_name [ gtkwave::getDumpFileName ]
    ```
* 例子: 
    ```tcl
    set nfacs [ gtkwave::getNumFacs ]
    set dumpname [ gtkwave::getDumpFileName
    set dmt [ gtkwave::getDumpType ]
    puts "number of signals in dumpfile '$dumpname' of type $dmt: $nfacs"
    ```
### 12. getDumpType
* 以字符串形式返迴轉儲類型（VCD、PVCD、LXT、LXT2、GHW、VZT）
* Syntax: 
    ```tcl
    set dump_type [ gtkwave::getDumpType ]
    ```
* 例子: 
    ```tcl
    set nfacs [ gtkwave::getNumFacs ]
    set dumpname [ gtkwave::getDumpFileName ]
    set dmt [ gtkwave::getDumpType ]
    puts "number of signals in dumpfile '$dumpname' of type $dmt: $nfacs"
    ```
### 13. getFacName
* 返回對應於給定設施編號的設施名稱的字符串
* Syntax: 
    ```tcl
    set fac_name [ gtkwave::getFacName fac_number ]
    ```
* 例子: 
    ```tcl
    set nfacs [ gtkwave::getNumFacs ]
    for {set i 0} {$i < $nfacs } {incr i} {
    set facname [ gtkwave::getFacName $i ]
    puts "$i: $facname"
    }    
    ```
### 14. getFacDir
* 返回與給定設施編號相對應的方向的字符串
* Syntax: 
    ```tcl
    set fac_dir [ gtkwave::getFacDir fac_number ]
    ```
* 例子: 
    ```tcl
    set nfacs [ gtkwave::getNumFacs ]
    for {set i 0} {$i < $nfacs } {incr i} {
    set facdir [ gtkwave::getFacDir $i ]
    puts "$i: $facdir"
    }    
    ```
### 15. getFacVtype
* 返回對應於給定設施編號的變量類型的字符串
* Syntax: 
    ```tcl
    set fac_vtype [ gtkwave::getFacVtype fac_number ]
    ```
* 例子: 
    ```tcl
    set nfacs [ gtkwave::getNumFacs ]
    for {set i 0} {$i < $nfacs } {incr i} {
    set facvtype [ gtkwave::getFacVtype $i ]
    puts "$i: $facvtype"
    }
    ```
### 16. getFacDtype
* 返回對應於給定設施編號的數據類型的字符串
* Syntax: 
    ```tcl
    set fac_dtype [ gtkwave::getFacDtype fac_number ]
    ```
* 例子: 
    ```tcl
    set nfacs [ gtkwave::getNumFacs ]
    for {set i 0} {$i < $nfacs } {incr i} {
    set facdtype [ gtkwave::getFacDtype $i ]
    puts "$i: $facdtype"
    }
    ```
### 17. getFontHeight
* 返回信號名稱的字體高度
* Syntax: 
    ```tcl
    set font_height [ gtkwave::getFontHeight ]
    ```
* 例子: 
    ```tcl
    set font_height [ gtkwave::getFontHeight ]
    puts "$font_height"
    ```
### 18. getFromEntry:
* 在“From:”框中返回時間值字符串。
* Syntax: 
    ```tcl
    set from_entry [ gtkwave::getFromEntry ]
    ```
* 例子: 
    ```tcl
    set from_entry [ gtkwave::getFromEntry ]
    puts "$from_entry"
    ```
### 19. getHierMaxLevel
* 返回查看器中設置的最大值
* Syntax: 
    ```tcl
    set hier_max_level [ gtkwave::getHierMaxLevel ]
    ```
* 例子: 
    ```tcl
    set max_level [ gtkwave::getHierMaxLevel ]
    puts "$max_level"
    ```
### 20. getLeftJustifySigs
* 如果信號左對齊，則返回 1，否則返回 0
* Syntax: 
    ```tcl
    set left_justify [ gtkwave::getLeftJustifySigs ]
    ```
* 例子: 
    ```tcl
    set justify [ gtkwave::getLeftJustifySigs ]
    puts "$justify"
    ```
### 21. getLongestName
* 返迴轉儲文件中最長名稱的字符數
* Syntax: 
    ```tcl
    set longestname_len [ gtkwave::getLongestName ]
    ```
* 例子: 
    ```tcl
    set longest [ gtkwave::getLongestName ]
    puts "$longest"
    ```
### 22. getMarker
* 返回主標記位置的數值
* Syntax: 
    ```tcl
    set marker_time [ gtkwave::getMarker ]
    ```
* 例子: 
    ```tcl
    set marker_time [ gtkwave::getMarker ]
    puts "$marker_time"
    ```
### 23. getMaxTime
* 返迴轉儲文件中最後一次值的數值
* Syntax: 
    ```tcl
    set max_time [ gtkwave::getMaxTime ]
    ```
* 例子: 
    ```tcl
    set max_time [ gtkwave::getMaxTime ]
    puts "$max_time"
    ```
### 24. getMinTime
* 返迴轉儲文件中第一個時間值的數值
* Syntax: 
    ```tcl
    set min_time [ gtkwave::getMinTime ]
    ```
* 例子: 
    ```tcl
    set min_time [ gtkwave::getMinTime ]
    puts "$min_time"
    ```
### 25. getNamedMarker
* 返回命名標記位置的數值
* Syntax: 
    ```tcl
    set time_value [ gtkwave::getNamedMarker which ]
    ```
    * such that which = A-Z or a-z
* 例子: 
    ```tcl
    set marker_time [ gtkwave::getNamedMarker A ]
    puts "$marker_time"
    ```
### 26. getNumFacs
* 返迴轉儲文件中遇到的設施數量
* Syntax: 
    ```tcl
    set numfacs [ gtkwave::getNumFacs ]
    ```
* 例子: 
    ```tcl
    set nfacs [ gtkwave::getNumFacs ]
    set dumpname [ gtkwave::getDumpFileName ]
    set dmt [ gtkwave::getDumpType ]
    puts "number of signals in dumpfile '$dumpname' of type $dmt: $nfacs"
    ```
### 27. getNumTabs
* 返回查看器上顯示的tabs數量
* Syntax: 
    ```tcl
    set numtabs [ gtkwave::getNumTabs ]
    ```
* 例子: 
    ```tcl
    set ntabs [ gtkwave::getNumTabs ]
    puts "number of tabs: $ntabs"
    ```
### 28. getPixelsUnitTime
* 返回每單位時間的像素數
* Syntax: 
    ```tcl
    set pxut [ gtkwave::getPixelsUnitTime ]
    ```
* 例子: 
    ```tcl
    set pxut [ gtkwave::getPixelsUnitTime ]
    puts "$pxut"
    ```
### 29. getSaveFileName
* 返回保存文件名
* Syntax: 
    ```tcl
    set save_file_name [ gtkwave::getSaveFileName ]
    ```
* 例子: 
    ```tcl
    set savename [ gtkwave::getSaveFileName ]
    puts "$savename"
    ```
### 30. getStemsFileName
* 返回stems文件名
* Syntax: 
    ```tcl
    set stems_file_name [ gtkwave::getStemsFileName ]
    ```
* 例子: 
    ```tcl
    set stemsname [ gtkwave::getStemsFileName ]
    puts "$stemsname"
    ```
### 31. getTimeDimension
* 返回保存跟踪的時間單位的第一個字符
* (例如，“u”代表我們，“n”代表“ns”，“s”代表秒等)
* Syntax: 
    ```tcl
    set dimension_first_char [ gtkwave::getTimeDimension ]
    ```
* 例子: 
    ```tcl
    set dimch [ gtkwave::getTimeDimension ]
    puts "$dimch"
    ```
### 32. getTimeZero
* 返迴轉儲文件中表示時間 #0 的數值。
* 僅當在轉儲文件中遇到 $timezero 指令時才有意義。
* Syntax: 
    ```tcl
    set zero_time [ gtkwave::getTimeZero ]
    ```
* 例子: 
    ```tcl
    set zero_time [ gtkwave::getTimeZero ]
    puts "$zero_time"
    ```
### Working...P.124~132
### 33. name
* how
* Syntax: 
    ```tcl
    
    ```
* 例子: 
    ```tcl
    
    ```
### Tcl callbacks
* gtkwave::cbClos​​eTabNumber 包含返回的值是要關閉的選項卡的編號，從零開始。由於這是在選項卡實際關閉之前設置的，因此腳本可以詢問更多信息。

* gtkwave::cbClos​​eTraceGroup 包含正在關閉的擴展跟踪或跟踪組的名稱。

* gtkwave::cbCurrentActiveTab 包含當前選擇的選項卡的編號。請注意，當創建新選項卡時，此回調有時會在新舊選項卡編號之間振盪，最終確定新選項卡正在
創建的。

* gtkwave::cbError 包含錯誤字符串，例如“重新加載失敗”、“回調中禁止 gtkwave::loadFile”、“回調中禁止gtkwave::reLoadFile”或“回調中禁止gtkwave::setTabActive”。

* gtkwave::cbFromEntryUpdated 包含更新時存儲在“From:”小部件中的值。

* gtkwave::cbOpenTraceGroup 包含正在展開的跟踪或正在打開的跟踪組的名稱。

* gtkwave::cbQuitProgram 包含啟動退出操作的選項卡編號。選項卡從零開始編號。

* gtkwave::cbReloadBegin 包含正在重新加載的跟踪的名稱。這在重新加載序列開始時調用。

* gtkwave::cbReloadEnd 包含正在重新加載的跟踪的名稱。這在重新加載序列結束時調用。

* gtkwave::cbStatusText 包含進入標準錯誤的狀態文本。

* gtkwave::cbTimerPeriod 包含以毫秒為單位的計時器週期（默認為 250），並且在每個計時器週期到期時調用此回調。如果 Tcl 代碼修改這個值，定時器週期可以動態改變。

* gtkwave::cbToEntryUpdated 包含更新時存儲在“To:”小部件中的值。

* gtkwave::cbTracesUpdated 包含跟踪的總數。當從查看器中添加、刪除等時調用此方法。

* gtkwave::cbTreeCollapse 包含被折疊的 SST 樹節點的扁平層次名稱。

* gtkwave::cbTreeExpand 包含被展開的 SST 樹節點的扁平層次名稱。

* gtkwave::cbTreeSelect 包含被選中的 SST 樹節點的扁平分層名稱。

* gtkwave::cbTreeSigDoubleClick 包含在 SST 的信號部分中被雙擊的信號的名稱。

* gtkwave::cbTreeSigSelect 包含在 SST 的信號部分中選擇的信號的名稱。

* gtkwave::cbTreeSigUnselect 包含在 SST 的信號部分中被取消選擇的信號的名稱。

* gtkwave::cbTreeUnselect 包含被取消選擇的 SST 樹節點的扁平分層名稱。
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
    * 將所有列出的信號改成Decimal顯示並最適化所有值
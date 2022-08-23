# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:10:28 2021

@author: wilhelmine
"""

import os
####------------------iverilog-------------------------------####
def autoVCD(fn,ftb,fvcd,fo):
    os.system('iverilog -o %s %s %s'%(fo,fn,ftb))
    os.system('vvp -n %s'%fo)
    os.system('gtkwave -T auto.tcl %s'%fvcd)
#
file_fn=input('檔案名:')
file_ftb=input('tb檔案名:')
file_fo=input('.out檔案名:')
file_fvcd=input('vcd檔案名:')

autoVCD(file_fn,file_ftb,file_fvcd,file_fo)
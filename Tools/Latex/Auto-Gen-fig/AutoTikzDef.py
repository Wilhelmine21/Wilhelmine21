import numpy as np
import cairosvg
import os
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
####----------------------####Ra_array,Ta_array=TableOne(module)
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
#Ra_array,Ta_array,Sa_array=TableTwo(module)
###
    
def AutoGenFig(path,A,model_sel,pdfoRsvg,SVGtoPNG,line_min,line_max):
    if pdfoRsvg == 0:
        str_command="\\documentclass{article}\n\\usepackage{tikz}\n"
    else:
        str_command="\\documentclass[tikz, margin=3pt, dvisvgm]{standalone}\n"
    #
    str_command=str_command+"\\usepackage[xetex,active,tightpage]{preview}\n\
    \\setlength\\PreviewBorder{2mm}\n\
    \\tikzset{font=\\LARGE}\n\
    \\usetikzlibrary{arrows,shapes}\n\
    \\usepackage{circuitikz}\n\
    \\usetikzlibrary{calc}\n"+\
    "\\begin{document}\n\
    \\begin{preview}\n\
    \\begin{tikzpicture}\n\
    \\ctikzset{\n\
        logic ports=ieee,\n\
        logic ports/scale=0.8,\n\
        }\n"
    # R xxx bits
    R_bits=len(bin(A-1)[2:])
    # Rmax -> Rmin
    xList=[]
    x1=0
    y1=0
    y11=y1-0.3
    y1L=y11-1
    yLP=y1L-1
    yINV=yLP-0.4
    yEND=yINV-(1.3+1.2*(A-2))

    strR_all=""
    for i in range(R_bits-1,-1,-1):
        strR1="\\node (R%s) at (%.2f,%.2f) {$R_%s$};\n"%(i,x1,y1,i)
        x1_not=x1-1.5
        xList.append([x1_not,x1])
        strR2="\\draw[-, line width=%dpt](%.2f,%.2f)--(%.2f,%.2f);\n"%(line_min,x1,y11,x1,yEND)
        strR3="\\draw[-, line width=%dpt](%.2f,%.2f)--(%.2f,%.2f);\n"%(line_min,x1_not,y1L,x1,y1L)
        strR4="\\draw[-, line width=%dpt](%.2f,%.2f)--(%.2f,%.2f);\n"%(line_min,x1_not,y1L,x1_not,yLP)
        strR5="\\node[not port, rotate=-90] (not%d) at (%.2f,%.2f){};\n"%(i,x1_not,yINV)
        strR6="\\draw[-, line width=%dpt](%.2f,%.2f)--(not%d.in);\n"%(line_min,x1_not,yLP,i)
        strR7="\\draw[-, line width=%dpt](not%d.out)--(%.2f,%.2f);\n"%(line_min,i,x1_not,yEND)
        strR_all=strR_all+strR1+strR2+strR3+strR4+strR5+strR6+strR7+"\n"
        x1=x1+3
    str_command=str_command+strR_all

        # % node and
        # [[3.0, 4.5], [6.0, 7.5], [9.0, 10.5], [12.0, 13.5]]
    yR=yINV-1.3
    strCC=""
    for j in range(1,A):
        j2=(bin(j)[2:]).zfill(R_bits)
        strC_all=""
        for k in range(len(j2)): 
            if j2[k]=="0":
                strC_all=strC_all+"\\draw[fill=black](%.2f,%.2f) circle(1mm);\n"%(xList[k][0],yR)
            else:
                strC_all=strC_all+"\\draw[fill=black](%.2f,%.2f) circle(1mm);\n"%(xList[k][1],yR)
        strC2="\\draw[-, line width=%dpt](%.2f,%.2f)--(%.2f,%.2f);\n"%(line_min,xList[0][0],yR,xList[-1][-1],yR)
        xANDR=xList[-1][-1]+2
        strC3="\\node[and port, number inputs=4] (AND%d) at (%.2f,%.2f){$%d$};\n"%(j,xANDR,yR,j)
        strC4="\\draw(AND%d.in 1) -- (AND%d.in 2) -- (AND%d.in 3) -- (AND%d.in 4);\n"%(j,j,j,j)
        strC5="\\draw[-, line width=%dpt](%.2f,%.2f)-- ++(1.1, 0);\n"%(line_max,xList[-1][-1],yR)
        strCC=strCC+strC_all+strC2+strC3+strC4+strC5+"\n"
        #print(strCC)
        yR=yR-1.2
    str_command=str_command+strCC
    ###
    color_name=["red","green","blue"]
    if model_sel==1:
        model="UNIHL"
        cbit=(A-1)
        Ra_array,Ta_array=TableOne(A)
        index=1
        d=0.2
        strConnect="\\draw [-, line width=%dpt]"%(line_max)
        strPart=""
        for i in range(cbit):
            d_and2or=8
            strNAND1="\\node [and port] (NAND%d) at ($(AND%d)+(%.1f,0)$){$%d$};\n"%(Ta_array[index],index,d_and2or,Ta_array[index])
            strNAND2="\\draw [-, line width=%dpt](AND%d.out) |- (NAND%d.in 1);\n"%(line_min,index,Ta_array[index])
            strNAND3="\\draw [-, line width=%dpt](NAND%d.in 2) -- ++(-1,0)node[left](Input%d){$Input[%d]$};\n"%(line_min,Ta_array[index],Ta_array[index],Ta_array[index])
            strNAND4="\\draw [fill=white]($(NAND%d.in 1)+(%.1f,0)$) circle(1mm);\n"%(Ta_array[index],d)
            index=index+1
            strPart=strPart+strNAND1+strNAND2+strNAND3+strNAND4
            if i == (cbit-1):
                strConnect=strConnect+" (NAND%d.out);\n"%(i)
            else:
                strConnect=strConnect+" (NAND%d.out) -- "%(i)
        ha=int(cbit/2)-1
        strAN="\\draw[-, line width=%dpt] (NAND%d.out) -- ++(2,0)node[left](AN){};\n"%(line_max,ha)
        strOut="\\draw [->, line width=%dpt]($(AN)+(1.4,0)$) -- ++(2,0)node[right](Output){Output};\n"%(line_max)
        strDiv="\\node (rect) at ($(AN)+(0.8,0)$) [draw, thick, minimum width=1cm,minimum height=4cm] {$/%d$};\n"%A
        str_command=str_command+strPart+strConnect+strAN+strOut+strDiv
    elif model_sel==0:
        model="UNILH"
        Ra_array,Ta_array=TableOne(A) #A-R
        cbit=(A-1)
        index=1
        d=0.2
        strConnect="\\draw [-, line width=%dpt]"%(line_max)
        strPart=""
        for i in range(cbit):
            d_and2or=8
            index2=A-index
            strOR1="\\node [or port] (OR%d) at ($(AND%d)+(%.1f,0)$){$%d$};\n"%(Ta_array[index2],index,d_and2or,Ta_array[index2])
            strOR2="\\draw [-, line width=%dpt](AND%d.out) |- (OR%d.in 1);\n"%(line_min,index,Ta_array[index2])
            strOR3="\\draw [-, line width=%dpt](OR%d.in 2) -- ++(-1,0)node[left](Input%d){$Input[%d]$};\n"%(line_min,Ta_array[index2],Ta_array[index2],Ta_array[index2])
            index=index+1
            strPart=strPart+strOR1+strOR2+strOR3
            if i == (cbit-1):
                strConnect=strConnect+" (OR%d.out);\n"%(i)
            else:
                strConnect=strConnect+" (OR%d.out) -- "%(i)
        ha=int(cbit/2)-1
        strAN="\\draw[-, line width=%dpt] (OR%d.out) -- ++(2,0)node[left](AN){};\n"%(line_max,ha)
        strOut="\\draw [->, line width=%dpt]($(AN)+(1.4,0)$) -- ++(2,0)node[right](Output){Output};\n"%(line_max)
        strDiv="\\node (rect) at ($(AN)+(0.8,0)$) [draw, thick, minimum width=1cm,minimum height=4cm] {$/%d$};\n"%A
        str_command=str_command+strPart+strConnect+strAN+strOut+strDiv
    elif model_sel==2:
        model="Alter"
        cbit=(A-1)
        Ra_array,Ta_array=TableOne(A) #對應兩個
        # HL NAND
        Hindex=1
        Hd=0.2
        dd=0.2
        HstrConnect="\\draw [-, line width=%dpt]"%(line_max)
        HstrPart=""
        for i in range(cbit):
            Hd_and2or=6+0.2*cbit
            Hd_up=cbit-3
            strNAND1="\\node [and port] (NAND%d) at ($(AND%d)+(%.1f,%.1f)$){$%d$};\n"%(Ta_array[Hindex],Hindex,Hd_and2or,Hd_up,Ta_array[Hindex])
            strNAND2="\\draw [-, line width=%dpt][blue](AND%d.out) -- ++(%.1f,0) |- (NAND%d.in 1);\n"%(line_min,Hindex,dd,Ta_array[Hindex])
            strNAND3="\\draw [-, line width=%dpt](NAND%d.in 2) -- ++(-1,0)node[left](Input%d){$Input[%d]$};\n"%(line_min,Ta_array[Hindex],Ta_array[Hindex],Ta_array[Hindex])
            strNAND4="\\draw [fill=white]($(NAND%d.in 1)+(%.1f,0)$) circle(1mm);\n"%(Ta_array[Hindex],Hd)
            Hindex=Hindex+1
            HstrPart=HstrPart+strNAND1+strNAND2+strNAND3+strNAND4
            if i == (cbit-1):
                HstrConnect=HstrConnect+" (NAND%d.out);\n"%(i)
            else:
                HstrConnect=HstrConnect+" (NAND%d.out) -- "%(i)
            dd=dd+0.2
        # LH OR
        index=1
        d=0.2
        ddL=0.1+0.2*(cbit-1)
        # 0.1 +0.2*11=0.1+2.2=2.3
        strConnect="\\draw [-, line width=%dpt]"%(line_max)
        strPart=""
        for i in range(cbit):
            d_and2or=6+0.2*cbit
            d_down=-1*(cbit/2)
            index2=A-index
            strOR1="\\node [or port] (OR%d) at ($(AND%d)+(%.1f,%.1f)$){$%d$};\n"%(Ta_array[index2],index,d_and2or,d_down,Ta_array[index2])
            strOR2="\\draw [-, line width=%dpt][green](AND%d.out) -- ++(%.1f,0) |- (OR%d.in 1);\n"%(line_min,index,ddL,Ta_array[index2])
            strOR3="\\draw [-, line width=%dpt](OR%d.in 2) -- ++(-1,0)node[left](Input%d){$Input[%d]$};\n"%(line_min,Ta_array[index2],Ta_array[index2],Ta_array[index2])
            index=index+1
            strPart=strPart+strOR1+strOR2+strOR3
            if i == (cbit-1):
                strConnect=strConnect+" (OR%d.out);\n"%(i)
            else:
                strConnect=strConnect+" (OR%d.out) -- "%(i)
            ddL=ddL-0.2
        #
        ha=int(cbit/2)-1
        HstrConnect2="\\draw[->, line width=%dpt] (NAND%d.out) -- ++(2,0)node[right](out1){$Out1$};\n"%(line_max,Ta_array[ha])
        strConnect2="\\draw[->, line width=%dpt] (OR%d.out) -- ++(2,0)node[right](out2){$Out2$};\n"%(line_max,Ta_array[(A-ha)])
        #
        strMux1="\\draw [-, line width=%dpt]($(NAND%d)+(10,-5)$)coordinate (O)--++(30:1)coordinate (A)--++(90:4)coordinate (B)--++(150:1)coordinate (C)--cycle node[left](MUX){MUX};\n"%(line_min,Ta_array[-1])
        strMux2="\\draw [-, line width=%dpt]($(A)!0.5!(B)$)--++(0:1)node[right](AN){};\n"%line_max
        strMux21="\\draw [-, line width=%dpt][align=center]($(O)!0.5!(A)$)--++(-90:2)node[below](){The number with mod A \\\\ equal to 0 is the output.};\n"%line_max
        strMux3="\\foreach \y/\\t in {0.2/2} {\n\\draw [-, line width=%dpt]($(C)! \y*1.1 !(O)$)--++(180:1) node[below](sel0){};}\n"%line_max
        strMux4="\\foreach \y/\\t in {0.7/7} {\n\\draw [-, line width=%dpt]($(C)! \y*1.1 !(O)$)--++(180:1) node[above](sel1){};}\n"%line_max
        strMux5="\\draw [->, line width=%dpt]($(out1)+(0.3,-0.5)$) -| (sel0);\n\\draw [->, line width=%dpt]($(out2)+(0.3,0.5)$) -| (sel1);\n"%(line_max,line_max)
        strOut="\\draw [->, line width=%dpt]($(AN)+(1,0)$) -- ++(2,0)node[right](Output){Output};\n"%(line_max)
        strDiv="\\node (rect) at ($(AN)+(0.4,0)$) [draw, thick,minimum width=1cm,minimum height=4cm] {$/%d$};\n"%A
        str_command=str_command+HstrPart+strPart+HstrConnect+strConnect+HstrConnect2+strConnect2+strMux1+strMux2+strMux21+strMux3+strMux4+strMux5+strOut+strDiv
    elif model_sel==3:
        model="BER"
        cbit=int((A-1)/2)
        Ra_array,Ta_array,Sa_array=TableTwo(A)
        index=1
        d=0.2
        strConnect="\\draw [-, line width=%dpt]"%(line_max)
        strPart=""
        for i in range(cbit):
            d_and2or=5*(int(cbit/9)+1)
            strOR1="\\node [or port] (OR%d) at ($(AND%d)+(%.1f,0)$){$%d$};\n"%(i,index,d_and2or,i)
            index=index+2
            findR=np.where(Ta_array==i)
            d=d+0.2
            if len(findR[0]) == 3:
                strOR2="\\draw [-, line width=%dpt][%s](AND%d.out)-- ++(%.1f,0) |- (OR%d.in 1);\n"%(line_min,color_name[(i%3)],findR[0][1],d,i)
                d=d+0.2
                strOR3="\\draw [-, line width=%dpt][%s](AND%d.out)-- ++(%.1f,0) |- (OR%d.in 2);\n"%(line_min,color_name[(i%3)],findR[0][2],d,i)
            else:
                strOR2="\\draw [-, line width=%dpt][%s](AND%d.out)-- ++(%.1f,0) |- (OR%d.in 1);\n"%(line_min,color_name[(i%3)],findR[0][0],d,i)
                d=d+0.2
                strOR3="\\draw [-, line width=%dpt][%s](AND%d.out)-- ++(%.1f,0) |- (OR%d.in 2);\n"%(line_min,color_name[(i%3)],findR[0][1],d,i)
            #
            strXOR1="\\node [xor port] (XOR%d) at ($(OR%d)+(5,-0.22)$){$%d$};\n"%(i,i,i)
            strXOR2="\\draw [-, line width=%dpt](OR%d.out) -| (XOR%d.in 1);\n"%(line_min,i,i)
            strXOR3="\\node (Input%d) at (XOR%d.in 2)[anchor=east]{$Input[%d]$};\n"%(i,i,i)
            #
            if i == (cbit-1):
                strConnect=strConnect+" (XOR%d.out);\n"%i
            else:
                strConnect=strConnect+" (XOR%d.out) -- "%i
            strPart=strPart+strOR1+strOR2+strOR3+strXOR1+strXOR2+strXOR3
        ha=int(cbit/2)-1
        strAN="\\draw [-, line width=%dpt](XOR%d.out) -- ++(1.5,0)node[right](AN){};\n"%(line_max,ha)
        strOut="\\draw [->, line width=%dpt]($(AN)+(1,0)$) -- ++(2,0)node[right](Output){Output};\n"%(line_max)
        strDiv="\\node (rect) at ($(AN)+(0.4,0)$) [draw, thick, minimum width=1cm,minimum height=4cm] {$/%d$};\n"%A
        str_command=str_command+strPart+strConnect+strAN+strOut+strDiv
    elif model_sel==4:
        model="AWE"
        cbit=int((A-1)/2)  
        Ra_array,Ta_array,Sa_array=TableTwo(A)
        index=1
        d=0.2
        strConnect="\\draw [-, line width=%dpt]"%(line_max)
        strPart=""
        for i in range(cbit):
            d_and2or=5*(int(cbit/9)+1)
            strOR1="\\node [or port] (OR%d) at ($(AND%d)+(%.1f,0)$){$%d$};\n"%(i,index,d_and2or,i)
            index=index+2
            findR=np.where(Ta_array==i)
            d=d+0.2
            if len(findR[0]) == 3:
                strOR2="\\draw [-, line width=%dpt][%s](AND%d.out)-- ++(%.1f,0) |- (OR%d.in 1);\n"%(line_min,color_name[(i%3)],findR[0][1],d,i)
                d=d+0.2
                strOR3="\\draw [-, line width=%dpt][%s](AND%d.out)-- ++(%.1f,0) |- (OR%d.in 2);\n"%(line_min,color_name[(i%3)],findR[0][2],d,i)
            else:
                strOR2="\\draw [-, line width=%dpt][%s](AND%d.out)-- ++(%.1f,0) |- (OR%d.in 1);\n"%(line_min,color_name[(i%3)],findR[0][0],d,i)
                d=d+0.2
                strOR3="\\draw [-, line width=%dpt][%s](AND%d.out)-- ++(%.1f,0) |- (OR%d.in 2);\n"%(line_min,color_name[(i%3)],findR[0][1],d,i)
            #
            #
            if i == (cbit-1):
                strConnect=strConnect+" (OR%d.out);\n"%i
            else:
                strConnect=strConnect+" (OR%d.out) -- "%i
            strPart=strPart+strOR1+strOR2+strOR3
        ha=int(cbit/2)-1
        strConnectName="\\draw [-, line width=%dpt](OR%d.out) -- ++(2,0)node[above](Error Bit){$Error Bit$};\n"%(line_max,ha)
        s1=np.where(Sa_array==1)
        strAdd1="\\draw [-, line width=%dpt] (AND%d.out) "%(line_max,s1[0][0])
        for z in range(len(s1[0])):
            strAdd1=strAdd1+"to [short,-*] (AND%d.out) "%(s1[0][z])
        strAdd1=strAdd1+";\n"
        strAdd2="\\node [or port,rotate=-90] (ORadd) at ($(AND%d.out) + (0.25,-2)$){$add$};\n"%(s1[0][-1])
        strAdd3="\\draw [-, line width=%dpt] (AND%d.out) to [short,-] (ORadd.in 2);\n"%(line_max,s1[0][-1])
        strAdd4="\\draw [-, line width=%dpt] (ORadd.in 1) -- (ORadd.in 2);\n"%(line_max)  

        strMux1="\\draw [-, line width=%dpt]($(OR%d)+(10,-2)$)coordinate (O)--++(30:1)coordinate (A)--++(90:4)coordinate (B)--++(150:1)coordinate (C)--cycle node[left](MUX){MUX};\n"%(line_min,ha)
        strMux2="\\draw [-, line width=%dpt]($(A)!0.5!(B)$)--++(0:1)node[right](AN){};\n"%line_max
        strMux3="\\draw [->, line width=%dpt](ORadd.out)-| ($(O)!0.5!(A)$);\n\\foreach \y/\\t in {0.2/2} {\n\draw [-, line width=%dpt]($(C)! \y*1.1 !(O)$)--++(180:1) node[left] {$Input+Error Bit$};}\n"%(line_max,line_max)
        strMux4="\\foreach \y/\\t in {0.7/7} {\n\draw [-, line width=%dpt]($(C)! \y*1.1 !(O)$)--++(180:1) node[left] {$Input-Error Bit$};}\n"%line_max
        
        strOut="\\draw [->, line width=%dpt]($(AN)+(1,0)$) -- ++(2,0)node[right](Output){Output};\n"%(line_max)
        strDiv="\\node (rect) at ($(AN)+(0.4,0)$) [draw, thick,minimum width=1cm,minimum height=4cm] {$/%d$};\n"%A
        str_command=str_command+strPart+strConnect+strConnectName+strAdd1+strAdd2+strAdd3+strAdd4+strMux1+strMux2+strMux3+strMux4+strOut+strDiv   
    else:
        print("NO this model!")
    ###
    str_command=str_command+"\\end{tikzpicture}\n\\end{preview}\n\\end{document}\n"
    #print(str_command)
    fnL="./"+path+"/"+model+str(A)+".tex"
    fn=model+str(A)+".tex"
    #if os.path.isfile(fn)==False:
    f=open(fn,"w")
    f.write("%s"%str_command)
    f.close()
    ###
    if pdfoRsvg == 0:
        fpdf=fnL[:-4]+".pdf"
        if os.path.isfile(fpdf)==False:
            os.system("xelatex %s"%fn)
    else:
        fpng=fnL[:-4]+".png"
        if os.path.isfile(fpng)==False:
            os.system("cd ./%s"%path)
            os.system("xelatex -no-pdf %s"%fn)
            os.system("dvisvgm --zoom=-1 --exact --font-format=woff %s.xdv"%fn[:-4])
            if SVGtoPNG == 1:
                cairosvg.svg2png(url="%s.svg"%fn[:-4], write_to="%s.png"%fn[:-4])
    return fn[:-4],fnL[:-4]
#fn1=AutoGenFig(A,model_sel,pdfoRsvg,SVGtoPNG,line_min,line_max)
# xelatex -no-pdf ./ANcodes_files/BER11.tex
# dvisvgm --zoom=-1 --exact --font-format=woff ./ANcodes_files/BER11.xdv
# ./ANcodes_files/BER11.svg
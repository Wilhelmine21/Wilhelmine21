# YourFileName="tmp"+".pdf"
YourFileName=input("YourFileName >> ")+".pdf"
from pdf2image import convert_from_path
images = convert_from_path(YourFileName)
for i in range(len(images)):
    if len(images) == 1:        
        images[i].save(YourFileName[:-4]+'.png', 'PNG')
    else:
        images[i].save(YourFileName[:-4]+'_page'+ str(i+1) +'.png', 'PNG')

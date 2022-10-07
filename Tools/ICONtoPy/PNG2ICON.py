# png to ico
from PIL import Image
FileName="Name"
InputFileName=FileName+".png"
OutputFileName=FileName+'.ico'
img = Image.open(InputFileName)
img.save(OutputFileName)

# svg2png
# import cairosvg
# FileName="start-illustration"
# InputFileName=FileName+".svg"
# OutputFileName=FileName+".png"
# cairosvg.svg2png(url=InputFileName, write_to=OutputFileName)

# Traceback (most recent call last):
#   File "C:\Users\Wilhelmine\Desktop\GitWork\Wilhelmine21\Tools\ICONtoPy\PNG2ICON.py", line 9, in <module>
#     import cairosvg
#   File "C:\Users\Wilhelmine\anaconda3\lib\site-packages\cairosvg\__init__.py", line 26, in <module>
#     from . import surface  # noqa isort:skip
#   File "C:\Users\Wilhelmine\anaconda3\lib\site-packages\cairosvg\surface.py", line 9, in <module>
#     import cairocffi as cairo
#   File "C:\Users\Wilhelmine\anaconda3\lib\site-packages\cairocffi\__init__.py", line 48, in <module>
#     cairo = dlopen(
#   File "C:\Users\Wilhelmine\anaconda3\lib\site-packages\cairocffi\__init__.py", line 45, in dlopen
#     raise OSError(error_message)  # pragma: no cover
# OSError: no library called "cairo-2" was found
# no library called "cairo" was found
# cannot load library 'C:\iverilog\gtkwave\bin\libcairo-2.dll': error 0x7f
# cannot load library 'libcairo.so.2': error 0x7e
# cannot load library 'libcairo.2.dylib': error 0x7e
# cannot load library 'libcairo-2.dll': error 0x7f
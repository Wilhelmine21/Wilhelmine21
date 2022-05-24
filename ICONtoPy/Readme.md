# Convert icon to python
1. import base64
```python:trans.py
import base64
```
2. Read the icon file
```python:trans.py
Inputfilename="name"+".ico"
# convert it to python
open_icon=open(Inputfilename,"rb")
b64str=base64.b64encode(open_icon.read())
open_icon.close()
```
3. Output the python file
```python:trans.py
# convert it to python
OutputFileName='name'+'.py'
write_data="img=%s"%b64str
f=open(OutputFileName,"w+")
f.write(write_data)
f.close()
```

# Import Your icon
1. import your python file
```python
from name import img
```
2. use base64 to decode it
```python
import base64
tmp=open("tmp.ico","wb+")
tmp.write(base64.b64decode(img))
tmp.close()
```
3. use iconbitmap
```python
root.iconbitmap("tmp.ico")
```
import base64
#
InputFileName="Name"+".ico"
OutputFileName='Name'+'.py'
#
open_icon=open(InputFileName,"rb")
b64str=base64.b64encode(open_icon.read())
open_icon.close()
#
write_data="img=%s"%b64str
f=open(OutputFileName,"w+")
f.write(write_data)
f.close()
from PIL import Image
InputFileName="Name"+".png"
OutputFileName='Name'+'.ico'

img = Image.open(InputFileName)
img.save(OutputFileName)
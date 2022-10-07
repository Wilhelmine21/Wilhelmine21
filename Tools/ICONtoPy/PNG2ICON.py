from PIL import Image
InputFileName="decoder"+".png"
OutputFileName='decoder'+'.ico'

img = Image.open(InputFileName)
img.save(OutputFileName)
import qrcode # here we are using qrcode library 
# to install this type pip install qrcode
# data is a variable which will take any data type
data=str(input("Enter the data"))
#img will create a qrcode using the given data
img=qrcode.make(data)
# line 8 Will Save your qrcode in the specified directory
img.save('/home/aamir/Pictures/myqrcode.png')

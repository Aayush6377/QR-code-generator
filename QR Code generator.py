import qrcode as qr
a=str(input("Enter link/content to store in QR code:"))
b=str(input("Do you want to change QR code colour (Y/N):"))
col1="black"
col2="white"
dim1=20
dim2=4
if (b.upper() in ["Y","YES"]):
    print("Note: Colour spelling should be correct otherwise it will not be implemented")
    col1=str(input("Enter QR code colour:"))
    col2=str(input("Enter background colour:"))
else:
    print("By default colour is black and white")

c=str(input("Do you want to change its dimensions:"))   
if (c.upper() in ["Y","YES"]):
    print("Note: By default box size is 20 and border is 4")
    dim1=int(input("Enter box size:"))
    dim2=int(input("Enter border width:"))
    
Q=qr.QRCode(border=dim2,box_size=dim1)
Q.add_data(a)
Q.add_data("\n\n")
Q.add_data("For more codes contact")
Q.add_data("\nE-mail: aayushkukreja0104@gmail.com")
Q.make(fit=True)
img=Q.make_image(fill_color=col1,back_color=col2)
name=str(input("Name your qr code:"))
ex="jpg"
print("By default extension is jpg")
e=str(input("Do you want to change your extension:"))
if e.upper() in ["Y","YES"]:
    ex=str(input("Enter extension:"))
img.save(name+"."+ex)


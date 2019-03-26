from PIL import Image
ascii_hua=list('●▲☆○')
OUTPUT='output4.txt'
WIDTH=50
HEIGHT=50
def get_char(r,g,b,alpha=256):  #rgb转字符
    if alpha==0:
        return ' '
    length=len(ascii_hua)
    gray=int(0.2126*r+0.7152*g+0.0722*b)
    unit=(256.0+1)/length
    return ascii_hua[int(gray/unit)]
im=Image.open('2.jpg')
im=im.resize((WIDTH,HEIGHT),Image.NEAREST)
txt=''
for i in range(HEIGHT):
    for j in range(WIDTH):
        txt += get_char(*im.getpixel((j,i)))
    txt+='\n'
print(txt)
with open(OUTPUT,'w') as f:
            f.write(txt)


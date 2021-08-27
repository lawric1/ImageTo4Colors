from PIL import Image

COLORS = [(10,45,34,255),
        (48,98,48,255),
        (101,141,78,255),
        (155,186,111,255),
        (0,0,0,0)]

imagePath = 'image.png'
im = Image.open(imagePath).convert('LA')
data = []

for lum_value in im.getdata(0):
    if lum_value == 0:
        data.append(COLORS[-1])

    elif lum_value < 50:
        data.append(COLORS[0])

    elif lum_value < 150:
        data.append(COLORS[1])

    elif lum_value <= 220:
        data.append(COLORS[2])

    else:
        data.append(COLORS[3])

new_im = Image.new('RGBA',im.size)
new_im.putdata(data)
new_im.save('New_' + imagePath)

new_im.show()
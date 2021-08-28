from PIL import Image
from random import randint

resolution_x = 100000 
resolution_y = int(resolution_x/2)
x, y, size = -0.60, 0.0, 2.0
step_x, step_y = (size*2)/resolution_x, size/resolution_y
imaginary, real = y + (size/2), x - size
MyImg = Image.new('RGBA', (resolution_x, resolution_y))
n = 0 


def mandelbrot(a, b):
    im, re = 0, 0
    for depth in range(766):
        im, re = b + (2 * im * re), a + (re**2 - im**2)
        if im**2 + re**2 > 4:
            return 0, depth
    return 1, 0

for a in range(resolution_y):
    real = x - size
    for b in range(resolution_x):
        pixel, color = mandelbrot(real, imaginary)
        if color < 256:
            MyImg.putpixel((b, a), (color, int(color/2), int(color/10), 255))
        elif color < 512:
            MyImg.putpixel((b, a), (int((color-255)/10), (color-255), int((color-255)/2), 255))
        else:
            MyImg.putpixel((b, a), (int((color-510)/2), int((color-510)/10), (color-510), 255))
        real = real + step_x
    imaginary = imaginary - step_y
    n += 1
    print(n)
picture_file = "D:\\Python\\" + str(randint(1,10000000000)) + "_mandelbrot.png"
MyImg = MyImg.save(picture_file)
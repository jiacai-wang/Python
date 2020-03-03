import cv2
import numpy
def byteAt(file, index):
    file.seek(int(index), 0)
    return ord(file.read(1))

f = open('./rgb.yuv','rb')
width = 480
height = 320
rgb = numpy.zeros((height,width,3))

for h in range(height):
    for w in range(width):
        # needs correction!!!
        # R = Y + 1.402 * (V-128)
        # G = Y - 0.34414 * (U-128) - 0.71414 * (V-128)
        # B = Y + 1.772 * (U-128)


        Y = byteAt(f, h*width+w)
        U = byteAt(f, width*height + int(h/2)*width/2 + int(w/2))
        V = byteAt(f, int(width*height*1.25) + int(h/2)*width/2 + int(w/2))
        Y = Y - 128

        rgb[h, w, 2] = int(Y + 1.402 * (V-128))
        if rgb[h, w, 2] > 255:
            rgb[h, w, 2] = 255
        elif rgb[h, w, 2] < 0:
            rgb[h, w, 2] = 0

        rgb[h, w, 1] = int(Y - 0.34414 * (U-128) - 0.71414 * (V-128))
        if rgb[h, w, 1] > 255:
            rgb[h, w, 1] = 255
        elif rgb[h, w, 1] < 0:
            rgb[h, w, 1] = 0
        
        rgb[h, w, 0] = int(Y + 1.772 * (U-128))
        if rgb[h, w, 0] > 255:
            rgb[h, w, 0] = 255
        elif rgb[h, w, 0] < 0:
            rgb[h, w, 0] = 0

cv2.imshow('rgb', rgb)
cv2.waitKey()
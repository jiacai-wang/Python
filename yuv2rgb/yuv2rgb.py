import cv2
import numpy
import struct


def byteAt(file, index):
    file.seek(int(index), 0)
    return ord(file.read(1))


f = open('./rgb.yuv', 'rb')
width = 480
height = 320
rgb = numpy.zeros((height, width, 3), dtype=numpy.uint8)
rgbraw = open('./rgbraw.rgb', 'wb')

for h in range(height):
    for w in range(width):
        # needs correction!!!
        # R = Y + 1.402 * (V-128)
        # G = Y - 0.34414 * (U-128) - 0.71414 * (V-128)
        # B = Y + 1.772 * (U-128)

        # Google
        # *r = yValue + (1.370705 * (vValue-128));
        # *g = yValue - (0.698001 * (vValue-128)) - (0.337633 * (uValue-128));
        # *b = yValue + (1.732446 * (uValue-128));

        # FourCC
        # B = 1.164*(Y - 16) + 2.018*(U - 128)
        # G = 1.164*(Y - 16) - 0.813*(V - 128) - 0.391*(U - 128)
        # R = 1.164*(Y - 16) + 1.596*(V - 128)

        Y = byteAt(f, h*width+w)
        U = byteAt(f, width*height + int(h/2)*width/2 + int(w/2))
        V = byteAt(f, int(width*height*1.25) + int(h/2)*width/2 + int(w/2))

        tmp = 1.164*(Y - 16) + 2.018*(U - 128)
        rgb[h, w, 0] = max(min(tmp, 255), 0)
        tmp = 1.164*(Y - 16) - 0.813*(V - 128) - 0.391*(U - 128)
        rgb[h, w, 1] = max(min(tmp, 255), 0)
        tmp = 1.164*(Y - 16) + 1.596*(V - 128)
        rgb[h, w, 2] = max(min(tmp, 255), 0)

        rgbraw.write(struct.pack("B", (rgb[h, w, 0])))
        rgbraw.write(struct.pack("B", (rgb[h, w, 1])))
        rgbraw.write(struct.pack("B", (rgb[h, w, 2])))
rgbraw.close()
cv2.imshow('rgb', rgb)
cv2.waitKey()

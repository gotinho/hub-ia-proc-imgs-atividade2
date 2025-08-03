import cv2
import numpy as np


def rotation(value, img):
    rows, cols = img.shape
    center = ((cols - 1) / 2.0, (rows - 1) / 2.0)
    scale = 1
    m = cv2.getRotationMatrix2D(center, value, scale)
    return cv2.warpAffine(img, m, (cols, rows))


def scale(value, img):
    return cv2.resize(img, None, fx=value, fy=value, interpolation=cv2.INTER_CUBIC)


def shear(value_h, value_v, img):
    rows, cols = img.shape
    sh = 0
    sv = 0
    if value_h < 0:
        sh = int(abs(value_h) * rows)
    if value_v < 0:
        sv = int(abs(value_v) * cols / 2)
    m = np.float32([[1, value_v, sv], [value_h, 1, sh], [0, 0, 1]])
    width = int(cols * (1.0 + abs(value_v / 2)))
    heigth = int(rows * (1.0 + abs(value_h)))
    return cv2.warpPerspective(img, m, (width, heigth))


def brightness(value, img):
    return cv2.add(img, value)


def contrast(value, img):
    return cv2.multiply(img, value)


def intensity(value, img):
    c = 255
    gamma = value
    r = img / 255.0
    res = c * np.power(r,gamma)
    return np.uint8(res)


def negative(img):
    return 256 - 1 - img

import cv2 as cv


def read_image(image_path):
    return cv.imread(image_path, cv.IMREAD_COLOR)

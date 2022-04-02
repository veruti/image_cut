import cv2 as cv
import numpy as np


def write_image(filename: str, image: np.array):
    cv.imwrite(filename=filename, img=image)

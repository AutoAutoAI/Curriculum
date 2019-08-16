import numpy as np
import cv2


def to_gray(img):
    """
    Converts the image `img` from an RGB image to a grayscale image.
    """
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return gray_img

def resize(img):
    """
    Our training set images were captured at a resolution of 160x128, therefore it
    is important that we scale our images here to that size before doing any of the
    other preprocessing. That is what this function does: resize the image `img` to
    be 160x128 pixels.
    """
    width, height = 160, 128
    small_img = cv2.resize(img, (width, height))
    return small_img

def crop(img):
    """
    We only want to keep the bottom 70 rows of pixels of the image. 
    We throw away the rows of pixels at the top of the image.
    That's what this function does; it returns only the bottom
    70 rows of pixels from the image `img`.
    """
    height = 70
    return img[-height:, :]

def edges(img):
    """
    This function takes a grayscale image `img` and runs
    the Canny edge detection algorithm on it. The returned
    image will be black and white, where the white parts are
    the edges of the original image `img`.
    """
    canny_thresh_1, canny_thresh_2 = 100, 200
    return cv2.Canny(img, canny_thresh_1, canny_thresh_2)

def preprocess(img):
    """
    This function runs all the functions above, and in the correct order!
    """
    img_edge = edges(resize(to_gray(img)))
    img_feats = crop(np.expand_dims(img_edge, 2))
    img_feats = np.array(img_feats, dtype=np.float32) / 255.0
    img_feats = np.expand_dims(img_feats, axis=0)
    return img_edge, img_feats

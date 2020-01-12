# blur_2.py

from cv2 import cv2
import numpy as np
import time


def blur_with_numpy_vectorization(input_filename, output_filename=None):
    """This function blurs an jpg image 

    The input file is first stored as a 3-dimensional numpy array (H,W,C),
    where H is the height, W is the width and C is the channels of the image.
    The image (H,W,C) is blurred by by applying convolution with an averaging 
    kernel. This means, for each pixel in the image, the corresponding pixel 
    in the blurred image is set to be an average of the pixel values in the 
    neighboring pixels. This is achieved by padding the image with 1 pixel on 
    each edge and using numpy arrays to find the average. 
    Resulting blurred image is saved in the output file if specified by the user.     

    Args:
        input_filename (str): Input file name
        output_filename (str, optional): Output file name. Defaults to none.

    Returns:
        dst_img (ndarray): numpy array of blurred image
    """
    src_img = cv2.imread(input_filename)
    dst_img = np.empty(src_img.shape)

    src_img_padded = np.pad(src_img,
                            ((1, 1), (1, 1), (0, 0)),
                            'edge')

    max_h = src_img.shape[0]            # original image height in pixels
    max_w = src_img.shape[1]            # original image width in pixels

    # covert to larger dtype to avoid overflow error when adding
    src_img_padded = src_img_padded.astype('uint32')

    neighbours_above_left = src_img_padded[0:max_h,   0:max_w, ]
    neighbours_above = src_img_padded[0:max_h,   1:max_w+1, ]
    neighbours_above_right = src_img_padded[0:max_h,   2:max_w+2, ]
    neighbours_right = src_img_padded[1:max_h+1, 2:max_w+2, ]
    neighbours_below_right = src_img_padded[2:max_h+2, 2:max_w+2, ]
    neighbours_below = src_img_padded[2:max_h+2, 1:max_w+1, ]
    neighbours_below_left = src_img_padded[2:max_h+2, 0:max_w, ]
    neighbours_left = src_img_padded[1:max_h+1, 0:max_w, ]

    dst_img = (
        neighbours_above_left
        + neighbours_above
        + neighbours_above_right
        + neighbours_left
        + src_img
        + neighbours_right
        + neighbours_below_left
        + neighbours_below
        + neighbours_below_right
    ) / 9

    dst_img = dst_img.astype('uint8')

    if (output_filename):
        cv2.imwrite(output_filename, dst_img)

    return dst_img


if __name__ == '__main__':
    import blur_1
    blur_1.measure_and_log_time(
        blur_1.blur_with_pure_python, 'beatles.jpg', report_filename='report_2.txt')
    blur_1.measure_and_log_time(blur_with_numpy_vectorization,
                                'beatles.jpg', report_filename='report_2.txt')

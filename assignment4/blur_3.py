# blur_1.py

from cv2 import cv2
import numpy as np
import time

from numba import jit


def blur_with_numba_support(input_filename, output_filename=None):
    """This function blurs an jpg image 

    The input file is first stored as a 3-dimensional numpy array (H,W,C),
    where H is the height, W is the width and C is the channels of the image.
    The image (H,W,C) is blurred by by applying convolution with an averaging 
    kernel. This means, for each pixel in the image, the corresponding pixel 
    in the blurred image is set to be an average of the pixel values in the 
    neighboring pixels. This is achieved by padding the image with 1 pixel on 
    each edge and using and inner function predefined by @jit and
    python for loops with numba to find the average. Resulting 
    blurred image is saved in the output file if specified by the user.     

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

    max_h = src_img_padded.shape[0]
    max_w = src_img_padded.shape[1]
    max_c = 3

    # convert to higher dtype to avoid overflow error
    src_img_padded = src_img_padded.astype('uint32')

    @jit
    def jitloop(src, dst, h, w, c):
        for h in range(1, h-1):
            for w in range(1, w-1):
                for c in range(0, c):
                    dst[h-1, w-1, c] = (                # averaging the colour c for
                        # the pixel at (h, w) and its neighbours at
                        src[h, w, c]
                        + src[h-1, w-1, c]       # above-left
                        + src[h-1, w, c]         # above
                        + src[h-1, w+1, c]       # above-right
                        + src[h, w+1, c]         # right
                        + src[h+1, w+1, c]       # below-right
                        + src[h+1, w, c]         # below
                        + src[h+1, w-1, c]       # below-left
                        + src[h, w-1, c]         # left
                    ) / 9

    jitloop(src_img_padded, dst_img, max_h, max_w, max_c)
    dst_img = dst_img.astype('uint8')

    if (output_filename):
        cv2.imwrite(output_filename, dst_img)

    return dst_img


if __name__ == '__main__':
    import blur_1
    import blur_2

    blur_1.measure_and_log_time(
        blur_1.blur_with_pure_python, 'beatles.jpg', report_filename='report_3.txt')
    blur_1.measure_and_log_time(
        blur_2.blur_with_numpy_vectorization, 'beatles.jpg', report_filename='report_3.txt')
    blur_1.measure_and_log_time(blur_with_numba_support,
                                'beatles.jpg', report_filename='report_3.txt')

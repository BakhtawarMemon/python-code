# blur_1.py

from cv2 import cv2
import numpy as np
import time


def blur_with_pure_python(input_filename, output_filename=None):
    """This function blurs an jpg image 

    The input file is first stored as a 3-dimensional numpy array (H,W,C),
    where H is the height, W is the width and C is the channels of the image.
    The image (H,W,C) is blurred by applying convolution with an averaging 
    kernel. This means, for each pixel in the image, the corresponding pixel 
    in the blurred image is set to be an average of the pixel values in the 
    neighboring pixels. This is achieved by padding the image with 1 pixel on each edge and
    using python for loops to find the average. 
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

    max_h = src_img_padded.shape[0]
    max_w = src_img_padded.shape[1]
    # nr. of colour channels (B, G, R)
    max_c = 3

    # convert to higher dtype to avoid overflow error
    src_img_padded = src_img_padded.astype('uint32')

    for h in range(1, max_h-1):
        for w in range(1, max_w-1):
            for c in range(0, max_c):
                dst_img[h-1, w-1, c] = (                # averaging the colour c for
                    # the pixel at (h, w) and its neighbours at
                    src_img_padded[h, w, c]
                    + src_img_padded[h-1, w-1, c]       # above-left
                    + src_img_padded[h-1, w, c]         # above
                    + src_img_padded[h-1, w+1, c]       # above-right
                    + src_img_padded[h, w+1, c]         # right
                    + src_img_padded[h+1, w+1, c]       # below-right
                    + src_img_padded[h+1, w, c]         # below
                    + src_img_padded[h+1, w-1, c]       # below-left
                    + src_img_padded[h, w-1, c]         # left
                ) / 9

    dst_img = dst_img.astype('uint8')

    if (output_filename):
        cv2.imwrite(output_filename, dst_img)

    return dst_img


def measure_and_log_time(function, input_image_filename, report_filename=None):
    """
    Function to print blur an image, print results and create a report

    Args:
        function (str): a function to be used on the image
        input_filename (str): Input filename
        output_filename (str, optional): Output file name. Defaults to none.

    """
    # measure time
    start_time = time.time()
    dst_img_arr = function(input_image_filename)  # Uses function as parameter
    end_time = time.time()

    # log time
    msg = "Log timestamp: {} -- {}() -- image size (H, W, C): {} -- time taken (s): {}".format(time.time(), function.__name__,
                                                                                               dst_img_arr.shape, end_time-start_time)
    if (report_filename):
        f = open(report_filename, 'a')
        f.write(msg + '\n')
        f.close

    # log to console
    print(msg)


if __name__ == '__main__':
    measure_and_log_time(blur_with_pure_python, 'beatles.jpg')

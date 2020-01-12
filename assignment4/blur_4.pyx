# blur_1.py

import cv2
import numpy as np 
import time 
cimport numpy as np


cpdef np.ndarray[np.double_t, ndim=3] blur_with_cython_support(str input_filename, str output_filename=None):
    """This function blurs an jpg image 

    The input file is first stored as a 3-dimensional numpy array (H,W,C),
    where H is the height, W is the width and C is the channels of the image.
    The image (H,W,C) is blurred by by applying convolution with an averaging 
    kernel. This means, for each pixel in the image, the corresponding pixel 
    in the blurred image is set to be an average of the pixel values in the 
    neighboring pixels. This is achieved by padding the image with 1 pixel on 
    each edge and using cython to find the average. Resulting 
    blurred image is saved in the output file if specified by the user.     

    Args:
        input_filename (str): Input file name
        output_filename (str, optional): Output file name. Defaults to none.

    Returns:
        dst_img (ndarray): numpy array of blurred image
    """
    cdef src_img = cv2.imread(input_filename)
    dst_img = np.zeros(src_img.shape, dtype=np.intc)
    cdef int [:, :, :] temp_dst_img = dst_img

    src_img_padded = np.pad(src_img, 
        ((1, 1), (1, 1), (0, 0)),                       
        'edge')                                         

    cdef int max_h = src_img_padded.shape[0]         
    cdef int max_w = src_img_padded.shape[1]
    cdef int max_c = 3                                           # nr. of colour channels (B, G, R)

    src_img_padded = src_img_padded.astype('uint32')    # convert to higher dtype to avoid overflow error
    cdef unsigned int [:, :, :] c_src_padded = src_img_padded
    cdef int h, w, c

    for h in range(1, max_h-1):
        for w in range(1, max_w-1):
            for c in range(0, max_c): 
                dst_img[h-1, w-1, c] = (                # averaging the colour c for 
                    c_src_padded[h, w, c]             # the pixel at (h, w) and its neighbours at  
                    + c_src_padded[h-1, w-1, c]       # above-left
                    + c_src_padded[h-1, w, c]         # above 
                    + c_src_padded[h-1, w+1, c]       # above-right 
                    + c_src_padded[h, w+1, c]         # right 
                    + c_src_padded[h+1, w+1, c]       # below-right 
                    + c_src_padded[h+1, w, c]         # below 
                    + c_src_padded[h+1, w-1, c]       # below-left 
                    + c_src_padded[h, w-1, c]         # left 
                ) / 9

    dst_img = dst_img.astype('uint8')

    if (output_filename):
        cv2.imwrite(output_filename, dst_img)

    return dst_img


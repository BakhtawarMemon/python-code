# blur.py

import argparse

import blur_1
import blur_2
import blur_3
import blur_4

parser = argparse.ArgumentParser(
    description='Blurs an input (JPG) image using the specified method.')
parser.add_argument('-m', '--blur_method', type=str,
                    help='Method to use for blurring: \n\t pure python (python), \n numpy vectorization (numpy), \n python with numba support (numba)', required=True)
parser.add_argument('-i', '--input_filename', type=str,
                    help='Input filename, e.g., myimage.jpg', required=True)
parser.add_argument('-o', '--output_filename', type=str,
                    help='Output filename, e.g., myimage_blur.jpg', required=False)

args = parser.parse_args()

if (args.blur_method == 'python'):
    blurred_img = blur_1.blur_with_pure_python(
        args.input_filename, args.output_filename)
elif (args.blur_method == 'numpy'):
    blurred_img = blur_2.blur_with_numpy_vectorization(
        args.input_filename, args.output_filename)
elif (args.blur_method == 'numba'):
    blurred_img = blur_3.blur_with_numba_support(
        args.input_filename, args.output_filename)
elif (args.blur_method == 'cython'):  # Added functionality for cython
    blurred_img = blur_4.blur_with_cython_support(
        args.input_filename, args.output_filename)

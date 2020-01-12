import numpy as np
import time

from blur_4 import blur_with_cython_support

if __name__ == '__main__':
    import blur_1
    import blur_2
    import blur_3

    blur_1.measure_and_log_time(
        blur_1.blur_with_pure_python, 'beatles.jpg', report_filename='report_4.txt')
    blur_1.measure_and_log_time(
        blur_2.blur_with_numpy_vectorization, 'beatles.jpg', report_filename='report_4.txt')
    blur_1.measure_and_log_time(
        blur_3.blur_with_numba_support, 'beatles.jpg', report_filename='report_4.txt')
    blur_1.measure_and_log_time(
        blur_with_cython_support, 'beatles.jpg', report_filename='report_4.txt')

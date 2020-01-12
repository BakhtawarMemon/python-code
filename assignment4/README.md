4.1 The script blur_1.py has function blur_with_pure_python(input_filename, output_filename=None)
The script is run as `python blur_1.py`
It will show the time taken to blur the input file on the console.

4.2 The script blur_2.py has function blur_with_numpy_vectorization(input_filename, output_filename=None)
The script is run as python blur_2.py
It will generate performance report on blur_1 and blur_2 (report_2.txt)

4.3 The script blur_3.py has function blur_with_numba_support(input_filename, output_filename=None)
The script is run as python blur_3.py
It will generate performance report on blur_1 blur_2 and blur_3 (report_3.txt)
4.4 The script blur_4.pyx has function blur_with_cython_support(input_filename, output_filename=None)
It is cythonize in blur_4_setup file. Run python blur_4_setup.py build_ext --inplace.

    The script blur_4.py imports blur_with_cython_support from blur_4.
    The script is run as python blur_4.py
    It will generate performance report on blur_1, blur_2, blur_3 and blur_4

4.5 The script blur.py is user interface for blur
Type python blur.py --help

4.6 The script setup.py has function blur_image(input_filename, output_filename=None)
The script is run as python setup.py

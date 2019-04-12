# How to run it?

execute:
```
$ python3 run.py
```
and it will display interactive prompt to select algorithms and input image

# How to add an algorithm?

add a file in `alg` directory, containing a callable/function named `convert`.

The function should receive the ndarray of the image as its only argument, and return the processed ndarray.

(the `do_nothing.py` can be used as a template)

After adding the file, it will be detected by the interactive prompt.

# Program structure

`output`: all output images will be written to this directory in png format
`input`: all input images are stured in this directory
`utility`: this contains utility functions such as `readImage`, `writeImage`, etc.
`alg`: this contains all algorithms used to convert images
`run.py`: this should be the entry point of the entire program where it is executed.

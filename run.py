import sys
import os
import glob
from utility import readImage, writeImage, pickFrom, shorten, inputDir, outputDir

# pick an algorithm
me = os.path.realpath(__file__) # full path to the current file
match = os.path.join(os.path.dirname(me), 'alg', '*.py') # same as './src/*.py'
algorithms = glob.glob(match) # find all algorithms e.g. 'xxx/xxx/xxx/example.py'
shortened_algorithms = [shorten(f) for f in algorithms] # 'example'

selected_algorithm = pickFrom(shortened_algorithms, prompt="Pick one algorithm")

try:
    sys.path.append("alg")
    alg = __import__(selected_algorithm)
    func = alg.convert
except ImportError as e:
    print("{} doesn't exist".format(selected_algorithm))
    exit(-1)
except AttributeError as e:
    print("{} doesn't contain a 'convert' callable".format(selected_algorithm))
    exit(-1)

# pick an input file

match = os.path.join(inputDir, "*") # same as './input/*'
input_files = glob.glob(match)

selected_input_file = pickFrom(input_files, prompt="Pick one input image", shortener=shorten)

try:
    arr = readImage(selected_input_file)
    arr = func(arr)
    output_file = os.path.join(outputDir, "{}.png".format(shorten(selected_input_file)))

    writeImage(output_file, arr)
except Exception as e:
    print(e)
    raise e
print("Successfully write output file to {}".format(output_file))

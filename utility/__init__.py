""" The utility file """
import os
from matplotlib import pyplot
baseDir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
inputDir = os.path.join(baseDir, "input")
outputDir = os.path.join(baseDir, "output")

def readImage(filename, fmt=None):
    """ filename is a file's name residing in the input directory 
    returns a numpy.ndarray object """
    fileUrl = os.path.join(inputDir, filename)
    return pyplot.imread(fileUrl, fmt)

def writeImage(filename, array):
    """ filename is the desired filename to write to, in output directory
    array is an numpy.ndarray object containing the image data """
    fileUrl = os.path.join(outputDir, filename)
    pyplot.imsave(fileUrl, array)

def pickFrom(lst, prompt="Pick from one below", shortener=None):
    """ Ask user to pick from a list interactively """
    print(prompt)
    for i, f in enumerate(lst):
        f = shortener(f) if shortener else f
        print("{}:\t{}".format(i, f))
    while True:
        idx = input("Enter a number between 0 and {} => ".format(len(lst)-1))
        try:
            idx = int(idx)
        except ValueError as e:
            print("Please enter a valid number")
            continue
        if idx < 0 or idx >= len(lst):
            print("Please enter a number in the correct range")
            continue
        break
    print("{} selected".format(idx))
    return lst[idx]

def shorten(longname):
    shortname = os.path.splitext(os.path.split(longname)[1])[0] # only keep the file name
    return shortname

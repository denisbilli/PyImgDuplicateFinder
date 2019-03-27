#coding=utf-8

import argparse
import os
import pathlib
import shutil
from PIL import Image
import imagehash
import glob
import ntpath
import sys
from haarPsi import haar_psi_numpy
import numpy

threshold = 0.5
input_path = ""
mode = "S"

parser = argparse.ArgumentParser(description='Process a folder of images finding the duplicates.\nThe entire process'
                                             'can be done both with a soft algorithm that simply hashes the images and'
                                             'a hard one that check for the similarity with a threshold. The duplicates'
                                             'are move to a duplicate folder inside the checked one.')

parser.add_argument('-dir', required=True, help='the folder to check')
parser.add_argument('-mode', nargs='?', default="S", help='the using mode desired (H = Hard, S = soft)')
parser.add_argument('-t', nargs='?', default=0.5, help='the threshold of similarity. a value between 0 and 1. '
                                                       'the default is 0.5. only works with Hard Mode')

args = parser.parse_args()

mode = args.mode
input_path = args.dir
threshold = args.t
output_path = input_path + "\\duplicated"


if not pathlib.Path(output_path).exists():
    os.mkdir(output_path)


def soft_mode():
    global file_moved

    file_moved = 0
    list = []
    i = 0
    for imagePath in glob.glob(input_path + "\\*.jpg"):
        image = Image.open(imagePath)

        basename = ntpath.basename(imagePath)
        h = str(imagehash.dhash(image))

        iFile = pathlib.Path(imagePath)
        oFile = pathlib.Path(output_path + "\\" + basename)

        if list.count(h) > 0:
            shutil.move(iFile.as_posix(), oFile.as_posix())
            file_moved += 1
        else:
            list.append(h)
            sys.stdout.write("\rChecking file #%i: %s " % (i, basename))
            sys.stdout.flush()
            i += 1
    return file_moved


def hard_mode():
    global threshold

    file_moved = 0
    images = []
    i = 1
    size = 128, 128
    # Deep fingerprinting with Haar Wavelet-Based Perceptual Similarity Index (HaarPSI)
    for imagePath in glob.glob(input_path + "\\*.jpg"):
        image = Image.open(imagePath)
        image.thumbnail(size, Image.ANTIALIAS)
        np_image = numpy.asarray(image)
        basename = ntpath.basename(imagePath)
        to_move = False

        iFile = pathlib.Path(imagePath)
        oFile = pathlib.Path(output_path + "\\" + basename)

        for saved_image in images:
            try:
                result = haar_psi_numpy(saved_image, np_image, True)
                if result[0] > threshold:
                    to_move = True
                    break
            except:
                continue

        if to_move:
            shutil.move(iFile.as_posix(), oFile.as_posix())
            file_moved += 1
        else:
            images.append(np_image)
            sys.stdout.write("\rChecking file #%i: %s " % (i, basename))
            sys.stdout.flush()
            i += 1

    return file_moved


if mode == "H":
    file_moved = hard_mode()
else:
    file_moved = soft_mode()

print("\n\nTotal file moved: " + str(file_moved))
# PyImgDuplicateFinder
A simple script to find and move duplicate images inside a folder using HaarPSI algorithm

## Usage:
Process a folder of images finding the duplicates. The entire processcan be
done both with a soft algorithm that simply hashes the images anda hard one
that check for the similarity with a threshold. The duplicatesare move to a
duplicate folder inside the checked one.

From the bash/command line just call the script move-by-fingerprint.py

### Command line arguments:

|arg|meaning|description|
|:-|:-|:-|
|-h, -help|[HELP]|shows the help message and exits|
|-dir|DIR|the folder to check|
|-mode &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|[MODE]| the using mode desired (H = Hard, S = soft)|
|-t|[T]|the threshold of similarity. a value between 0 and 1. the default is 0.5. only works with Hard Mode|

## Credits:
The HaarPSI algorithm has been downloaded from http://www.haarpsi.org/

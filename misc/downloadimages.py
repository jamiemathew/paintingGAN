## Assuming a csv file has:
## Image Name (ImageID) in column 1 (line[0])
## Full Resolution URL (OriginalURL) in column 3 (line[2])

import sys
import urllib.request
from csv import reader
import os.path
# from download_images_from_csv import * 

def open_images(csv_filename):
    with open(csv_filename+".csv".format(csv_filename), 'r') as csv_file:
        for line in reader(csv_file):
            if os.path.isfile("fullimages/" + line[0] + ".jpg"):
                print ("Image skipped for {0}")
            else:
                if line[2] != '' and line[0] != "ImageID":
                    urllib.request.urlretrieve(line[2], "fullimages/" + line[0] + ".jpg")
                    print (line[2])
                    print ("Image saved")
                else:
                    print ("No result for {0}")
                    
open_images("vgdb_2016")
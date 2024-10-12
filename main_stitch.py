#https://youtube.com/watch?v=v9JARVu74CI&t=14s <- A cool source
#https://github.com/OpenStitching/stitching <- also used, and carried
#https://dronemapper.com/sample_data/ <- sample data
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import cv2 as cv

#Magic show images code
def plot_image(img, figsize_in_inches=(5,5)):
    fig, ax = plt.subplots(figsize=figsize_in_inches)
    ax.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.show()
    
def plot_images(imgs, figsize_in_inches=(5,5)):
    fig, axs = plt.subplots(1, len(imgs), figsize=figsize_in_inches)
    for col, img in enumerate(imgs):
        axs[col].imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.show()

#FOR TESTING SPEED, will not show an actual image (well it shouldn't)
#This is a copy of the expanded code above
#number_of_photos is like for loop range
def stitch_method_TJ(photo_sample_folder, number_of_photos):
    
    imagefiles = glob.glob(photo_sample_folder + "\\*")
    imagefiles.sort()
    images = []
    for i in range(number_of_photos[0],number_of_photos[1]):
        filename = imagefiles[i]
        #OpenCV + Vscode = files? idk man cant see
        #Solution, use another library to say that the path actually exists
        file_name = os.path.join(os.path.dirname(__file__), filename)
        assert os.path.exists(file_name)
        #imread, reads a file. shocking
        #1 = Color Image
        #0 = Grayscale
        #-1 = Includes Alpha Channel
        img = cv2.imread(filename)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        images.append(img)
    from stitching import Stitcher
    '''
    for detector, brisk or sift seem to not cause error Idk difference
    brisk seems to give better results? maybe forces more data to be kept
    akaze and orb are also options?? has a bunch of errors
    matches_graph_dot_file prints analysis (1 or not inputed)
    KEEP CROP FALSE, the data loss with it true basically ruins the point when using low sample sizes
    blender_type seems to have no effect (multiband or feather)
    n_features also doesnt do anything what??? (int > 0)
    '''
    settings = {"try_use_gpu": True,
                "crop":False,
                "detector": "brisk",
                "confidence_threshold": 0.0002,
                "matches_graph_dot_file": None
                }
    stitcher = Stitcher(**settings)
    panorama = stitcher.stitch(images)
    plot_image(panorama)
    #plot_images([panorama] + images)

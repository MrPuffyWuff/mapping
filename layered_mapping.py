from main_stitch import stitch_method_TJ

def layer_main():
    print("\n--------------------\n")
    total_images = 100
    for i in range(0, total_images, 10):
        stitch_method_TJ("SamplePhotos\\Images", [0 + i,10 + i], -1, new_pano_name = 'LayerCache\\' + str(i) + '_' + str(10 + i) + '.png', debug = False)
        print("Images: " + str(i) + ' to ' + str(10 + i) + " Stitched")
    print("\nRePackagingDone\n\n--------------------\n")
    stitch_method_TJ("LayerCache", [0, total_images/10], -1, debug = True)
    print("\nLayered Mapping Finished\n\n--------------------\n")
#layer_main()
stitch_method_TJ("SamplePhotos\\Images", [20,30], 1, debug=True)
from main_stitch import stitch_method_TJ
import time

def speed_test(folder, photos):
    start_time = time.time()
    stitch_method_TJ(folder, photos, 0)
    end_time = time.time()
    return end_time - start_time

def timing_main(max):
    print("\n--------------------\n")
    for i in range(2, max):
        print("Images Checked: " + str(i), end =" ")
        print( "Seconds: " + str(
            speed_test("SamplePhotos\\Images", [0,i])
            ))
    print("\Time Test Finished\n\n--------------------\n")

timing_main(10)
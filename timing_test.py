from main_stitch import stitch_method_TJ
import time

def speed_test(folder, photos):
    start_time = time.time()
    stitch_method_TJ(folder, photos)
    end_time = time.time()
    return end_time - start_time

def main():
    print("\n--------------------\n")
    for i in range(2, 15):
        print("Images Checked: " + str(i), end =" ")
        print( "Seconds: " + str(speed_test("SamplePhotos\\Images", i)) )

main()
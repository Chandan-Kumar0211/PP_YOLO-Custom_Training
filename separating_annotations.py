import glob
import os
import shutil

os.chdir('E:/PP_YOLO-Custom_Training/obj')
myfiles = glob.glob('*.txt')
#print(len(myfiles))
files = myfiles
for f in myfiles:
     shutil.copy(f,'E:/PP_YOLO-Custom_Training/txt_annotation')
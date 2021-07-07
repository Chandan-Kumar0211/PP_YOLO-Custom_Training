import os
import cv2

#
originLabelsDir = 'E:/PP_YOLO-Custom_Training/txt_annotation'
# Converted file save path
saveDir = 'E:/PP_YOLO-Custom_Training/label_coco_format/annos.txt'
# Picture path corresponding to the original label
originImagesDir = 'E:/PP_YOLO-Custom_Training/train_images'

txtFileList = os.listdir(originLabelsDir)
with open(saveDir, 'w') as fw:
    for txtFile in txtFileList:
        with open(os.path.join(originLabelsDir, txtFile), 'r') as fr:
            labelList = fr.readlines()
            for label in labelList:
                label = label.strip().split()
                x = float(label[1])
                y = float(label[2])
                w = float(label[3])
                h = float(label[4])

                # convert x,y,w,h to x1,y1,x2,y2
                imagePath = os.path.join(originImagesDir,
                                         txtFile.replace('txt', 'jpg'))
                image = cv2.imread(imagePath)
                H, W, _ = image.shape
                x1 = (x - w / 2) * W
                y1 = (y - h / 2) * H
                x2 = (x + w / 2) * W
                y2 = (y + h / 2) * H
                # In order to match the coco label method, the label serial number is calculated from 1
                fw.write(txtFile.replace('txt', 'jpg') + ' {} {} {} {} {}\n'.format(int(label[0]) + 1, x1, y1, x2, y2))

        print('{} done'.format(txtFile))

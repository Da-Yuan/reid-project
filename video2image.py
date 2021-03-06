import os
import re
import argparse
import cv2
from scipy.misc import imresize
import xml.etree.ElementTree as ET


def dirList(mainPath, allFileList):
    fileList = os.listdir(mainPath)
    for fileName in fileList:
        filePath = os.path.join(mainPath, fileName)
        if os.path.isdir(filePath):
            dirList(filePath, allFileList)
        else:
            allFileList.append(filePath)
    return allFileList


def readXml_saveROI(xmlName, imageFile, savePath, widthMin, heightMin):
    pathStr = re.split('/', imageFile)
    f = open(xmlName, 'rb')
    tree = ET.parse(f)
    imageName = tree.find('filename').text
    print(imageName)
    nameStr = re.split('_|\.', imageName)
    frame = nameStr[7].zfill(5)
    imagePath = imageFile + '/' + imageName
    srcImg = cv2.imread(imagePath)
    # image2 = imresize(image, 50, interp='cubic')
    objects = tree.findall('object')
    if len(objects) == 0:
        print(' - No objects.')
        return
    for index, object in enumerate(objects):
        className = object.find('name').text
        bbox = object.find('bndbox')
        x_min = int(bbox.find('xmin').text)
        x_max = int(bbox.find('xmax').text)
        width = x_max - x_min
        y_min = int(bbox.find('ymin').text)
        y_max = int(bbox.find('ymax').text)
        height = y_max - y_min
        if width < widthMin & height < heightMin:
            print('Skip tiny box.')
            continue
        print(' -', 'id:', className,
              'x:', x_min, '-', x_max,
              'y:', y_min, '-', y_max)

        cropImg = srcImg[y_min*2:y_max*2, x_min*2:x_max*2]
        saveFile = savePath + '/' + className + '_' + pathStr[2] + '_' + frame + '.jpg'
        cv2.imwrite(saveFile, cropImg)
        # cv2.imshow('crop', cropImg)

        # cv2.rectangle(image2, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 1)
        # cv2.imshow('bbox', image2)
        # cv2.waitKey(0)


def main(args):
    # 读入文件夹下所有xml
    allFiles = dirList(args.xmlPath, [])
    for i in range(len(allFiles)):
        readXml_saveROI(allFiles[i], args.imagePath, args.savePath, args.widthMin, args.heightMin)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--xmlPath', '-xp', type=str, default='../3/c60s2/Annotations')
    parser.add_argument('--imagePath', '-ip', type=str, default='../3/c60s2/JPEGImages')
    parser.add_argument('--savePath', '-sp', type=str, default='../bbox')
    parser.add_argument('--widthMin', '-wm', type=int, default=0)
    parser.add_argument('--heightMin', '-hm', type=int, default=0)
    main(parser.parse_args())

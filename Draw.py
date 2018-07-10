#coding:utf-8

import os
import cv2
from scipy.misc import imresize
import matplotlib.pyplot as plt
from readXml import read_xml_show, read_xml_show1
from dirStr import findStr


def drawALLpoints(DICT):
    plt.cla()
    COLOR = 'rgbcmykwr'
    KEYS = list(DICT.keys())
    for i in range(len(DICT)):
        # X = []
        # Y = []
        if KEYS[i] in DICT:
            tmp = list(set(DICT[KEYS[i]]))
            # tmp = list(set(DICT.get(KEYS[i])))
            if len(tmp) >= 1 and i < 8:
                for j in range(len(tmp)):
                    plt.plot(tmp[j][0], tmp[j][1], color=COLOR[i], marker='o')
                    plt.annotate(KEYS[i], xy=(tmp[0][0], tmp[0][1]), xytext=(tmp[0][0], tmp[0][1]))
            elif len(tmp) >= 1 and i >= 8:
                t = i % 8
                for j in range(len(tmp)):
                    plt.plot(tmp[j][0], tmp[j][1], color=COLOR[t], marker='o')
                    plt.annotate(KEYS[i], xy=(tmp[0][0], tmp[0][1]), xytext=(tmp[0][0], tmp[0][1]))
    plt.pause(0.2)

def drawALLpoints2(DICT):
    plt.cla()
    COLOR = 'rgbcmykrgbcmyk'
    # COLOR =   [ '#F0F8FF', '#FAEBD7', '#00FFFF',  '#F0FFFF',  '#F5F5DC',  '#FFE4C4',  '#000000',
    #    '#FFEBCD', '#0000FF',  '#A52A2A',  '#DEB887',  '#7FFF00',  '#D2691E',  '#FF7F50',  '#6495ED',
    #    '#FFF8DC', '#DC143C',  '#00FFFF', '#00008B',  '#008B8B', '#B8860B', '#006400', '#BDB76B',
    #     '#8B008B']
    KEYS = list(DICT.keys())
    count = 0
    for i in range(len(DICT)):
        # X = []
        # Y = []
        if KEYS[i] in DICT:
            tmp = list(set(DICT[KEYS[i]]))
            # tmp = list(set(DICT.get(KEYS[i])))
            if len(tmp) >= 1 and i < 8:
                for j in range(len(tmp)):
                    plt.plot(tmp[j][0], tmp[j][1], color=COLOR[i], marker='o')
                    plt.annotate(KEYS[i], xy=(tmp[0][0], tmp[0][1]), xytext=(tmp[0][0], tmp[0][1]))
            elif len(tmp) >= 1 and i >= 8:
                i = i % 8
                for j in range(len(tmp)):
                    plt.plot(tmp[j][0], tmp[j][1], color=COLOR[i], marker='o')
                    plt.annotate(KEYS[i], xy=(tmp[0][0], tmp[0][1]), xytext=(tmp[0][0], tmp[0][1]))
    plt.pause(0.2)


def Show_pictures(ImgPath, allfile, FINAL_GIS_DICT, FRAME_COUNT):
    for i in range(len(allfile)):
        picname = os.path.splitext(os.path.basename(allfile[i]))[0]
        image_path = ImgPath+'\\' + picname + ".jpg"
        img = cv2.imread(image_path)
        img = imresize(img, 50, interp='cubic')  # 50%
        if findStr(allfile[i], picname):  # 根据name找到对应的xml
            _, timeStamp1, ID, GIS, FINAL_GIS_DICT = read_xml_show(img, allfile[i], FINAL_GIS_DICT, FRAME_COUNT)  # 读取xml并画框
            if timeStamp1 != None:  #ID != [] and ID == []:
                cv2.imshow("result", img)
                # drawALLpoints(FINAL_GIS_DICT)  # GIS点
                # cv2.waitKey(0)


def Show_pictures2(ImgPath, galaryList, FINAL_GIS_DICT):
    for i in range(len(galaryList)):
        picname = os.path.splitext(os.path.basename(galaryList[i]))[0]
        image_path = ImgPath+'\\' + picname + ".jpg"
        img = cv2.imread(image_path)
        img = imresize(img, 50, interp='cubic')  # 50%
        if findStr(galaryList[i], picname):  # 根据name找到对应的xml
            _, timeStamp1, ID, GIS, FINAL_GIS_DICT = read_xml_show1(img, galaryList[i], FINAL_GIS_DICT)  # 读取xml并画框
            print(FINAL_GIS_DICT)
            print("字典长度： ", len(FINAL_GIS_DICT))
            if timeStamp1 != None: #ID != [] and ID == []:
                cv2.imshow("result2", img)
                # drawALLpoints2(FINAL_GIS_DICT) # GIS点
                # cv2.waitKey(0)
                # time.sleep(10)
#coding: utf-8

import argparse
import multiprocessing
from multiprocessing import Manager
from dirStr import dirList
from Draw import Show_pictures, Show_pictures2

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--xmlPath1', '-A1', type=str, dest='xmlPath1')
    parser.add_argument('--xmlPath2', '-A2', type=str, dest='xmlPath2')
    parser.add_argument('--ImagePath1', '-I1', type=str, dest='ImgPath1')
    parser.add_argument('--ImagePath2', '-I2', type=str, dest='ImgPath2')
    args = parser.parse_args()

    args.xmlpath1 = "../3/c60s2/Annotations"  # 第一个相机的xml
    args.ImgPath1 = "../3/c60s2/JPEGImages"  # 第一个相机的图片

    args.xmlpath2 = "../3/c68s2/Annotations"  # 第二个相机的xml
    args.ImgPath2 = "../3/c68s2/JPEGImages"  # 第二个相机的图片

    allfile = dirList(args.xmlpath1, [])  # 取出所有xml文件
    galaryList = dirList(args.xmlpath2, [])

    FINAL_GIS_DICT = Manager().dict()
    FRAME_COUNT = Manager().Value("NUM", 0)

    thread = []
    p1 = multiprocessing.Process(target=Show_pictures, args=(args.ImgPath1, allfile, FINAL_GIS_DICT, FRAME_COUNT))
    thread.append(p1)
    p2 = multiprocessing.Process(target=Show_pictures2, args=(args.ImgPath2, galaryList, FINAL_GIS_DICT))
    thread.append(p2)
    for i in thread:
        i.start()
    for i in thread:
        i.join()

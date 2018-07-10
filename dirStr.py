#coding: utf-8

import os
import re
# 递归查找路径下所有xml
def dirList(mainPath, allFileList):
    """
    :param mainPath:
    :param allFileList:  a list
    :return:
    """
    fileList = os.listdir(mainPath)
    for fileName in fileList:
        filePath = os.path.join(mainPath, fileName)
        if os.path.isdir(filePath):
            dirList(filePath, allFileList)
        else:
            allFileList.append(filePath)  #
    return allFileList


# 判断一个文件下是否包含一个固定的字符串
def findStr(fileName, keyWords):
    fp = open(fileName, 'r')
    for everyLine in fp:
        if re.search(keyWords, everyLine, re.I):
            return True
    return False
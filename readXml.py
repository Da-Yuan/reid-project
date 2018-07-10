#coding:utf-8

import cv2
import xml.etree.ElementTree as ET


def read_xml_show(img, xmlName, FINAL_GIS_DICT, FRAME_COUNT):
    f = open(xmlName, 'r')
    tree = ET.parse(f)
    root = tree.getroot()
    print("*" * 20)
    # global pictureName
    pictureName = root.find('filename').text
    print('fileName: ', pictureName)
    objs = tree.findall('object')
    count = 0
    timeStamp = None
    ID = []
    gis = []
    for idx, obj in enumerate(objs):
        className = obj.find('name').text
        print('clasName:  ', className)
        bbox = obj.find('bndbox')
        x_min = float(bbox.find('xmin').text)
        y_min = float(bbox.find('ymin').text)
        x_max = float(bbox.find('xmax').text)
        y_max = float(bbox.find('ymax').text)
        cv2.rectangle(img, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 1)
        cv2.putText(img, str(className[7:11]), (int(x_max), int(y_max)),cv2.FONT_HERSHEY_SIMPLEX, 0.4,  (0, 0, 255), 1)

        GIS = obj.find('reIdenInfo')
        if GIS == None:
            continue
        GIS_x = GIS.find('gis').find('x').text
        GIS_y = GIS.find('gis').find('y').text
        if (int(GIS_x[:-8]) < 100000000000) and (int(GIS_y[:-8]) < 100000000000):
            ID.append(className)  # 防止index超标
            GIS_x = float(GIS_x)
            GIS_y = float(GIS_y)
            gis.append([GIS_x, GIS_y])

            global class_name1
            class_name1 = str(className[7:11])  # 显示最后两位，否则标出gis点上的字重叠
            if class_name1 in FINAL_GIS_DICT.keys():
                tmp = FINAL_GIS_DICT[class_name1]
                tmp.extend([(GIS_x, GIS_y)])
                FINAL_GIS_DICT[class_name1] = tmp
            else:
                FINAL_GIS_DICT[class_name1] = [(GIS_x, GIS_y)]
            if FRAME_COUNT.value != -1:
                FRAME_COUNT.value += 1
                if FRAME_COUNT.value % 50 == 0:
                    KEYS = list(FINAL_GIS_DICT.keys())
                    for i in range(len(FINAL_GIS_DICT)):
                        tmp = list(set(FINAL_GIS_DICT[KEYS[i]]))
                        if len(tmp) < 10:
                            FINAL_GIS_DICT.pop(KEYS[i])
                elif FRAME_COUNT.value % 200 == 0:
                    KEYS = list(FINAL_GIS_DICT.keys())
                    for i in range(len(FINAL_GIS_DICT)):
                        tmp = list(set(FINAL_GIS_DICT[KEYS[i]]))
                        if len(tmp) < 50:
                            FINAL_GIS_DICT.pop(KEYS[i])

            timeStamp = GIS.find('timestamp').text
            Width3D = GIS.find('width3d').text
            Direction3D = GIS.find('direction3d').text
            count += 1
        else:
            continue
    print("共有%s类" % count)
    print("*" * 20)
    return pictureName, timeStamp, ID, gis, FINAL_GIS_DICT


def read_xml_show1(img, xmlName, FINAL_GIS_DICT):
    f = open(xmlName, 'r')
    tree = ET.parse(f)
    root = tree.getroot()
    print("*" * 20)

    # global pictureName
    pictureName = root.find('filename').text
    print('fileName: ', pictureName)

    objs = tree.findall('object')
    count = 0
    timeStamp = None
    ID = []
    gis = []
    for idx, obj in enumerate(objs):
        className = obj.find('name').text

        print('clasName:  ', className)

        bbox = obj.find('bndbox')
        x_min = float(bbox.find('xmin').text)
        y_min = float(bbox.find('ymin').text)
        x_max = float(bbox.find('xmax').text)
        y_max = float(bbox.find('ymax').text)
        cv2.rectangle(img, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 1)
        cv2.putText(img, str(className[7:11]), (int(x_max), int(y_max)),cv2.FONT_HERSHEY_SIMPLEX, 0.4,  (0, 0, 255), 1)

        GIS = obj.find('reIdenInfo')
        if GIS == None:
            continue
        GIS_x = GIS.find('gis').find('x').text
        GIS_y = GIS.find('gis').find('y').text
        if (int(GIS_x[:-8]) < 100000000000) and (int(GIS_y[:-8]) < 100000000000):
            ID.append(className) # 防止index超标
            GIS_x = float(GIS_x)
            GIS_y = float(GIS_y)
            gis.append([GIS_x, GIS_y])

            global class_name1
            class_name1 = str(className[7:11])  # 显示最后两位，否则标出gis点上的字重叠
            if class_name1 in FINAL_GIS_DICT.keys():
                tmp = FINAL_GIS_DICT[class_name1]
                tmp.extend([(GIS_x, GIS_y)])
                FINAL_GIS_DICT[class_name1] = tmp
            else:
                FINAL_GIS_DICT[class_name1] = [(GIS_x, GIS_y)]
            timeStamp = GIS.find('timestamp').text
            Width3D = GIS.find('width3d').text
            Direction3D = GIS.find('direction3d').text
            count += 1
        else:
            continue

    print("共有%s类" % count)
    print("*" * 20)
    return pictureName, timeStamp, ID, gis, FINAL_GIS_DICT
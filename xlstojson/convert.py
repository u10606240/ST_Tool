import os
import re
from optparse import OptionParser
from XlsFileUtil import XlsFileUtil

diff = []
skinType = ['I','II','III','IV','V','VI']
hair = [0.5,2.0,3.5]
hair_density = ['Soft','Medium','Intense']
hair_color = ['LightBrown','DarkBrown','Black']
hair_thickness = ['Fine','Normal','Thick']
val = [[] for i in range(162)]

def addParser():
    parser = OptionParser()

    parser.add_option("-f", "--fileDir",
                      help="files directory.",
                      metavar="fileDir")

    parser.add_option("-t", "--targetDir",
                      help="The directory where the files will be saved.",
                      metavar="targetDir")

    parser.add_option("-m", "--machineCode",
                      help="Please enter the machine code you want to convert",
                      metavar="machineCode")

    (options, args) = parser.parse_args()

    return options


def convertForm803(fileDir, targetDir):
    xlsFileUtil = XlsFileUtil(fileDir)
    table = xlsFileUtil.getTableByIndex(0)
    table2 = xlsFileUtil.getTableByIndex(1)

    # if index == 0:
    #     tableTmp = table
    #     sex = 'Female'
    # else:
    #     tableTmp = table2
    #     sex = 'Male'
    keys = table.col_values(0)
    for i in range(len(keys)):
        if i == 0:
            pass
        else:
            values = table.row_values(i)
            check = False
            values[2] = int(values[2])
            values[2] = skinType[(values[2]-1)]
            values[1] = values[1] + '_Female'
            for j in range(len(hair)):
                if values[3] == hair[j]:
                    values[3] = str(hair_density[j])
                if values[4] == hair[j]:
                    values[4] = str(hair_color[j])
                if values[5] == hair[j]:
                    values[5] = str(hair_thickness[j])
            values[14] = int(values[14])
            tmp = values[3] + "_" + values[4] + "_" + values[5] + "_" + str(values[2]) + "_"
            if len(diff) == 0:
                diff.append(tmp)
            for i in range(len(diff)):
                if diff[i] == tmp:
                    check = False
                    val[i].append(values)
                    break
                else:
                    check = True
            if check:
                diff.append(tmp)
                val[len(diff)-1].append(values)
    keys = table2.col_values(0)
    for i in range(len(keys)):
        if i == 0:
            pass
        else:
            values = table2.row_values(i)
            values[2] = int(values[2])
            values[2] = skinType[(values[2]-1)]
            values[1] = values[1] + '_Male'
            for j in range(len(hair)):
                if values[3] == hair[j]:
                    values[3] = str(hair_density[j])
                if values[4] == hair[j]:
                    values[4] = str(hair_color[j])
                if values[5] == hair[j]:
                    values[5] = str(hair_thickness[j])
            values[14] = int(values[14])
            tmp = values[3] + "_" + values[4] + "_" + values[5] + "_" + str(values[2]) + "_"
            for i in range(len(diff)):
                if diff[i] == tmp:
                    val[i].append(values)
    i = 0
    for file in diff:  # 162
        path = targetDir
        filename = file + "parameter.json"
        writeToFile803(val[i], path, filename)
        i = i + 1
    print "Conversion Successful"


def writeToFile803(values, directory, filename):
    if not os.path.exists(directory):
        os.makedirs(directory)
    freq1 = []
    freq2 = []
    freq3 = []
    freq5 = []
    freq8 = []
    freq10 = []
    for i in range(len(values)):
        if values[i][14] == 1:
            freq1.append(values[i])
        elif values[i][14] == 2:
            freq2.append(values[i])
        elif values[i][14] == 3:
            freq3.append(values[i])
        elif values[i][14] == 5:
            freq5.append(values[i])
        elif values[i][14] == 8:
            freq8.append(values[i])
        elif values[i][14] == 10:
            freq10.append(values[i])

    fo = open(directory + "/" + filename, "wb")
    fo.write("{\r\n")
    fo.write("\t\"modifyer\":\"Winnie\",\r\n")
    fo.write("\t\"command_1\": \"[pulseWidth, Energy, Time(s)]\",\r\n")

    fo.write("\t\"freq_1\":[\r\n")
    for i in range(len(freq1)):
        fo.write("\t\t{\r\n")
        fo.write("\t\t\t\"symptoms\":\""+str(freq1[i][1])+"\",\r\n")
        fo.write("\t\t\t\"para\":[" + str(int(freq1[i][8])) + "," + str(int(freq1[i][9])) + "," + str(int(freq1[i][18])) + "]\r\n")
        fo.write("\t\t},\r\n")
    fo.write("\t],\r\n")

    fo.write("\t\"freq_2\":[\r\n")
    for i in range(len(freq2)):
        fo.write("\t\t{\r\n")
        fo.write("\t\t\t\"symptoms\":\""+str(freq2[i][1])+"\",\r\n")
        fo.write("\t\t\t\"para\":[" + str(int(freq2[i][8])) + "," + str(int(freq2[i][9])) + "," + str(int(freq2[i][18])) + "]\r\n")
        fo.write("\t\t},\r\n")
    fo.write("\t],\r\n")

    fo.write("\t\"freq_3\":[\r\n")
    for i in range(len(freq3)):
        fo.write("\t\t{\r\n")
        fo.write("\t\t\t\"symptoms\":\""+str(freq3[i][1])+"\",\r\n")
        fo.write("\t\t\t\"para\":[" + str(int(freq3[i][8])) + "," + str(int(freq3[i][9])) + "," + str(int(freq3[i][18])) + "]\r\n")
        fo.write("\t\t},\r\n")
    fo.write("\t],\r\n")

    fo.write("\t\"freq_5\":[\r\n")
    for i in range(len(freq5)):
        fo.write("\t\t{\r\n")
        fo.write("\t\t\t\"symptoms\":\""+str(freq5[i][1])+"\",\r\n")
        fo.write("\t\t\t\"para\":[" + str(int(freq5[i][8])) + "," + str(int(freq5[i][9])) + "," + str(int(freq5[i][18])) + "]\r\n")
        fo.write("\t\t},\r\n")
    fo.write("\t],\r\n")

    fo.write("\t\"freq_8\":[\r\n")
    for i in range(len(freq8)):
        fo.write("\t\t{\r\n")
        fo.write("\t\t\t\"symptoms\":\""+str(freq8[i][1])+"\",\r\n")
        fo.write("\t\t\t\"para\":[" + str(int(freq8[i][8])) + "," + str(int(freq8[i][9])) + "," + str(int(freq8[i][18])) + "]\r\n")
        fo.write("\t\t},\r\n")
    fo.write("\t],\r\n")

    fo.write("\t\"freq_10\":[\r\n")
    for i in range(len(freq10)):
        fo.write("\t\t{\r\n")
        fo.write("\t\t\t\"symptoms\":\""+str(freq10[i][1])+"\",\r\n")
        fo.write("\t\t\t\"para\":[" + str(int(freq10[i][8])) + "," + str(int(freq10[i][9])) + "," + str(int(freq10[i][18])) + "]\r\n")
        fo.write("\t\t},\r\n")
    fo.write("\t]\r\n")
        # values[i][11] = int(values[i][11])
        # values[i][12] = int(values[i][12])
        # values[i][13] = int(values[i][13])
        # values[i][14] = int(values[i][14])
        # fo.write("{" + str(round(values[i][7], 1)) + "," + str(values[i][8]) + "," + str(values[i][9]) + "," + str(
        #     values[i][10]) + "," + str(values[i][11]) + "," + str(values[i][12]) + "," + str(values[i][13]) + "," + str(
        #     values[i][14]) + "},\r\n")
    fo.write("}")
    fo.close()

def convertForm691(fileDir, targetDir):
    xlsFileUtil = XlsFileUtil(fileDir)
    table = xlsFileUtil.getTableByIndex(4)
    table2 = xlsFileUtil.getTableByIndex(5)
    table3 = xlsFileUtil.getTableByIndex(6)

    keys = table.col_values(0)
    for i in range(len(keys)):
        if i == 0:
            pass
        else:
            values = table.row_values(i)
            if values[0] == 'Woman':
                values[0] = 'Female'
            elif values[0] == 'Man':
                values[0] = 'Male'
            check = False
            tmp = values[0] + "_" + values[2].capitalize() + "_" + values[3].capitalize() + "_" + values[4].capitalize() + "_"
            if len(diff) == 0:
                diff.append(tmp)
            for i in range(len(diff)):
                if diff[i] == tmp:
                    check = False
                    val[i].append(values)
                    break
                else:
                    check = True
            if check:
                diff.append(tmp)
                val[len(diff)-1].append(values)

    keys = table2.col_values(0)
    for j in range(len(diff)):
        for i in range(len(keys)):
            if i == 0:
                pass
            else:
                values = table2.row_values(i)
                if values[0] == 'Woman':
                    values[0] = 'Female'
                elif values[0] == 'Man':
                    values[0] = 'Male'
                if values[3] == 5:
                    if values[0] in diff[j]:
                        val[j].append(values)

    keys = table3.col_values(0)
    for i in range(len(keys)):
        if i == 0:
            pass
        else:
            values = table3.row_values(i)
            if values[0] == 'Woman':
                values[0] = 'Female'
            elif values[0] == 'Man':
                values[0] = 'Male'
            tmp = values[0] + "_" + values[2].capitalize() + "_" + values[3].capitalize() + "_" + values[4].capitalize()+ "_"
            for j in range(len(diff)):
                if diff[j] == tmp:
                    val[j].append(values)
                    break
    i = 0
    for file in diff:  # 54
        path = targetDir
        filename = file + "parameter.json"
        writeToFile691(val[i], path, filename)
        i = i + 1
    print "Conversion Successful"


def writeToFile691(values, directory, filename):
    if not os.path.exists(directory):
        os.makedirs(directory)
    skin1 = []
    skin2 = []
    skin3 = []
    skin4 = []
    skin5 = []
    fo = open(directory + "/" + filename, "wb")
    for i in range(len(values)):
        if i >= 10:
            if values[i][5] == 1:
                skin1.append(values[i])
            elif values[i][5] == 2:
                skin2.append(values[i])
            elif values[i][5] == 3:
                skin3.append(values[i])
            elif values[i][5] == 4:
                skin4.append(values[i])
            elif values[i][5] == 5:
                skin5.append(values[i])
        else:
            if values[i][1] == 1:
                skin1.append(values[i])
            elif values[i][1] == 2:
                skin2.append(values[i])
            elif values[i][1] == 3:
                skin3.append(values[i])
            elif values[i][1] == 4:
                skin4.append(values[i])
            elif values[i][1] == 5:
                skin5.append(values[i])
    fo.write("{\r\n")
    fo.write("\t\"modifyer\":\"EdHo\",\r\n")
    fo.write("\t\"command_1\": \"[LV, Filter, Pulse No., Pulse 1, Delay 1, Pulse 2, Delay 2, Pulse n]\",\r\n")
    fo.write("\t\"command_2\": \"[LV, Filter, Freq]\",\r\n")
    fo.write("\t\"command_2\": \"[LV, Filter, Freq, Timer]\",\r\n")

    fo.write("\t\"I\":[\r\n")
    for i in range(len(skin1)):
        fo.write("\t\t{\r\n")
        if i == 0:
            fo.write("\t\t\t\"symptoms\":\"Hair Removal_Smart\",\r\n")
            fo.write("\t\t\t\"para\":[" + str(int(skin1[i][5])) + "," + str(int(skin1[i][12])) + "," + str(int(skin1[i][6])) + "," + str(int(skin1[i][7])) + "," + str(int(skin1[i][8])) + "," + str(int(skin1[i][9])) + "," + str(int(skin1[i][10]))+ "," + str(int(skin1[i][11])) + "]\r\n")
        elif i == 1:
            fo.write("\t\t\t\"symptoms\":\"Hair Removal_SHR\",\r\n")
            fo.write("\t\t\t\"para\":[" + str(int(skin1[i][2])) + "," + "690" + "," + str(int(skin1[i][3])) + "," + str(int(skin1[i][4])) + "]\r\n")
        else:
            fo.write("\t\t\t\"symptoms\":\"Hair Removal_Stack_"+skin1[i][1]+"\",\r\n")
            fo.write("\t\t\t\"para\":[" + str(int(skin1[i][6])) + "," + "690" + "," + str(int(skin1[i][7]))+ "," + str(int(skin1[i][8])) + "]\r\n")
        fo.write("\t\t},\r\n")
    fo.write("\t],\r\n")

    fo.write("\t\"II\":[\r\n")
    for i in range(len(skin2)):
        fo.write("\t\t{\r\n")
        if i == 0:
            fo.write("\t\t\t\"symptoms\":\"Hair Removal_Smart\",\r\n")
            fo.write("\t\t\t\"para\":[" + str(int(skin2[i][5])) + "," + str(int(skin2[i][12])) + "," + str(int(skin2[i][6])) + "," + str(int(skin2[i][7])) + "," + str(int(skin2[i][8])) + "," + str(int(skin2[i][9])) + "," + str(int(skin2[i][10]))+ "," + str(int(skin2[i][11])) + "]\r\n")
        elif i == 1:
            fo.write("\t\t\t\"symptoms\":\"Hair Removal_SHR\",\r\n")
            fo.write("\t\t\t\"para\":[" + str(int(skin2[i][2])) + "," + "690" + "," + str(int(skin2[i][3])) + "," + str(int(skin2[i][4])) + "]\r\n")
        else:
            fo.write("\t\t\t\"symptoms\":\"Hair Removal_Stack_"+skin2[i][1]+"\",\r\n")
            fo.write("\t\t\t\"para\":[" + str(int(skin2[i][6])) + "," + "690" + "," + str(int(skin2[i][7]))+ "," + str(int(skin2[i][8])) + "]\r\n")
        fo.write("\t\t},\r\n")
    fo.write("\t],\r\n")

    fo.write("\t\"III\":[\r\n")
    for i in range(len(skin3)):
        fo.write("\t\t{\r\n")
        if i == 0:
            fo.write("\t\t\t\"symptoms\":\"Hair Removal_Smart\",\r\n")
            fo.write("\t\t\t\"para\":[" + str(int(skin3[i][5])) + "," + str(int(skin3[i][12])) + "," + str(int(skin3[i][6])) + "," + str(int(skin3[i][7])) + "," + str(int(skin3[i][8])) + "," + str(int(skin3[i][9])) + "," + str(int(skin3[i][10]))+ "," + str(int(skin3[i][11])) + "]\r\n")
        elif i == 1:
            fo.write("\t\t\t\"symptoms\":\"Hair Removal_SHR\",\r\n")
            fo.write("\t\t\t\"para\":[" + str(int(skin3[i][2])) + "," + "690" + "," + str(int(skin3[i][3])) + "," + str(int(skin3[i][4])) + "]\r\n")
        else:
            fo.write("\t\t\t\"symptoms\":\"Hair Removal_Stack_"+skin3[i][1]+"\",\r\n")
            fo.write("\t\t\t\"para\":[" + str(int(skin3[i][6])) + "," + "690" + "," + str(int(skin3[i][7]))+ "," + str(int(skin3[i][8])) + "]\r\n")
        fo.write("\t\t},\r\n")
    fo.write("\t],\r\n")

    fo.write("\t\"IV\":[\r\n")
    for i in range(len(skin4)):
        fo.write("\t\t{\r\n")
        if i == 0:
            fo.write("\t\t\t\"symptoms\":\"Hair Removal_Smart\",\r\n")
            fo.write("\t\t\t\"para\":[" + str(int(skin4[i][5])) + "," + str(int(skin4[i][12])) + "," + str(int(skin4[i][6])) + "," + str(int(skin4[i][7])) + "," + str(int(skin4[i][8])) + "," + str(int(skin4[i][9])) + "," + str(int(skin4[i][10]))+ "," + str(int(skin4[i][11])) + "]\r\n")
        elif i == 1:
            fo.write("\t\t\t\"symptoms\":\"Hair Removal_SHR\",\r\n")
            fo.write("\t\t\t\"para\":[" + str(int(skin4[i][2])) + "," + "690" + "," + str(int(skin4[i][3])) + "," + str(int(skin4[i][4])) + "]\r\n")
        else:
            fo.write("\t\t\t\"symptoms\":\"Hair Removal_Stack_"+skin4[i][1]+"\",\r\n")
            fo.write("\t\t\t\"para\":[" + str(int(skin4[i][6])) + "," + "690" + "," + str(int(skin4[i][7]))+ "," + str(int(skin4[i][8])) + "]\r\n")
        fo.write("\t\t},\r\n")
    fo.write("\t],\r\n")

    fo.write("\t\"V\":[\r\n")
    for i in range(len(skin5)):
        fo.write("\t\t{\r\n")
        if i == 0:
            fo.write("\t\t\t\"symptoms\":\"Hair Removal_Smart\",\r\n")
            fo.write("\t\t\t\"para\":[" + str(int(skin5[i][5])) + "," + str(int(skin5[i][12])) + "," + str(int(skin5[i][6])) + "," + str(int(skin5[i][7])) + "," + str(int(skin5[i][8])) + "," + str(int(skin5[i][9])) + "," + str(int(skin5[i][10]))+ "," + str(int(skin5[i][11])) + "]\r\n")
        elif i == 1:
            fo.write("\t\t\t\"symptoms\":\"Hair Removal_SHR\",\r\n")
            fo.write("\t\t\t\"para\":[" + str(int(skin5[i][2])) + "," + "690" + "," + str(int(skin5[i][3])) + "," + str(int(skin5[i][4])) + "]\r\n")
        else:
            fo.write("\t\t\t\"symptoms\":\"Hair Removal_Stack_"+skin5[i][1]+"\",\r\n")
            fo.write("\t\t\t\"para\":[" + str(int(skin5[i][6])) + "," + "690" + "," + str(int(skin5[i][7]))+ "," + str(int(skin5[i][8])) + "]\r\n")
        fo.write("\t\t},\r\n")
    fo.write("\t]\r\n")

    fo.write("}")
    fo.close()

def startConvert(options):
    fileDir = options.fileDir

    targetDir = options.targetDir

    machine = options.machineCode

    print "Start converting"

    if fileDir is None:
        print "files directory can not be empty! try -h for help."
        return
    elif targetDir is None:
        print "Target file path can not be empty! try -h for help."
        return
    elif fileDir is not None and targetDir is not None:
        if machine == "803":
            convertForm803(fileDir, targetDir)
        elif machine == "691":
            convertForm691(fileDir, targetDir)
        else:
            print "please enter machine code"


def main():
    options = addParser()
    startConvert(options)


main()
# convertForm("C:\\Users\\Winnie\\Desktop\\ST-803_Data Table_20240115.xls",
#             "C:\\Users\\Winnie\\Desktop\\recomend_1600W_12x14_new\\")

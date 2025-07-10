# -*- coding:utf-8 -*-
import re

import xlwt
import xml.dom.minidom
from optparse import OptionParser
import pyExcelerator
import os
import time
import cgi

from Log import Log
from XlsFileUtil import XlsFileUtil


def addParser():
    parser = OptionParser()

    parser.add_option("-f", "--fileDir",
                      help="files directory.",
                      metavar="fileDir")

    parser.add_option("-t", "--targetDir",
                      help="The directory where the files will be saved.",
                      metavar="targetDir")

    parser.add_option("-i", "--input",
                      action="store_true",
                      help="Convert String from (.xls) to (.xml).",
                      metavar="input")

    parser.add_option("-o", "--output",
                      action="store_true",
                      help="Convert String from (.xml) to (.xls).",
                      metavar="output")

    parser.add_option("-n", "--assign",
                      type="string",
                      help="Assign strings,error_msg or all",
                      metavar="assign")

    (options, args) = parser.parse_args()

    return options


def convertInputForm(options, fileDir, targetDir):
    flag_str = False
    for _, _, filenames in os.walk(fileDir):
        if options == 'all':
            xlsFilenames = ['error_msg.xls', 'strings.xls']
            xlsFilenames_str = []
            for i in xlsFilenames:
                for fi in filenames:
                    if fi.endswith(i):
                        xlsFilenames_str.append(fi)
        elif options is None:
            print 'Please enter argument -n'
            break
        else:
            xlsFilenames = options.split(',')
            for i in range(len(xlsFilenames)):
                xlsFilenames[i] += '.xls'
            xlsFilenames_str = []
            for i in xlsFilenames:
                for fi in filenames:
                    if fi.endswith(i):
                        xlsFilenames_str.append(fi)
        if len(xlsFilenames_str) != 0:
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)

            for file in xlsFilenames_str:
                flag_str = True
                xlsFileUtil = XlsFileUtil(fileDir + "/" + file)
                file = file.replace(".xls", "")
                table = xlsFileUtil.getTableByIndex(0)
                firstRow = table.row_values(0)
                keys = table.col_values(0)
                del keys[0]

                for index in range(len(firstRow)):
                    if index <= 0:
                        continue
                    languageName = firstRow[index]
                    values = table.col_values(index)
                    del values[0]

                    path = targetDir + "/values-" + languageName + "/"
                    if languageName == 'default':
                        path = targetDir + "/values/"
                    # if file.startswith('error'):
                    filename = file + ".xml"
                    writeToFile(keys, values, path, filename, languageName)
        else:
            if flag_str == False:
                print 'Cant find file'
            break
    if flag_str:
        print "Convert %s successfully! you can xml files in %s" % (fileDir, targetDir)
    else:
        print 'Cant find file in this area'


def convertOutputForm(options, fileDir, targetDir):
    destDir = targetDir
    flag = False
    flag_str = False
    for _, dirnames, _ in os.walk(fileDir):
        valuesDirs = [di for di in dirnames if di.startswith("values")]
        if len(valuesDirs) != 0:
            flag = True
            for dirname in valuesDirs:
                for _, _, filenames in os.walk(fileDir + '/' + dirname):
                    xmlFiles_str = []
                    if options == 'all':
                        xmlFiles = ['error_msg.xml', 'strings.xml']
                        for i in xmlFiles:
                            for fi in filenames:
                                if fi.endswith(i):
                                    xmlFiles_str.append(fi)
                    elif options is None:
                        print 'Please enter argument -n'
                        break
                    else:
                        xmlFiles = options.split(',')
                        for i in range(len(xmlFiles)):
                            xmlFiles[i] += '.xml'
                        for i in xmlFiles:
                            for fi in filenames:
                                if fi == i:
                                    xmlFiles_str.append(fi)

                    if len(xmlFiles_str) != 0:
                        flag_str = True
                        if not os.path.exists(targetDir):
                            os.makedirs(targetDir)
                        for xmlfile in xmlFiles_str:
                            fileName = xmlfile.replace(".xml", "")
                            filePath = destDir + "/" + fileName + ".xls"
                            if not os.path.exists(filePath):
                                workbook = pyExcelerator.Workbook()
                                ws = workbook.add_sheet(fileName)
                                style = pyExcelerator.XFStyle()
                                style1 = pyExcelerator.XFStyle()

                                pattern = pyExcelerator.Pattern()
                                pattern.pattern = xlwt.Pattern.SOLID_PATTERN
                                pattern.pattern_fore_colour = 22
                                style.pattern = pattern

                                font = pyExcelerator.Font()
                                font.bold = True
                                style1.font = font
                                style.font = font

                                index = 0
                                for dirname in valuesDirs:
                                    if index == 0:
                                        ws.write(0, 0, 'keyName', style)
                                    countryCode = getCountryCode(dirname)
                                    ws.write(0, index + 1, countryCode, style)

                                    path = fileDir + '/' + dirname + '/' + xmlfile
                                    (keys, values) = getKeysAndValues(path)

                                    max_key = 0
                                    max_val = 0
                                    for x in range(len(keys)):
                                        key = keys[x]
                                        value = values[x]
                                        if max_key < len(key):
                                            max_key = len(key)
                                        if max_val < len(value):
                                            max_val = len(value)
                                        if (index == 0):
                                            ws.write(x + 1, 0, key, style1)
                                            ws.write(x + 1, 1, value)
                                        else:
                                            ws.write(x + 1, index + 1, value)
                                    index += 1
                                    if countryCode == 'ja':
                                        max_val = max_val + 10
                                    max_key = max_key + 5
                                    ws.col(0).width = 256 * max_key
                                    ws.col(index).width = 256 * max_val
                                ws.set_panes_frozen(True)
                                ws.set_horz_split_pos(1)
                                ws.set_vert_split_pos(1)
                                workbook.save(filePath)
                    else:
                        print "no xml in file"
        else:
            if flag == False:
                print "Can't find values in file"
            break
    if flag_str:
        print "Convert %s successfully! you can see xls file in %s" % (fileDir, destDir)
    else:
        print 'Cant find file in this area'


def getCountryCode(dirname):
    code = 'default'
    dirSplit = dirname.split('values-')
    if len(dirSplit) > 1:
        code = dirSplit[1]
    return code


def getKeysAndValues(path):
    if path is None:
        Log.error('file path is None')
        return

    dom = xml.dom.minidom.parse(path)
    root = dom.documentElement
    itemlist = root.getElementsByTagName('string')

    keys = []
    values = []
    for index in range(len(itemlist)):
        item = itemlist[index]
        ex1 = item.getElementsByTagName('b')
        ex2 = item.getElementsByTagName('sup')
        key = item.getAttribute("name")
        try:
            if ex1:
                value = ex1.item(0).childNodes.item(0).data
            elif ex2:
                value = item.firstChild.data + ex2.item(0).childNodes.item(0).data
            else:
                value = item.firstChild.data
        except AttributeError:
            pass
        keys.append(key)
        values.append(value)

    itemlist_arr = root.getElementsByTagName('string-array')
    if len(itemlist_arr) != 0:
        for length in range(len(itemlist_arr)):
            key = itemlist_arr[length].getAttribute("name")
            value = itemlist_arr[length].getElementsByTagName('item')
            for index in range(len(value)):
                keys.append(key + '[' + unicode(index) + ']')
                if value.item(index).childNodes.item(0) is None:
                    values.append('\n')
                else:
                    tmp = value.item(index).childNodes.item(0).data
                    # if tmp >= unicode('0') and tmp <= unicode('9'):
                    #     values.append(int(tmp))
                    # else:
                    values.append(tmp)

    return (keys, values)


def writeToFile(keys, values, directory, filename, language):
    if not os.path.exists(directory):
        os.makedirs(directory)

    fo = open(directory + "/" + filename, "wb")

    stringEncoding = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\r\n<resources>\r\n"
    fo.write(stringEncoding)
    check = False
    check1 = False
    diff = []
    for x in range(len(keys)):
        if values[x] is None or values[x] == '' or values[x] == '\n':
            Log.error("Key:" + keys[x] +
                      "\'s value is None. Index:" + str(x + 1))
            if re.findall(r'\W\d+\W', keys[x]):
                content = "\t\t<item></item>\r\n"
                fo.write(content)
            continue
        key = keys[x].strip()
        if type(values[x]) is unicode:
            value = re.sub(r'(%\d\$)(@)', r'\1s', values[x])
            if language == 'fr':
                value = re.sub(r"'", r"\'", value)
        else:
            value = values[x]
        if re.findall(r'\W\d+\W', key):
            tmp = re.findall(r'\w+', key)
            number = re.findall(r'\d+', key)
            diff.append(tmp[0])
            length = len(diff)
            if diff[length - 1] != diff[length - 2]:
                check = True
            if check:
                check = False
                content = "\t</string-array>\r\n"
                fo.write(content)
            if number[0] == '0':
                content = "\t<string-array name=\"" + tmp[0] + "\">\r\n"
                check1 = True
                fo.write(content)
            content = "\t\t<item>" + value + "</item>\r\n"
        else:
            if check:
                check = False
                content = "\t</string-array>\r\n"
                fo.write(content)
            if key == 'text_recomend':
                content = "\t<string name=\"" + key + "\"><b>" + value + "</b></string>\r\n"
            elif key == 'jcm2':
                value1 = value[0:4]
                value2 = value[4]
                content = "\t<string name=\"" + key + "\">" + value1 + "<sup>" + value2 + "</sup>" + "</string>\r\n"
            elif key == 'sr_reminder':
                value1 = value.split("<b>")
                tmp1 = value1[1].split("</b>")
                value2 = value.split("</b>")
                content = "\t<string name=\"" + key + "\">" + value1[0] + "<b>" + tmp1[0] + "</b>" + value2[
                    1] + "</string>\r\n"
            else:
                if type(values[x]) is unicode:
                    value = cgi.escape(value)
                else:
                    value = unicode(int(value))
                content = "\t<string name=\"" + key + "\">" + value + "</string>\r\n"
        fo.write(content)
    if check1:
        content = "\t</string-array>\r\n"
        fo.write(content)
    fo.write("</resources>\r\n")
    fo.close()


def startConvert(options):
    fileDir = options.fileDir

    targetDir = options.targetDir

    print "Start converting"

    if fileDir is None:
        print "files directory can not be empty! try -h for help."
        return

    if targetDir is None:
        print "Target file path can not be empty! try -h for help."
        return

    if options.input:
        targetDir = targetDir + "/xls-files-to-xml_" + \
                    time.strftime("%Y%m%d_%H%M%S")
        convertInputForm(options.assign, fileDir, targetDir)
    elif options.output:
        targetDir = targetDir + "/xml-files-to-xls_" + \
                    time.strftime("%Y%m%d_%H%M%S")
        convertOutputForm(options.assign, fileDir, targetDir)
    else:
        print "Please give a status"


def main():
    options = addParser()
    startConvert(options)


main()
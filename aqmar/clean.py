# -*- coding: utf-8 -*-
import glob

files = glob.glob(r'.\articles\*.txt')
#print(myFilesPaths)

for file in files:
    iFile = open(file, 'r', encoding="utf8")
    oFile = open(file + ".clean.txt", 'w', encoding="utf8")
    lines = iFile.readlines()
    for line in lines:
        term = line.split()
        if len(term) != 0:
            #print(term[0])
            oFile.write(term[0] + " ")
    iFile.close()
    oFile.close()



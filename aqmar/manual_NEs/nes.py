# -*- coding: utf-8 -*-
import glob

files = glob.glob(r'.\*.txt')
#print(myFilesPaths)

for file in files:
    iFile = open(file, 'r', encoding="utf8")
    oFileL = open(file + ".locations.txt", 'w', encoding="utf8")
    oFileO = open(file + ".Organizations.txt", 'w', encoding="utf8")
    oFileP = open(file + ".Persons.txt", 'w', encoding="utf8")
    lines = iFile.readlines()
    for line in lines:
        term = line.split()
        if len(term) != 0:
            if term[1] == 'B-LOC' or term[1] == 'I-LOC':
                oFileL.write(term[0])
                oFileL.write("\n")
            if term[1] == 'B-ORG' or term[1] == 'I-ORG':
                oFileO.write(term[0])
                oFileO.write("\n")
            if term[1] == 'B-PER' or term[1] == 'I-PER':
                oFileP.write(term[0])
                oFileP.write("\n")
    iFile.close()
    oFileL.close()
    oFileO.close()
    oFileP.close()

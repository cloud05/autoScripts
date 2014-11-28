# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 14:46:00 2014

@author: prinsepe
"""
'''
    A script to automate the changing of HVT files for single or multiple tide
    points. This is still a crude version of the code. Further versions will 
    include:
        a. input of (tidestation: range) in csv format(Done)
        b. error catchment
        c. code efficiency
        d. automatic tidestation generation
        e. etc.
'''
import os, fnmatch, re, csv
    
def changeHVTone():
    typhs = [] #original path
    corsHVT = [] #corresponding hvt folder
    counter = 0
    noSim = input("How many typhoons will you simulate?: ")
    while counter < noSim: 
        typh  = raw_input("Enter the path of the model: ")
        typhs.append(typh)
        corHVT = raw_input("Enter the hvt path corresponding to the model: ")
        corsHVT.append(corHVT)
        counter += 1
    dic2 = dict(zip(typhs,corsHVT))
    a = raw_input("Choose the station to use: ")
    for origPath in dic2.keys():
        print origPath
        mainhvtPath = dic2[origPath]       
        prompt_a = a + '.hvt'
        hvtPath = os.path.join(mainhvtPath,prompt_a)
        for root, dirnames, filenames in os.walk(origPath):
            for files in fnmatch.filter(filenames,'*.hvt'):
                filePath = os.path.join(origPath,files)
                print filePath
                print hvtPath
                x = open(hvtPath,"r+")
                f = open(filePath,'r+')
                txtin = x.read()
                txtout = f.read()
                res = ''.join([i for i in txtout if i.isalpha()])
                txtout = re.sub('',txtin,res)
                f.seek(0)
                f.write(txtout)
                f.truncate()
                f.close()
                x.close()
    print "Done!"
        


def changeHVTmulti():
    typhs = [] #original path
    corsHVT = [] #corresponding hvt folder
    hvts  = [] #hvt's to be used to change the output full path
    points = [] #F2D-GDS hvts
    stations = [] #range of points for a certain station
    counter = 0
#    count = 1    
    noSim = input("How many typhoons will you simulate?: ")
    
    #    hvtmainPath = raw_input("Enter the path of the hvt folder: ")
    #    hvtDir = os.listdir(hvtmainPath)    
    
    while counter < noSim:
        typh  = raw_input("Enter the path of the models: ")
        typhs.append(typh)        
        corHVT = raw_input("Enter the hvt path corresponding to the model: ")
        corsHVT.append(corHVT)
        counter +=1
    reader = raw_input("Enter the path of your csv input: ")
    read = csv.reader(open(reader))
    next(read)
    for row in read:
        prompt_b = row[0] + '.hvt'
        prompt_c = row[1]
        prompt_d = row[2]
        
    #prompt = int(raw_input("Enter the EXACT number of stations you'll use: "))
    #while count < prompt+1:
    #    promt_e = raw_input("Enter STATIONS to use: ")
    #    prompt_b = promt_e + '.hvt'
    #    prompt_c = raw_input("Enter the STARTING point of {}: ".format(prompt_b))
    #    prompt_d = raw_input("Enter the ENDPOINT of {}: ".format(prompt_b))    
    #    count  += 1
        for mainhvtPath in corsHVT:
            zipper = tuple((prompt_c,prompt_d))
            stations.append(zipper)
            hvtPath = os.path.join(mainhvtPath,prompt_b)
            hvts.append(hvtPath)
            dic = dict(zip(hvts,stations))
    

    dic2 = dict(zip(typhs,corsHVT))
    for origPath in typhs:
        print "MainDir: "+ origPath
        for root, dirnames, filenames in os.walk(origPath):
            for files in fnmatch.filter(filenames,'*.hvt'):
                points.append(files)
        for j in dic.keys():
            for i in range(int(dic[j][0]),int(dic[j][1])+1):
                for point in points:
                    if " {}.HVT".format(str(i)) in point:
                        hvtPath = os.path.join(dic2[origPath],os.path.split(j)[1])
                        filePath = os.path.join(origPath,point)
                print "hvt: "+hvtPath
                print "file: "+filePath
                x = open(hvtPath,"r+")
                f = open(filePath,'r+')
                txtin = x.read()
                txtout = f.read()
                res = ''.join([i for i in txtout if i.isalpha()])
                txtout = re.sub('',txtin,res)
                f.seek(0)
                f.write(txtout)
                f.truncate()
                f.close()
                x.close()
                        
    print "Done!"
        
if __name__ == '__main__':
    while True:
        random = raw_input("Choose the code to run.\n"+"a. Single point-station"+"\nb. Multi point-station" +'\n>>> ')
        small = random.lower()
        if small == 'a':
            changeHVTone()
            break
        if small == 'b':
            changeHVTmulti()
            break
        else:
            print "Enter letter only!"
            True
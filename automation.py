#used for making requests to the cameras http
import requests

import sys

#used to download the images
import wget

#used for the timer function
import time

#used for multithreading and running functions at the same time
import threading

from datetime import date

import os 

#set the start time for the overall time
time_start = time.time()

#set the start time for the 8 second counter
time_startTwo = time.time()

#variable for keeping track of if the program should still run
keepRunning = True

#init time variables
secondsTwo = 0
seconds = 0
minutes = 0
#index of the photos
index = 0

parent_dir = "C:/Users/zoro/Desktop/Cams"
directory = str(date.today())
path = os.path.join(parent_dir, directory) 

class Billboard:

    def __init__(self, name, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.name = name
        self.response = None
        self.writeable = False
        if(username is None and password is None):
            try:
                self.response = requests.get(url)
                self.writeable = True
            except:
                print("Unable to get " + self.name + " image")
                self.writeable = False
        else:
            try:
                self.response = requests.get(url, auth=(username, password))
                self.writeable = True
            except:
                print("Unable to get " + self.name + " image")
                self.writeable = False
        
    def updateResponse(self):
        try:
            if(self.username is None and self.password is None):
                self.response = requests.get(self.url)
                self.writeable = True
            else:
                self.response = requests.get(self.url, auth=(self.username, self.password))
                self.writeable = True
        except:
            print("Unable to get " + self.name + " image")
            self.writeable = False

    def writeImage(self, imageIndex, path):
        if(self.response != None):
            if(len(self.response.content) > 500):
                try:
                    print(len(self.response.content))
                    file = open(path + "/" + str(self.name) + "/" + self.name + "_" + str(imageIndex) + ".jpg", "wb")
                    file.write(self.response.content)
                    file.close()
                except:
                    print("Unable to write " + self.name + " image")
        
      


kenJohBillboards = [Billboard("200", 'http://63.46.61.55:9501/record/current.jpg', 'kenjoh', 'camera.812'),
                    Billboard("401", "http://166.168.239.41:9501/record/current.jpg", "kenjoh", 'kenjoh2020')]

americanBillboards = [Billboard("3-1E", "http://166.154.63.73:9501/cgi-bin/image.jpg", "american",'124296'),
                    Billboard("03-3W", "http://166.164.77.251:9501/cgi-bin/image.jpg", "american", "124297"),
                    Billboard("4-1S", "http://166.154.7.75:9501/cgi-bin/image.jpg?rand=8968745", "american", "128274"),
                    Billboard("04-1N", "http://166.154.7.71:9501/cgi-bin/image.jpg?rand=8968745", "american", "128273"),
                    Billboard("05-1S", "http://166.154.7.106:9501/record/current.jpg", "american", "112901"),
                    Billboard("05-1N", "http://166.154.7.107:9501/record/current.jpg?rand=648878", "american", "117996")]

MileHighBillboards = [Billboard("2181", "http://166.144.174.13:9501/record/current.jpg", "milehigh", "wf149703"),
                    Billboard("2168", "http://166.248.84.202:8089/axis-cgi/jpg/image.cgi?camera=1&resolution=352x240&compression=30&text=0&clock=0&date=0", None, None),
                    Billboard("2169", "http://166.248.84.202:8088/axis-cgi/jpg/image.cgi?camera=1&resolution=352x240&compression=30&text=0&clock=0&date=0", None, None),
                    Billboard("2183", "http://166.140.119.79:8089/axis-cgi/jpg/image.cgi?camera=1&resolution=352x240&compression=30&text=0&clock=0&date=0", None, None),
                    Billboard("2184", "http://166.140.119.79:8088/axis-cgi/jpg/image.cgi?camera=1&resolution=352x240&compression=30&text=0&clock=0&date=0", None, None),
                    Billboard("3099", "http://63.227.141.5:8088/axis-cgi/jpg/image.cgi?camera=1&resolution=352x240&compression=30&text=0&clock=0&date=0", None, None),
                    Billboard("3100", "http://63.227.141.5:8089/axis-cgi/jpg/image.cgi?camera=1&resolution=352x240&compression=30&text=0&clock=0&date=0", None, None),
                    Billboard("3113", "http://166.168.62.232:9501/record/current.jpg?rand=639436", "milehigh", "139221"),
                    Billboard("3018", "http://166.255.235.75:9501/record/current.jpg?rand=4185626", "milehigh", "wf144819"),
                    Billboard("3017", "http://166.253.103.213:9501/record/current.jpg?rand=9637150", "milehigh", "wf144820"),
                    Billboard("3026", "http://166.255.235.74:9501/record/current.jpg?rand=428350", "milehigh", "141046"),
                    Billboard("3162", "http://166.253.103.214:9501/record/current.jpg", "milehigh", "118092"),
                    Billboard("3167", "http://166.153.133.14:9501/record/current.jpg", "milehigh", "131546"),
                    Billboard("3097", "http://63.42.122.188:9501/record/current.jpg?rand=", "milehigh", "109716"),
                    Billboard("3170", "http://166.141.93.251:82/SnapshotJPEG??", None, None),
                    Billboard("3171", "http://166.141.93.251:81/SnapshotJPEG??", None, None),
                    Billboard("3116", "http://63.42.199.173:9501/record/current.jpg?rand=426521", "milehigh", "wf155444")]

POAWBillboards = [Billboard("270", "http://166.130.109.0:5001/record/current.jpg?", None, None),
                Billboard("128", "http://166.130.163.102:9501/record/current.jpg?rand=3636102", "pacificoutdoor", "wf145562"),
                Billboard("130", "http://166.130.165.209:9501/record/current.jpg?rand=8245940", "pacific", "wf145563"),
                Billboard("263", "http://166.130.163.40:9501/record/current.jpg?rand=8233049", "pacific", "wf145561"),
                Billboard("267", "http://155.170.123.92:9501/record/current.jpg?rand=2954205", "pacific", "wf145867"),
                Billboard("160", "http://166.218.50.236:9501/record/current.jpg?rand=3811820", "pacific", "wf145560"),
                Billboard("161", "http://166.218.51.11:9501/record/current.jpg?rand=7806201", "pacific", "wf145559"),
                Billboard("279", "http://166.203.166.135:9501/record/current.jpg?rand=3636102", "pacific", "wf153224")]

POAOBillboards = [Billboard("80852", "http://166.130.53.12:5001/jpg/1/image.jpg?timestamp=1614804928048", None, None),
                Billboard("80851", "http://166.130.53.12:5002/record/current.jpg?", None, None),
                Billboard("81080", "http://166.130.5.116:5002/record/current.jpg?", None, None),
                Billboard("81079", "http://166.130.5.116:5001/record/current.jpg?", None, None),
                Billboard("83300", "http://166.164.197.178:8088/axis-cgi/jpg/image.cgi?camera=1&resolution=352x240&compression=30&text=0&clock=0&date=0", "pacific", "137489"),
                Billboard("83400", "http://166.139.102.66:9501/record/current.jpg?rand=9031498", "pacific", "137489"),
                Billboard("85112", "http://166.130.51.49:5001/record/current.jpg?", None, None),
                Billboard("84236", "http://166.130.177.243:9501/record/current.jpg?rand=313110", "pacific", "138464"),
                Billboard("84424", "http://166.130.39.176:9501/record/current.jpg?rand=1377279", "pacific", "138465"),
                Billboard("80815", "http://166.130.52.93:5001/record/current.jpg?", None, None),
                Billboard("80816", "http://166.130.52.93:5002/record/current.jpg?", None, None),
                Billboard("80714", "http://166.130.152.188:5001/record/current.jpg?", None, None),
                Billboard("80715", "http://166.130.152.188:5002/record/current.jpg?", None, None),
                Billboard("81045", "http://166.130.50.109:5001/jpg/1/image.jpg?timestamp=1614805794722", None, None),
                Billboard("81059", "http://166.130.52.157:5001/jpg/1/image.jpg?timestamp=1614805896075", None, None),
                Billboard("76105", "http://166.130.51.188:5001/axis-cgi/jpg/image.cgi?camera=1&resolution=352x240&compression=30&text=0&clock=0&date=0", None, None),
                Billboard("76127", "http://166.248.195.35:8088/jpg/1/image.jpg?timestamp=1614807653156", None, None),
                Billboard("76128", "http://166.248.195.34:8088/jpg/1/image.jpg?timestamp=1614808948975", None, None),
                Billboard("76556", "http://166.130.51.43:5001/axis-cgi/jpg/image.cgi?camera=1&resolution=352x240&compression=30&text=0&clock=0&date=0", None, None),
                Billboard("76868", "http://166.130.52.55:5001/axis-cgi/jpg/image.cgi?camera=1&resolution=352x240&compression=30&text=0&clock=0&date=0", None, None),
                Billboard("76869", "http://166.130.52.55:5002/axis-cgi/jpg/image.cgi?camera=1&resolution=352x240&compression=30&text=0&clock=0&date=0", None, None)]

def kenjoh():

    savedIndex = index
    
    for x in kenJohBillboards:
        x.writeImage(savedIndex, path + "/Kenjoh")
        x.updateResponse()

def American():
    savedIndex = index

    for x in americanBillboards:
        x.writeImage(savedIndex, path + "/American")
        x.updateResponse()

def MileHigh():

    savedIndex = index

    for x in MileHighBillboards:
        x.writeImage(savedIndex, path + "/Mile-High")
        x.updateResponse()

#POAW seattle boards
def POAWMass():

    #save current image index
    savedIndex = index

    for x in POAWBillboards:
        x.writeImage(savedIndex, path + "/POAW")
        x.updateResponse()

#function for POAO
def POAOMass():
    savedIndex = index
  
    for x in POAOBillboards:
        x.writeImage(savedIndex, path + "/POAO")
        x.updateResponse()
        
#Main function, not needed but here for organization reasons
def createFolderStructure():

    os.mkdir(path)
    os.mkdir(path + "/American")
    os.mkdir(path + "/Kenjoh")
    os.mkdir(path + "/Mile-High")
    os.mkdir(path + "/POAO")
    os.mkdir(path + "/POAW")

    for i in kenJohBillboards:
        os.mkdir(path + "/Kenjoh/" + i.name)

    for i in americanBillboards:
        os.mkdir(path + "/American/" + i.name)

    for i in MileHighBillboards:
        os.mkdir(path + "/Mile-High/" + i.name)
    
    for i in POAOBillboards:
        os.mkdir(path + "/POAO/" + i.name)

    for i in POAWBillboards:
        os.mkdir(path + "/POAW/" + i.name)

if __name__=='__main__':
    #kenjoh kenjo2020
    #kenjoh camera.812
    #main program loop

    createFolderStructure()

    while(keepRunning):

        #set the seconds to the amount of seconds passed 
        seconds = int(time.time() - time_start) - minutes * 60

        #seconds passed but not keeping track of minutes
        secondsTwo = int(time.time() - time_startTwo) - 0 * 60
        
        #timer for overall program, this is how long the program will run
        if(minutes >= 10):
            keepRunning = False
        else:
            #this is to keep track of minutes, if seconds is over 60 
            if seconds >= 60:
                #add one to minutes and set seconds to 0
                minutes += 1
                seconds = 0
            #this is for the 8 second counter
            if(secondsTwo >= 4):
                #set the 8 second timer to 0
                secondsTwo = 0

                #set the new overall time to the current time
                time_startTwo = time.time()

                #create a thread for the POAO function
                POAOMassThread = threading.Thread(target=POAOMass)

                POAWMassThread = threading.Thread(target=POAWMass)

                MileHighThread = threading.Thread(target=MileHigh)

                AmericanThread = threading.Thread(target=American)

                kenjohThread = threading.Thread(target=kenjoh)
                #start the thread
                POAOMassThread.start()
                POAWMassThread.start()
                MileHighThread.start()
                AmericanThread.start()
                kenjohThread.start()

                #add one to the image index
                index += 1
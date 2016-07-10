import sys
from PyQt4 import QtCore, QtGui
import time
import HV_GUI
from slacker import Slacker # SLACK API
import serial # so we can talk over serial

import plotly, plotly.plotly as py, json, datetime


ser = serial.Serial('/dev/ttyS0', 4800, timeout=3)
print("Serial Line Open")
ser.setDTR(False) #needed to keep data coming over serial without timeout     
time.sleep(1)                                                     
ser.write("1".encode('utf-8')) #get to top menu  
time.sleep(1)                                                     
ser.write("A".encode('utf-8')) #display params                                                                    
time.sleep(1)                                                     
print("Serial Data Sent")

global record
record = 0
#setting global var record to 0 flag used later to 
#decide if we record variables to text file or not


# NEED TO GENERATE ANOTHER SLACK API TOKEN AND PUT IT HERE
#slack = Slacker('') #api token        
slackMessage = "" #can put extra info into the slack message here                                        
print("Slack API set up")

class ConnectThread(QtCore.QThread): # connect thread. so we can constantly read data
    data_downloaded = QtCore.pyqtSignal(object)

    def __init__(self, url):
        QtCore.QThread.__init__(self)
        self.url = url
        print(url + "HERE" ) 

    def run(self):
        global RUN
        while (RUN == 1): # loop forever 
            ser.write("o".encode('utf-8')) #refresh params                                                                         
            input = ser.read(8192).decode().strip().split('\n') # read 8192 bytes or until timeout (set to 3)                      
            self.data_downloaded.emit(input) # data that is sent back. 
            time.sleep(1) #do loop every 2 seconds default *changed to 1 sec

class TimeThread(QtCore.QThread): # time thread. so we can constantly update the time
    setTime = QtCore.pyqtSignal(object)
    print("in Time Thread")
    def __init__(self, url):
        QtCore.QThread.__init__(self)
        print("in _init_ and url is " + url)


    def run(self):
        while True:
                #sets the labels for date and time
            currentTimeOnly = time.strftime("%H:%M:%S")
            currentDateOnly = time.strftime("%d/%m/%Y")
        
            datetime = currentTimeOnly + "|" + currentDateOnly 
            self.setTime.emit(datetime) # data that is sent back. 
            time.sleep(1)
                
class PlotlyThread(QtCore.QThread): # plotly thread.
    Stream = QtCore.pyqtSignal(object)
    print("in Time Thread")
    def __init__(self, url):
        QtCore.QThread.__init__(self)
        print("in Plotly thread")


    def run(self):
        test = "test"
        while True:
            self.Stream.emit(test) # data that is sent back. 
            time.sleep(10)
                

# ===================================================================================

class HV_GUI_App(QtGui.QMainWindow, HV_GUI.Ui_MainWindow):
    def __init__(self):                            # allows us to access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)                         # This is defined in HV_GUI.py file automatically

        self.threads = [] 
        time = TimeThread("Setting_Time")
        time.setTime.connect(self.time_set)
        self.threads.append(time)
        time.start()

        #sets the labels for date and time
     #   currentTimeOnly = time.strftime("%H:%M:%S")
     #   currentDateOnly = time.strftime("%d/%m/%Y")
     #   self.date.setText(currentDateOnly)
     #   self.time.setText(currentTimeOnly)

                                           # It sets up layout and widgets that are defined
        global height
        height = 525
        self.setFixedSize(939, height)                # Fixes windows size - 936 x 729.

        self.set_button.setEnabled(False)
        self.send_button.setEnabled(False)
        self.kill_button.setEnabled(False)
        self.exit_button.setEnabled(True)
        self.disconnect_button.setEnabled(False)

        self.connect_button.clicked.connect(self.connect)

        self.disconnect_button.clicked.connect(self.disconnect)
        self.set_button.clicked.connect(self.set)
        self.send_button.clicked.connect(self.send)
        self.kill_button.clicked.connect(self.kill)
        self.exit_button.clicked.connect(self.exit)
        self.plotly_button.clicked.connect(self.plotlyPressed)
        self.expand_button.clicked.connect(self.expand)

        self.listWidget.setReadOnly(True)

        #POWER BUTTONS
        #self.P_0.stateChanged.connect(self.power)
        #self.P_1.stateChanged.connect(self.power)
        #self.P_2.stateChanged.connect(self.power)
        #self.P_3.stateChanged.connect(self.power)
        #self.P_4.stateChanged.connect(self.power)
        #self.P_5.stateChanged.connect(self.power)
        #self.P_6.stateChanged.connect(self.power)
        #self.P_7.stateChanged.connect(self.power)
        #self.P_8.stateChanged.connect(self.power)

#TODO IS THIS NEEDED? @MF
        for i in range(0,9):
            if i == 1:
                continue
            PowerConnect = "self.P_" + str(i) + ".stateChanged.connect(self.power)"
            eval(PowerConnect)

#Whenever a checkbox is checked or cleared it emits the signal stateChanged(). Connect to this signal if you want to trigger an action each time the checkbox changes state. What else can we connect to?



        print("GUI SET UP")
    
    def time_set(self, datetime):
        currentTime, currentDate = datetime.split('|')
        self.time.setText(currentTime)
        self.date.setText(currentDate)

    def connect(self): #starts the connect thread
        #this thread is used to send data back at the same time 
        # as the GUI is open.
        global RUN
        RUN = 1
        print("Connect Pressed")
        self.connect_button.setEnabled(False)
        self.disconnect_button.setEnabled(True)
        self.set_button.setEnabled(False)
        self.kill_button.setEnabled(True)

        global PowerList
        PowerList = ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"]      
#needs to be defined outside 'set' and 'power'. Peferably at GUI startup? (EDIT does PowerList need to be set back to '-1's since we uncheck the boxes?) I don't like this functionality but it will do for now.
   
        for i in range (0,9):
            if i == 1:
                continue
            Power = "self.P_" + str(i) + ".setEnabled(True)"     #(Re)Enable all power switches so user can change PowerList. 
            eval(Power)
            
        for i in range (0,9):
            Tick = "self.P_" + str(i) + ".setCheckState(False)"        #Automatically uncheck check boxes? Check.
            eval(Tick)

      #  self.threads = [] 
        downloader = ConnectThread("Passing to Connect ")
        downloader.data_downloaded.connect(self.on_data_ready)
        self.threads.append(downloader)
        downloader.start()


    def on_data_ready(self, input): # shit that happens when data comes back from connectThread
         currentTime = time.strftime("%H:%M:%S %d/%m/%Y")
         
         font = QtGui.QFont("Courier")# might only need to do this once, not each time on_data_ready is called
         self.listWidget.setFont(font)
         self.listWidget.insertPlainText("CH#         VMON  IMON   V0     V1     I0    I1    RUP   RDW   T  STATUS : " + currentTime + " \n" )

 #Include datetime, make var with current time, format time to look nice. print it here - some kind of timestamp? look at slack format.
         for i in range (26,35): #loop over the lines with data in them
                serLine = str(input[i]) #uses the data passed back now called input
                print(serLine)  

                self.listWidget.moveCursor(QtGui.QTextCursor.End)
                self.listWidget.ensureCursorVisible() #scrolls to bottom of text input box
                self.listWidget.insertPlainText(serLine)

                channelNum = i - 26 #makes channelNum from the iterator value  
                
                if (channelNum == 0):
                    CH0 = serLine #sets CH0 vars to correct lines
                if (channelNum == 1):
                    CH1 = serLine
                if (channelNum == 2):
                    CH2 = serLine
                if (channelNum == 3):
                    CH3 = serLine
                if (channelNum == 4):
                    CH4 = serLine
                if (channelNum == 5):
                    CH5 = serLine
                if (channelNum == 6):
                    CH6 = serLine
                if (channelNum == 7):
                    CH7 = serLine
                if (channelNum == 8):
                    CH8 = serLine
         
         #splits channel lines to the individual
         #variables splitting on whitespace
         CH0 = CH0.split()
         CH1 = CH1.split()
         CH2 = CH2.split()
         CH3 = CH3.split()
         CH4 = CH4.split()
         CH5 = CH5.split()
         CH6 = CH6.split()
         CH7 = CH7.split()
         CH8 = CH8.split()            


         #write to text file
         global record
         if (record == 1):
             recordFile.write(CH0[1] + ", "+ CH1[1] + ", " + CH2[1] + ", "+ CH3[1] + ", " + CH4[1] + ", "+ CH5[1] + ", " + CH6[1] + ", "+ CH7[1] + ", " + CH8[1] + ", " + currentTime + "\n")
         
# sets the label text to the votlage of each channel
         self.VMon_0.setText(CH0[1]) 
#         self.VMon_1.setText(CH1[1])   #commeneted out as CH1 isnt used
         self.VMon_2.setText(CH2[1]) 
         self.VMon_3.setText(CH3[1])
         self.VMon_4.setText(CH4[1])
         self.VMon_5.setText(CH5[1])
         self.VMon_6.setText(CH6[1])
         self.VMon_7.setText(CH7[1])
         self.VMon_8.setText(CH8[1])

#Fills IMon
         self.IMon_0.setText(CH0[2]) 
#         self.IMon_1.setText(CH1[2])   #commeneted out as CH1 isnt used
         self.IMon_2.setText(CH2[2]) 
         self.IMon_3.setText(CH3[2])
         self.IMon_4.setText(CH4[2])
         self.IMon_5.setText(CH5[2])
         self.IMon_6.setText(CH6[2])
         self.IMon_7.setText(CH7[2])
         self.IMon_8.setText(CH8[2])

#Fills V0 Set
         self.V0_0.setText(CH0[3])
         global V0_0  #TODO Why do we need these to be global?
         V0_0 = CH0[3]

 #        self.V0_1.setText(CH1[3])   #commeneted out as CH1 isnt used

         self.V0_2.setText(CH2[3])
         global V0_2
         V0_2 = CH2[3]

         self.V0_3.setText(CH3[3])
         global V0_3
         V0_3 = CH3[3]

         self.V0_4.setText(CH4[3])
         global V0_4
         V0_4 = CH4[3]

         self.V0_5.setText(CH5[3])
         global V0_5
         V0_5 = CH5[3]

         self.V0_6.setText(CH6[3])
         global V0_6
         V0_6 = CH6[3]

         self.V0_7.setText(CH7[3])
         global V0_7
         V0_7 = CH7[3]

         self.V0_8.setText(CH8[3])
         global V0_8
         V0_8 = CH8[3]

#Fills V1 Set --- FUTURE
#         self.V1_0.setText(CH0[4])
#         self.V1_1.setText(CH1[4])   #commeneted out as CH1 isnt used
#         self.V1_2.setText(CH2[4])
#         self.V1_3.setText(CH3[4])
#         self.V1_4.setText(CH4[4])
#         self.V1_5.setText(CH5[4])
#         self.V1_6.setText(CH6[4])
#         self.V1_7.setText(CH7[4])
#         self.V1_8.setText(CH8[4])

#Fills I0 Set
         self.I0_0.setText(CH0[5])
         global I0_0
         I0_0 = CH0[5]

#         self.I0_1.setText(CH1[5])   #commeneted out as CH1 isnt used

         self.I0_2.setText(CH2[5])
         global I0_2
         I0_2 = CH2[5]

         self.I0_3.setText(CH3[5])
         global I0_3
         I0_3 = CH3[5]

         self.I0_4.setText(CH4[5])
         global I0_4
         I0_4 = CH4[5]

         self.I0_5.setText(CH5[5])
         global I0_5
         I0_5 = CH5[5]

         self.I0_6.setText(CH6[5])
         global I0_6
         I0_6 = CH6[5]

         self.I0_7.setText(CH7[5])
         global I0_7
         I0_7 = CH7[5]

         self.I0_8.setText(CH8[5])        
         global I0_8
         I0_8 = CH8[5]



#Fills I1 Set --- FUTURE
#         self.I1_0.setText(CH0[6])
#         self.I1_1.setText(CH1[6])   #commeneted out as CH1 isnt used
#         self.I1_2.setText(CH2[6])
#         self.I1_3.setText(CH3[6])
#         self.I1_4.setText(CH4[6])
#         self.I1_5.setText(CH5[6])
#         self.I1_6.setText(CH6[6])
#         self.I1_7.setText(CH7[6])
#         self.I1_8.setText(CH8[6])

#Fills Ramp Up Speed
         self.RUP_0.setText(CH0[7])
         global RUP_0
         RUP_0 = CH0[7]

#         self.RUP_1.setText(CH1[7])   #commeneted out as CH1 isnt used

         self.RUP_2.setText(CH2[7])
         global RUP_2
         RUP_2 = CH2[7]

         self.RUP_3.setText(CH3[7])
         global RUP_3
         RUP_3 = CH3[7]

         self.RUP_4.setText(CH4[7])
         global RUP_4
         RUP_4 = CH4[7]

         self.RUP_5.setText(CH5[7])
         global RUP_5
         RUP_5 = CH5[7]

         self.RUP_6.setText(CH6[7])
         global RUP_6
         RUP_6 = CH6[7]

         self.RUP_7.setText(CH7[7])
         global RUP_7
         RUP_7 = CH7[7]

         self.RUP_8.setText(CH8[7])
         global RUP_8
         RUP_8 = CH8[7]


#Fills Ramp Down Speed
         self.RDN_0.setText(CH0[8])
         global RDN_0
         RDN_0 = CH0[8]

#         self.RDN_1.setText(CH1[8])   #commeneted out as CH1 isnt used

         self.RDN_2.setText(CH2[8])
         global RDN_2
         RDN_2 = CH2[8]

         self.RDN_3.setText(CH3[8])
         global RDN_3
         RDN_3 = CH3[8]

         self.RDN_4.setText(CH4[8])
         global RDN_4
         RDN_4 = CH4[8]

         self.RDN_5.setText(CH5[8])
         global RDN_5
         RDN_5 = CH5[8]

         self.RDN_6.setText(CH6[8])
         global RDN_6
         RDN_6 = CH6[8]

         self.RDN_7.setText(CH7[8])
         global RDN_7
         RDN_7 = CH7[8]

         self.RDN_8.setText(CH8[8])
         global RDN_8
         RDN_8 = CH8[8]


#Fills Trip Time
         self.trip_0.setText(CH0[9])
         global trip_0
         trip_0 = CH0[9]

#         self.trip_1.setText(CH1[9])   #commeneted out as CH1 isnt used

         self.trip_2.setText(CH2[9])
         global trip_2
         trip_2 = CH2[9]

         self.trip_3.setText(CH3[9])
         global trip_3
         trip_3 = CH3[9]

         self.trip_4.setText(CH4[9])
         global trip_4
         trip_4 = CH4[9]

         self.trip_5.setText(CH5[9])
         global trip_5
         trip_5 = CH5[9]

         self.trip_6.setText(CH6[9])
         global trip_6
         trip_6 = CH6[9]

         self.trip_7.setText(CH7[9])
         global trip_7
         trip_7 = CH7[9]

         self.trip_8.setText(CH8[9])
         global trip_8
         trip_8 = CH8[9]


# Fills Status Info
         self.S_0.setText(CH0[10])
#         self.S_1.setText(CH1[10])   #commeneted out as CH1 isnt used
         self.S_2.setText(CH2[10]) 
         self.S_3.setText(CH3[10])
         self.S_4.setText(CH4[10])
         self.S_5.setText(CH5[10])
         self.S_6.setText(CH6[10])
         self.S_7.setText(CH7[10])
         self.S_8.setText(CH8[10])

#if CH0[10] = TRIP then set text to red, send message over SLACK. 

############   CODE FOR SENDING TO SLACK ########################
         TRIP = False #this is set here and changed later if a channel trips                                                                                                           
         for i in range(0,8):
             CHNum = "CH" + str(i)
             CHNumOption = str(CHNum) + "[10]"

#             print(eval (CHNumOption)) # from stackOverflow 295058

             # this next block looks at the STATUS of the channel
             # and does some things depending what the result is
             # like sending group messages on SLACK if OVC/TRIP

             if (eval(CHNumOption) == "TRIP"):

            # if CHNumOption (looks at ch varaibles) for "TRIP" if found on a line
            # it sets TRIP to true and adds a line saying this channel has tripped to slackMessage

                 currentTime = time.strftime("%c")
                 slackPreMessage = "Automated Message from HV Supply (%s) " % currentTime

                 TRIP = True
                 global slackMessage 
                 slackMessage = str(slackMessage) + "\n Channel " + str(i) + " has TRIPPED"


         if (TRIP == True):
             print(slackPreMessage)
             print(slackMessage)
             slack.chat.post_message('#testing', slackPreMessage, as_user="caen_hv_supply", attachments=[{"text": slackMessage, "color":"#FF0000"}])
    
#post message to group #testing as user 'caen_hv_supply' with a preMessage
# of the time and date. and the main message, slackMessage, as an
#attachment which allows a colour tab next to the message.

############ //  CODE FOR SENDING TO SLACK #########################     

    def disconnect(self):
        print("Disconnect Pressed")
        global RUN
        RUN = 0
        self.disconnect_button.setEnabled(False)
        self.connect_button.setEnabled(True)
        self.set_button.setEnabled(True)
        self.send_button.setEnabled(False)

##  add stuff here to kill loop

    def set(self):
        print("Set Pressed")
        self.send_button.setEnabled(True)
        
        global ValuesSet, Elements, Command
        ValuesSet = []                                                   #An "array" of values that are changed by user in the GUI.
        Elements = ["V0","I0","RUP","RDN","trip","P"]                    #Just strings used in for loop below. 
        Limits = [1500, 10, 10, 20, 0, 1]                                #Highest value that can be set by user. Indices MUST correspond to Elements list. 
        Command = ["C","F","I","J","L","N"]                              #Letter used by serial to edit value.   Indices MUST correspond to Elements list.
        #Units = [] 
        
        for i in range (0,9):                                     #For loop for number of channels, I'd rather this value came from somewhere rather than hard-coded.
            ValuesSet.append([])                                  #Add a list inside ValuesSet for every channel -> [[V0_0, I0_0,...],[V0_1, I0_1,...],...,[V0_n, I0_n,...]].
            for j in range (0,len(Elements)):                     #len(Elements) returns length of 'Elements' list. Will continue for loop for this number. 
                if i == 1:                                        #   v
                    ValuesSet[i].insert(i, -1)                    #   Since channel 1 isn't working, will need to be removed when it is.
                    continue                                      #   ^
                ValuesSet[i].insert(j, -1)                        #For 'i'th channel, insert '-1' for every value the user can change.
                Element = str(Elements[j]) + "_" + str(i)         #Program creates a string using constituents of 'Elements' list, e.g. the V0 of channel 6 will become "V0_6". This is now equal to the value that has pulled from the HV supply.
                if Elements[j] != "P":                            #i.e. do something different for Power. See 'else'.
                    SetElement = "self." + Element + ".text()"    #Creates another string ("self.V0_6.text()"), that will be equal to the users entry.                                  
                    if (int(eval(SetElement)) > Limits[j]):       #If the value entered by the user is above the 'Limit' (which we want hard-coded!), do not save and ...
                        print(str(eval(SetElement)) + " too high. Value unchanged. Max = " + str(Limits[j])) # ... return this warning.
                    elif (eval(Element) != eval(SetElement)):     #If the user has changed the value (i.e. value they have "set" for "element" is not equal (!=) to value pulled ...
                        ValuesSet[i][j] = eval(SetElement)        #... from supply, save it to ValuesSet array in the 'i'th channel for the 'j'th element.
                        #elif put '-1', maybe?...
                else:
                    #Am I able to determine the state of the switch, and therefore set value to 1/-1?
                    ValuesSet[i][j] = eval(PowerList[i])          #Set 'Power'th element to value in PowerList list. See power function defined below.
        print(ValuesSet)

    def send(self):
        print("Send Pressed")
        self.send_button.setEnabled(False)
        self.set_button.setEnabled(False)

        for i in range (0,9):
            Power = "self.P_" + str(i) + ".setEnabled(False)"             #Disable all power switches to stop user changing PowerList. Do this for all elements above! 
            eval(Power)
       
        wait = 0.5                                                        #Added for testing (rather than changing ALL time.sleep(amounts)!). Would like this value to be smaller, obviously.
        
        ser.write("1".encode('utf-8'))                                    #"1" will always ensure we know "where we are" in the serial menu. Is there a "go to screen" function for python ...  
        time.sleep(wait)                                                  # ... when communicating with a serial? Would ensure faster comminucation...
        ser.write("B".encode('utf-8'))                                    #DISPLAY/MODIFY PARAMETERS
        time.sleep(wait)
        ser.write("A".encode('utf-8'))                                    #SINGLE CHANNEL
        time.sleep(wait)
        for i in range (0,9):                                             #Repeat below commands for a maximum (see below) of 9 channels (again, would like this value to come from somewhere) 
            if sum(int(n) for n in ValuesSet[i]) != len(ValuesSet[i])*-1: #If sum of values in ValuesSet (per channel) is not equal to the negative of the total number of Elements, switch to that channel, because something needs to be changed (since unchanged values are set equal to -1). In other words if nothing has changed for that channel all elements summed will add up to -(Total Number of Elements), so don't switch to it!  
                    print("Switching to Channel " + str(i) + "...")
                    ser.write("A".encode('utf-8'))                        #Switch to CHANNEL NAME [CH##] screen.
                    time.sleep(wait)
                    ser.write("C".encode('utf-8'))                        #Literally - "Type 'C'"
                    time.sleep(wait)
                    ser.write("H".encode('utf-8'))
                    time.sleep(wait)
                    ser.write("0".encode('utf-8'))                        #Type '0' - This means the current program won't work for channels '10' and above! Very easy to change. (but then the GUI would physically need to be changed too!
                    time.sleep(wait)
                    ser.write(str(i).encode('utf-8'))                     #Type whichever number corresponds to the channel that needs editing. This will so far only work for single digits!
                    time.sleep(wait)
                    ser.write("\r\n".encode('ascii'))                     #Literally - "Press 'Enter'".
                    time.sleep(wait)
            for j in range (0,len(Elements)):
                if ValuesSet[i][j] != -1:                                 #Do the below for the 'i'th channel, if the 'j'th element has been changed, i.e. is not equal to -1!
                    if Elements[j] != "P":                                #Do the below for all elements that aren't 'Power'. This is because the checkboxes behave differently to text fields.  
                        print("Setting " + ValuesSet[i][j] + " for " + Elements[j] + "...")                  
                        ser.write(Command[j].encode('utf-8'))             #Literally - type whichever letter (stored in Command list) corresponds with the value that needs changing. Shares it's index with Elements.
                        time.sleep(wait)
                        Value = list(ValuesSet[i][j])                     #Create (temporary) list equal to the edited value. If ValuesSet[i][j] = 1500, Value = [1,5,0,0].
                        for k in range (0,len(Value)):                    #If Value = 1500, len(Value) = 4, so repeat below 4 times. This allows values of different orders to be input.
                            ser.write(Value[k].encode('utf-8'))           #1: Type '1'. 2: Type '5'. 3: Type '0'. 4: Type '0'.
                            time.sleep(wait)
                        ser.write("\r\n".encode('ascii'))
                        print("Value set.")
                        time.sleep(wait)
                    else:
                        print("Toggling power...")
                        ser.write(Command[j].encode('utf-8'))             #For this channel, type 'N' is the box was checked. This will toggle power.
                        time.sleep(wait)
        print("Returning to main screen...")
        ser.write("1".encode('utf-8'))                                       #goes back to display status screen, ...
        time.sleep(wait)                                                     # ... would rather this happened when ...
#        ser.write("A".encode('utf-8'))                                       # ... connect is pressed.
#        time.sleep(wait)
        #print("Change CH0" + str(i) + " for which " + str(ValuesSet[i][j]) + " is the new value, located at element " + str(j) + " which is " + str(Elements[j]))
        print("Done.")
        
    def power(self):
        global PowerList

        if self.P_0.isChecked():
            PowerList[0] = "1"
        else:
            PowerList[0] = "-1"
        if self.P_1.isChecked():
            PowerList[1] = "1"
        else:
            PowerList[1] = "-1"
        if self.P_2.isChecked():
            PowerList[2] = "1"
        else:
            PowerList[2] = "-1"
        if self.P_3.isChecked():
            PowerList[3] = "1"
        else:
            PowerList[3] = "-1"
        if self.P_4.isChecked():
            PowerList[4] = "1"
        else:
            PowerList[4] = "-1"
        if self.P_5.isChecked():
            PowerList[5] = "1"
        else:
            PowerList[5] = "-1"
        if self.P_6.isChecked():
            PowerList[6] = "1"
        else:
            PowerList[6] = "-1"
        if self.P_7.isChecked():
            PowerList[7] = "1"
        else:
            PowerList[7] = "-1"
        if self.P_8.isChecked():
            PowerList[8] = "1"
        else:
            PowerList[8] = "-1"
            
        print(PowerList)
    
    def plotlyPressed(self):
        
        with open('plot.ly.config.json') as config_file:
            plotly_user_config = json.load(config_file)

            url = py.plot([
                    {
                        'x': [],
                        'y': [],
                        'mode': 'lines+markers',
                        'stream': 
                        {
                            'token': plotly_user_config['plotly_stream_ids'][0],
                            'maxpoints': 20000
                        }
                    },{
                        'x': [],
                        'y': [],
                        'mode': 'lines+markers',
                        'stream': 
                        {
                            'token': plotly_user_config['plotly_stream_ids'][1],
                            'maxpoints': 20000
                        }
                    }], name='HV Voltage Supply', auto_open=False)

            global stream_CH02, stream_CH08 
            stream_CH02 = py.Stream(plotly_user_config['plotly_stream_ids'][0])
            stream_CH08 = py.Stream(plotly_user_config['plotly_stream_ids'][1])
            #print(plotly_user_config['plotly_stream_ids'][0])
            #print(plotly_user_config['plotly_stream_ids'][1])
            stream_CH02.open()
            stream_CH08.open()
            print ("Plotly stream(s) set up.")

            print("I AM RUN ONCE??")
            self.threads = [] 
            plotly = PlotlyThread("Streaming")
            plotly.Stream.connect(self.plotly)
            self.threads.append(plotly)
            plotly.start()

    def plotly(self, nothing):
        print("Streaming to Plot.ly...")

      #  try:
        d = datetime.datetime.now()
        d = d.strftime('%Y-%m-%d %H:%M:%S')
        
        y = int(self.VMon_2.text()) #on at the time (08/07/16 14:20)... fluctuating between 3V and 4V
        y2 = int(self.VMon_8.text())

        stream_CH02.write({'x': d, 'y': y})
        stream_CH08.write({'x': d, 'y': y2})
        print("stream data sent")
            
            #could take average value over the minute to send to plotly 
                
            #if (i % 10 == 0):
            #print("Saved Graph")
                
      #  except:
      #      print("ERROR")

    def kill(self): #hijacking this for record button
        global record
        currentTime = time.strftime("%H:%M:%S %d/%m/%Y")

        if (record == 0):
            #open file
            global recordFile
            recordFile = open('HV_Record.txt','a')
            recordFile.write("CH1, CH2, CH3, CH4, CH5, CH6, CH7, CH8, CH9 : " + currentTime + " \n")

            record = 1 
            print("File Opened + Recording.")
            #change button label to "End Record"
            
        elif (record == 1):
            #close file and upload to elog in one move? or just close file
            record = 0
            print("Record Pressed again, file closing.")
            recordFile.write("File Closed at " + currentTime + " \n")
            recordFile.close()
            #change button label to "Record" again
       

    def exit(self):
        print("GUI has been terminated")
        self.deleteLater()

    def expand(self): #setIcon() mess around with "Ubuntu" arrows.
        global height
        print ("Window resized.")
        if height == 525:
            self.setFixedSize(939, 731)
            height = 731
        else:
            self.setFixedSize(939, 525)
            height = 525
        
# =============================================================================================

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = HV_GUI_App()
    window.show()
    sys.exit(app.exec_())



#TODO- find a way to stop the autofil when a value is changed to be set
# plot the voltages over time (could live stream with plotly
# make sure window is not re-sizeable 
# make a window that does and monitors HV trainin

#HV Cable # in GUI to help debug trips and stuff.
#Realtime graphing of data over serial: http://playground.arduino.cc/Interfacing/Python

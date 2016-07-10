import sys
from PyQt4 import QtCore, QtGui
import time
import HV_GUI
from slacker import Slacker # SLACK API
import serial # so we can talk over serial

ser = serial.Serial('/dev/ttyS0', 4800, timeout=3)

print("Serial Line Open")
ser.setDTR(False) #needed to keep data coming over serial without timeout     
time.sleep(0.25)                                                     
ser.write("1".encode('utf-8')) #get to top menu  
time.sleep(0.25)                                                     
ser.write("A".encode('utf-8')) #display params                                                                    
print("Serial Data Sent")


slack = Slacker('xoxb-44847750660-eYVraklA1Aog95VzBv1hx4V0') #api token        
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
            time.sleep(2) #do loop every 2 seconds

# ===================================================================================

class HV_GUI_App(QtGui.QMainWindow, HV_GUI.Ui_MainWindow):
    def __init__(self):                            # allows us to access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)                         # This is defined in HV_GUI.py file automatically
                                                   # It sets up layout and widgets that are defined

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

        self.listWidget.setReadOnly(True)
                
        print("GUI SET UP")


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

        self.threads = [] 
        downloader = ConnectThread("Passing to Connect ")
        downloader.data_downloaded.connect(self.on_data_ready)
        self.threads.append(downloader)
        downloader.start()


    def on_data_ready(self, input): # shit that happens when data comes back from connectThread

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
         global V0_0 
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

############ //  CODE FOR SENDING TO SLACK ##########################

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
        
        global ValuesSet, Elements
        ValuesSet = []
        Elements = ["V0_","I0_","RUP_","RDN_","trip_"]
        Limits = [1500, 10, 10, 20, 0]
        #Units = []
        
        for i in range (0,9): #Number of channels, I'd rather this number came from somewhere.
            ValuesSet.append([]) 
            for j in range (0,len(Elements)):
                Element = str(Elements[j]) + str(i)
                SetElement = "self." + Element + ".text()"
                if i == 1:
                    ValuesSet[i].insert(i, -1)
                    continue
                ValuesSet[i].insert(j, -1)
                if (int(eval(SetElement)) > Limits[j]):
                    print(str(eval(SetElement)) + " too high. Value unchanged. Max = " + str(Limits[j]))
                elif (eval(Element) != eval(SetElement)):
                    ValuesSet[i][j] = eval(SetElement) #else if put '-1' maybe?...
        print(ValuesSet)

    #def ControlHV(self, ModifyParameters = []):

    def send(self):
        print("Send Pressed")
        print("Writing changes...") #or whatever
        self.send_button.setEnabled(False)
        for i in range (0,9):
            for j in range (0,len(Elements)):
                if ValuesSet[i][j] != -1:
                    wait = 0.5
                    channel = str(i)
        
                    ser.write("1".encode('utf-8'))
                    time.sleep(wait)
                    ser.write("B".encode('utf-8'))
                    time.sleep(wait)
                    ser.write("A".encode('utf-8'))
                    time.sleep(wait)
                    ser.write("A".encode('utf-8'))
                    time.sleep(wait)
                    ser.write("C".encode('utf-8'))
                    time.sleep(wait)
                    ser.write("H".encode('utf-8'))
                    time.sleep(wait)
                    ser.write("0".encode('utf-8'))
                    time.sleep(wait)
                    ser.write(channel.encode('utf-8')) #str(i) straight in here?
                    time.sleep(wait)
                    ser.write("\r\n".encode('ascii'))
                    time.sleep(wait)
                        
                    command = ["C","F","I","J","L"]
                    ser.write(command[j].encode('utf-8'))
                    time.sleep(wait)
                    Value = list(ValuesSet[i][j])
                    for k in range (0,len(Value)):
                        ser.write(Value[k].encode('utf-8'))
                        time.sleep(wait)
                    ser.write("\r\n".encode('ascii'))
                    time.sleep(wait)

                    ser.write("1".encode('utf-8')) #goes back to display status screen,
                    time.sleep(wait)               #would rather this happened when 
 
                    #print("Change CH0" + str(i) + " for which " + str(ValuesSet[i][j]) + " is the new value, located at element " + str(j) + " which is " + str(Elements[j]))
        print("Done.")
        
        

    def kill(self):
        print("Process Killed")

    def exit(self):
        print("GUI has been terminated")
        self.deleteLater()

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

#HV Cabel # in GUI to help debug trips and stuff.

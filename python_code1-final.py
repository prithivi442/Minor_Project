import ctypes
import SocketServer


def media_play():
    
    #Press the play key in order to see output
    
    PressKey(0xB3) #press play/pause
    
    ReleaseKey(0xB3) #release play/pause

def media_stop():
    
    #Press the stop key in order to see output
    
    PressKey(0xB2) #press stop
   
    ReleaseKey(0xB2) #release stop

def volume_up():
    
    #Press the volume up key in order to see output
    
    PressKey(0xAF) #press volume up
    #time.sleep(2)
    ReleaseKey(0xAF) #release volume up

def volume_down():
    
    #Press the volume down key in order to see output
    
    PressKey(0xAE) #press volume down
    #time.sleep(2)
    ReleaseKey(0xAE) #release volume down

def media_next():
    
    #Press media_next to change current song

    PressKey(0x27) #media next simulation press
    #time.sleep(2)
    ReleaseKey(0x27) #media next simulation release

def media_previous():
    
    #Press media_previous to change current song   

    PressKey(0x25) #media previous simulation press
    #time.sleep(2)
    ReleaseKey(0x25) #media previous simulation release


def ppt_next():
    
    #Press ppt_next to change current slide

    PressKey(0x20) #slide next simulation press pressing space
    #time.sleep(1)
    ReleaseKey(0x20) #slide next simulation release

def ppt_previous():
    
    #Press ppt_previous to change current slide

    PressKey(0x25) #slide previous simulation pressing left arrow
    #time.sleep(1)
    ReleaseKey(0x25) #slide previous simulation release


def ppt_slideshow():
    
    #Press ppt_slideshow to slideshow the slide from beganing

    PressKey(0x7A) #slideshow simulation pressing f5
    #time.sleep(1)
    ReleaseKey(0x7A) #slidehow simulation releasing f5

#simulation process
SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions

PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


# simulation functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(hexKeyCode, 0x48, 0, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(hexKeyCode, 0x48, 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def simulate(x):
    str(x)
    try:
        if x == "stop":
            media_stop()
                    
        elif x == "next":
            media_next()

        elif x == "play":
            media_play()
    
        elif x == "vdwn":
            volume_down()

        elif x == "vup":
            volume_up()

        elif x == "prev":
            media_previous()

        elif x == "srht":
            ppt_next()

        elif x == "sleft":
            ppt_previous()

        elif x == "ejct":
            ppt_slideshow()

        #elif x == "stop#
            #AltTab()

        #elif x == 1010:
                #Shut_down()

        #elif x == 1011:
            #Shut_down_confirm()

        #elif x == 1011:
            # cancel_request()

        #else:
            #break
    
            
    except KeyboardInterrupt:
        #print "Phew! Done Searching"
        sys.exit()

if __name__ == "__main__":

    class MyTCPHandler(SocketServer.BaseRequestHandler):
        """
    The RequestHandler class for our server.
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
 
        def handle(self):
            # self.request is the TCP socket connected to the client
            self.data = self.request.recv(1024).strip()
            if self.data:
                simulate(self.data)
            
            print self.data


#HOST = check_output("ifconfig wlan0 | grep \"inet addr\" | awk '{print $2}' | awk -F: '{print $2}'",shell=True)
HOST= '192.168.43.40'
PORT=9999

if __name__ == "__main__":
    #if not getuid():
        
        #HOST, PORT = defns.IP_ADDRESS, defns.PORT
        # Create the server, binding to localhost on port 9999
        #try:
        if(HOST==""):
            print "Seems your wi-fi is off. Try again after connecting to a wifi"
            exit(1)
        SocketServer.TCPServer.allow_reuse_address = True
        server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
        try:
            print"\n\n...WELCOME... \n"
            print "Remote is running...\n"
            print "IP address:   {}".format(HOST)
            print "PORT:         {}".format(PORT)
            print "\nCtrl+c to exit."
            server.serve_forever()
        except KeyboardInterrupt:
            server.shutdown()
            print "\nGoodbye."
    
        except socerr:
            print "Sorry, something's wrong."

        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C

if __name__ == "__main__":
    #if not getuid():
        
        #HOST, PORT = defns.IP_ADDRESS, defns.PORT
        # Create the server, binding to localhost on port 9999
        #try:
        if(HOST==""):
            print "Seems your wi-fi is off. Try again after connecting to a wifi"
            exit(1)
        SocketServer.TCPServer.allow_reuse_address = True
        server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
        try:
            print"\n\n...WELCOME... \n"
            print "Remote is running...\n"
            print "IP address:   {}".format(HOST)
            print "PORT:         {}".format(PORT)
            print "\nCtrl+c to exit."
            server.serve_forever()
        except KeyboardInterrupt:
            server.shutdown()
            print "\nGoodbye."
    

        except socerr:
            print "Sorry, something's wrong."

        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        
    


    
    



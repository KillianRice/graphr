import verdi_config
import serial
from datetime import datetime

class verdi_command:
    def __init__(self, nickname = 'Set Power (W)', command = b'?SP\r\n'):
        self.nickname = nickname
        if command[-2:] != b'\r\n':
            self.command = command + b'\r\n'
        else:
            self.command = command
    def send_command(self, ser):
        """ writes verdi command to serial port ser, returns response from laser"""
        ser.write(self.command)
        response = ser.readline()
        return response

def get_verdi_commands():
    commands = []
    for c in verdi_config.COMMANDS:
        commands.append(
                verdi_command(c,verdi_config.COMMANDS[c])
            )
    return commands

def start_verdi_session():
    ser = serial.Serial(**verdi_config.SESSION)
    return ser

class Verdi(object):

    def __init__(self, get_commands = True, start_session = True, datafile = None):
        if get_commands:
            self.commands = get_verdi_commands()
        if start_session:
            self.session = start_verdi_session()
        if datafile != None:
            self.datafile = datafile
        else:
            self.datafile = 'data.txt'
        self.onStandby = verdi_command('On Standby', b'?L')

    def write_verdi_header(self, otherFile = None):
        if otherFile == None:
            f = open(self.datafile, 'w+')
        else:
            f = open(otherFile, 'w+')
        for c in self.commands[:-1]:
            f.write(c.nickname+'\t')
        f.write(self.commands[-1].nickname+'\n')
        
        if otherFile == None:
            f.close()
            return 0
        else:
            return f
            

    def get_verdi_data(self, mode='a'):
        """Records the responses for each command in 'commands' from the verdi on Serial port 'ser' into the file 'datafile'"""
        ## check that the laser is not off or in a fault
        onStandby = float(self.onStandby.send_command(self.session))
        
        if onStandby == 1:
            s = ''
            
            # flush the input buffer if there are bits waiting
            if self.session.inWaiting() > 0:
                self.session.read(ser.inWaiting())
            
            # add the date and time for the current data point
            s += str(datetime.now())+'\t'
            
            # loop over the commands and get their responses
            for c in self.commands[:-1]:
                r = float(c.send_command(self.session))
                s += '%.8e\t'%r
            r = float(self.commands[-1].send_command(self.session))
            s += '%.8e\n'%r
            
            # write to the datafile
            f = open(self.datafile, mode)
            f.write(s)
            f.close()

            return s
        
        else:
            
            return ''


    def verdi_test(self):
        passed = True
        for c in self.commands[:-1]:
            try:
                print('Sending command ' + c.nickname)
                r = float(c.send_command(self.session))
                print(c.nickname + '\t' + '%.8e'%r)
            except:
                print('Failed to send command ' + c.nickname)
                passed = False
                break
        return passed
                
                

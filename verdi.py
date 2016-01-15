import verdi_config
import serial

class verdi_command:
    def __init__(self, nickname = 'Set Power (W)', command = b'?SP\r\n', return_bytes = 8):
        self.nickname = nickname
        if command[-2:] != b'\r\n':
            self.command = command + b'\r\n'
        else:
            self.command = command
        self.return_bytes = return_bytes
    def send_command(self, ser):
        """ writes verdi command to serial port ser, returns response from laser"""
        ser.write(self.command)
        response = ser.readline()
        if response[-2:] != b'\r\n':
            print(ser.inWaiting())
            response += ser.read(ser.inWaiting())
            return response
        else:
            return response

def start_verdi_session():
    ser = serial.Serial(**verdi_config.SESSION)
    return ser

def get_verdi_commands():
    commands = []
    for c in verdi_config.COMMANDS:
        commands.append(
                verdi_command(c,verdi_config.COMMANDS[c])
            )
    return commands


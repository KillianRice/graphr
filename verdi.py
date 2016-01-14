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


__COMMANDS__ = [
    verdi_command('Set Power (W)', b'?SP', 8),
    verdi_command('Output Power (W)', b'?P', 7),
    verdi_command('Current (A)', b'?C', 6),
    verdi_command('Current Delta (A)', b'?CD', 5),
    verdi_command('Baseplate Temp (C)', b'?BT', 7),
    verdi_command('Diode 1 Current (A)', b'?d1c', 6),
    verdi_command('Diode 1 Photocell Voltage (V)', b'?d1pc', 6),
    verdi_command('Diode 1 Set Temp (C)', b'?d1st', 7),
    verdi_command('Diode 1 Temp (C)', b'?d1t', 7),
    verdi_command('Diode 1 Heatsink Temp (C)', b'?d1hst', 7),
    verdi_command('Diode 1 Hours (hr)', b'?d1h', 10),
    verdi_command('Diode 1 RCF', b'?d1rcf', 6),
    verdi_command('Diode 1 Max Current (A)', b'?d1rcm', 7),
    verdi_command('Diode 2 Current (A)', b'?d2c', 6),
    verdi_command('Diode 2 Photocell Voltage (V)', b'?d2pc', 6),
    verdi_command('Diode 2 Set Temp (C)', b'?d2st', 7),
    verdi_command('Diode 2 Temp (C)', b'?d2t', 7),
    verdi_command('Diode 2 Heatsink Temp (C)', b'?d2hst', 7),
    verdi_command('Diode 2 Hours (hr)', b'?d2h', 10),
    verdi_command('Diode 2 RCF', b'?d2rcf', 6),
    verdi_command('Diode 2 Max Current (A)', b'?d2rcm', 7),
    verdi_command('Etalon Temp (C)', b'?et', 7),
    verdi_command('Vanadate Set Temp (C)', b'?vst', 7),
    verdi_command('Vanadate Temp (C)', b'?vt', 7),
    verdi_command('Power Supply Hours (hr)', b'?psh', 10),
    verdi_command('Laser Head Hours (hr)', b'?HH', 10),
    verdi_command('Vanadate Temp Servo Drive', b'?VD', 10),
    verdi_command('Diode 1 Temp Servo Drive', b'?d1td', 10),
    verdi_command('Diode 2 Temp Servo Drive', b'?d2td', 10),
    verdi_command('Etalon Temp Servo Drive' , b'?ed', 10),
]

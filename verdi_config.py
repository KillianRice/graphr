import serial

#### Verdi serial port configuration settings ####
SESSION = { 
        'port'          : '/dev/tty.usbserial-AL009OE0',# the port for the verdi
        'baudrate'      : '19200',               # default is 19200
        'stopbits'      : serial.STOPBITS_ONE,   # default is stopbits_one
        'parity'        : serial.PARITY_NONE,    # default is parity_none
        'rtscts'        : False                 # default is false
        }

#### Verdi command dictionary ####
# all commands in this list will be sent to the verdi
# and their responses will be recorded.
COMMANDS = {
        'Set Power (W)'                 : b'?SP',
        'Output Power (W)'              : b'?P',
        'Current (A)'                   : b'?C',
        'Current Delta (A)'             : b'?CD',
        'Baseplate Temp (C)'            : b'?BT',
        'Diode 1 Current (A)'           : b'?d1c',
        'Diode 1 Photocell Voltage (V)' : b'?d1pc',
        'Diode 1 Set Temp (C)'          : b'?d1st',
        'Diode 1 Temp (C)'              : b'?d1t',
        'Diode 1 Heatsink Temp (C)'     : b'?d1hst',
        'Diode 1 Hours (hr)'            : b'?d1h',
        'Diode 1 RCF'                   : b'?d1rcf',
        'Diode 1 Max Current (A)'       : b'?d1rcm',
        'Diode 2 Current (A)'           : b'?d2c',
        'Diode 2 Photocell Voltage (V)' : b'?d2pc',
        'Diode 2 Set Temp (C)'          : b'?d2st',
        'Diode 2 Temp (C)'              : b'?d2t',
        'Diode 2 Heatsink Temp (C)'     : b'?d2hst',
        'Diode 2 Hours (hr)'            : b'?d2h',
        'Diode 2 RCF'                   : b'?d2rcf',
        'Diode 2 Max Current (A)'       : b'?d2rcm',
        'Etalon Temp (C)'               : b'?et',
        'Vanadate Set Temp (C)'         : b'?vst',
        'Vanadate Temp (C)'             : b'?vt',
        'Power Supply Hours (hr)'       : b'?psh',
        'Laser Head Hours (hr)'         : b'?HH',
        'Vanadate Temp Servo Drive'     : b'?VD',
        'Diode 1 Temp Servo Drive'      : b'?d1td',
        'Diode 2 Temp Servo Drive'      : b'?d2td',
        'Etalon Temp Servo Drive'       : b'?ed'
    }


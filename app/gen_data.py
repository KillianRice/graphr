import numpy as np
from numpy import random
from datetime import datetime
import time

def printdata(f, data):
    ts = datetime.now()
    f.write(str(ts))
    f.write('\t')
    for i in data[:-1]:
        f.write('%.18e\t'%i)
    f.write('%.18e\n'%data[-1])

### DEBUGGING ###
debug = True
if debug:
    filemode = 'w'
else:
    filemode = 'a'

###
data = np.zeros(4)
datafile = 'data.txt'
header = 'a\tb\tc\td\n'
f = open(datafile, filemode)
f.write(header)
f.close()
while True:
    f = open(datafile, 'a')
    printdata(f,data)
    data += random.randn(4)
    f.close()
    print(data)
    time.sleep(.300)











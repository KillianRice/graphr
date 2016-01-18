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
updatefile = 'most_recent.txt'
header = 'a\tb\tc\td\n'
f = open(datafile, filemode)
f.write(header)
f.close()
while True:
    f = open(datafile, 'a')
    g = open(updatefile, 'w')
    g.write(header)
    printdata(g,data)
    printdata(f,data)
    data += random.randn(4)
    f.close()
    g.close()
    #print(data)
    time.sleep(.300)











import verdi
from datetime import datetime

datadir = '/media/KillianDrobo/Neutral/Equipment & Laser Systems/Laser System - 532nm - Lattice/pi_log'
#datadir = 'data'
fname = datadir+'/'+datetime.now().strftime('%Y.%m.%d_neutral_verdi.txt')
tempfile = 'app/most_recent.txt'
v = verdi.Verdi(datafile = fname)
v.write_verdi_header()
while True:
    s = v.get_verdi_data()
    f = v.write_verdi_header(otherFile = tempfile)
    f.write(s)
    f.close()

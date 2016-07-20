import verdi
from datetime import datetime

#### Define Variables ####
#datadir = '/media/KillianDrobo/Neutral/Equipment & Laser Systems/Laser System - 532nm - Lattice/pi_log'
datadir = '.'
datefmt = '%Y.%m.%D_rydberg_verdi.txt'
fname = datadir+'/'+datetime.now().strftime(datefmt)
tempfile = 'app/most_recent.txt'
today = datetime.now()

#### Initialize the Verdi Session ####
v = verdi.Verdi(datafile = fname)

#### Write the first line of the data file ####
v.write_verdi_header()

while True:
    # asks the verdi for its data and writes it to the main data file
    # defined above (fname)
    s = v.get_verdi_data()

    # write the data to the temporary file (tempfile)

    if s != '':
        f = v.write_verdi_header(otherFile = tempfile)
        f.write(s)
        f.close()
    
    # check that it is still the same day as when you started, if not
    # make a new file
    if today.day != datetime.now().day:
        newfile = datadir+'/'+datetime.now().strftime(datefmt)
        v.datafile = newfile
        v.write_verdi_header()
        today = datetime.now()

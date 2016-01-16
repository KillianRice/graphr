import verdi

v = verdi.Verdi(datafile = 'data/data.txt')
v.write_verdi_header()
while True:
    v.get_verdi_data()

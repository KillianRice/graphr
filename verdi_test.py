import verdi

v = verdi.Verdi()

p = v.verdi_test()

if p:
    print('All tests passed')
else:
    print('One or more tests failed')

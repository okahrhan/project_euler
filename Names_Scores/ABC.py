def abc():
    girdi_dosyasi = '0022_names.txt'
    cikti_dosyasi = 'sirali_isimler.txt'
    with open(girdi_dosyasi, 'r') as dosya:
        isimler = dosya.read().strip().split(',')

    sirali_isimler = sorted(isimler)
    with open(cikti_dosyasi, 'w') as dosya:
        dosya.write(','.join(sirali_isimler))
abc()

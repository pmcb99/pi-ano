from glob import glob

fldr = '\\home\\pmb\\Downloads\\MIDI\\V'
for f in glob.glob(fldr + '*'):
    print(f)

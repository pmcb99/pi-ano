import glob
import os

dir = '/home/pmb/Downloads/MIDIS/V'

oldfiles = glob.glob(dir + '/*')

nums = list(range(1, 11))


newfiles = []
counter = 0
for line in open('/home/pmb/Downloads/MIDIS/fixedmidinames.txt', 'r'):
    line = line.rstrip("\n")
    newfiles.append('/home/pmb/Downloads/MIDIS/V/'+line)

for item in oldfiles:
    print(newfiles[counter])
    os.rename(oldfiles[counter], (newfiles[counter]))
    counter += 1

print(newfiles[counter])
os.rename(oldfiles[0], (newfiles[0]))

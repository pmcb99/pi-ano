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
x = 818
print(oldfiles[x],'\n',newfiles[x])

# for item in oldfiles:
#     print(oldfiles[9],newfiles[9])
    # os.rename(oldfiles[counter], (newfiles[counter]))
    # counter += 1

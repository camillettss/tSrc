#installer
import sys, os
import json

# setup the tsrc folder path

os.mkdir('C:/tSrcEx')
os.mkdir('C:/tSrcEx/data') #make the main directories.

srcpath='tSrc/data/'
mainpath='tSrc/help.py'

# get sources
sources={'help.py':open(mainpath).read()}

for file in os.listdir(srcpath):
    sources.update({'data/'+file:open(srcpath+file).read()})

# ora usa le keys per creare i file in C:
for key in sources:
    print(key)
    f=open('C:/tSrcEx/'+key, 'w')
    f.write(sources[key])
    f.close()

print('[*] Done')

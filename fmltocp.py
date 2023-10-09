#! /usr/bin/python3

import os
import re
import sys

expectedUser = 'ronnieperez' #user that can execute command
#expectedUser = 'root'        #user that can execute command

fileDict = {}


#check user login, exit if not expectedUser
def whoIsThis():

	if os.getlogin() != expectedUser:

		print('')
		print('   You must be logged in as',expectedUser)
		print('')

		sys.exit(1)

#get input folder from the user
def getInDir():

	while True:

		print('')
		indir = input('   Give me your folder to archive: ')

		if os.path.isdir(indir):
			break
		else:
			print('   ~~~Not a directory~~~')
	print('')

	pattern = r'/+'
	replacement = '/'

	indir = re.sub(pattern,replacement,indir)




	return indir

#get the ltfs mountpoint
def getLtfsMount():

	while True:
		print('')
		outdir = input('   Give me your LTFS mount point: ')

		if os.path.ismount(outdir):
			break
		else:
			print('   ~~~Not a mount~~~')
	print('')
	pattern = r'/+'
	replacement = '/'

	outdir = re.sub(pattern,replacement,outdir)
	return outdir

#recursively list all files
def getAllFiles(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            if os.path.isfile(file_path):
            	#print(file_path)
            	fileDict[file_path] = '1'


#Make the output destination of the outfile
def getoutf(ltfsd,inf):

	dirparts = inf.split('/')
	fname    = dirparts.pop()
	outdir   = ltfsd + '/' + '/'.join(dirparts)
	#print(inf,',',outdir,',',fname)


whoIsThis()
indir     = getInDir()
ltfsmount = getLtfsMount() 
getAllFiles(indir)
infileList = sorted(fileDict.keys())

for sourcef in infileList:
	
	outf = getoutf(ltfsmount,sourcef)






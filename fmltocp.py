#! /usr/bin/python3

import os
import sys

expectedUser = 'ronnieperez' #user that can execute command
#expectedUser = 'root'        #user that can execute command


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
	return outdir





whoIsThis()
indir     = getInDir()
ltfsmount = getLtfsMount() 




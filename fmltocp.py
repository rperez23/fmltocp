#! /usr/bin/python3

import hashlib
import os
import re
import shutil
import sys

expectedUser = 'ronnieperez' #user that can execute command
#expectedUser = 'root'        #user that can execute command

fileDict  = {}
hashDict  = {}
errorDict = {}


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

	try:
		os.makedirs(outdir,exist_ok=True)
	except FileNotFoundError as e:
		print('   Error Creating',outdir)
		sys.exit(1)
	except Exception as e:
		print('   Error Creating',outdir)
		sys.exit(1)




	return [outdir, fname]


#calc md5 of file
# Function to calculate MD5 hash of a file
def calculate_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as file:
        while chunk := file.read(8192):  # Read the file in 8KB chunks
            md5_hash.update(chunk)
    return md5_hash.hexdigest()


#md5_hash = calculate_md5(file_path)




whoIsThis()
indir     = getInDir()
ltfsmount = getLtfsMount() 
getAllFiles(indir)
infileList = sorted(fileDict.keys())

for sourcef in infileList:
	
	outfList = getoutf(ltfsmount,sourcef)
	outdir   = outfList[0]
	outfname = outfList[1]
	fulloutfname = outdir + '/' + outfname

	print(sourcef,'->',fulloutfname)

	try:
		shutil.copy(sourcef,fulloutfname)
	except shutil.Error as e:
		print('Error copying',sourcef)
	except Exception as e:
		print('Unexpected error copying',sourcef)


	#MD5 Calculation
	srcmd5 = calculate_md5(sourcef)
	dstmd5 = calculate_md5(fulloutfname)
	hashDict[sourcef] = 'srcmd5'

	if srcmd5 != dstmd5:

		errorparts = [srcmd5, dstmd5]
		errorDict[sourcef] = errorparts







	






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


whoIsThis() 



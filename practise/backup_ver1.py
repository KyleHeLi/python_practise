#!/usr/bin/python
# Filename: backup_ver1.py

import os
import time

# 1. The files and directories to be backed up are specified in a list
source = ['/home/kyle/Documents/NetworkCapture', 
'/home/kyle/Documents/python_scripts']

# 2. The backup must be stored in a main backup directory
target_dir = '/home/kyle/Documents/backup/'

# 3. The files are backed up into a zip file

# 4.1. The name of the zip archive is the current date and time
#target = target_dir + time.strftime("%Y%m%d%H%M%s") + '.zip'
# 4.2. We can use the tar command
target = target_dir + time.strftime("%Y%m%d%H%M%s") + '.tar.gz'

# 5. We use the zip command (in Unix/Linux) to put the files in a zip
# archive
#zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
tar_command = "tar -zcvf '%s' %s" % (target, ' '.join(source))

# Run the backup
if os.system(tar_command) == 0:
	#print("zip_command is"), zip_command
	print("Successful backup to"), target
else:
	print("Backup FAILED")
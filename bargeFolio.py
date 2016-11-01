import subprocess
import csv
import os

def makeFolder (ou): 
	proc=subprocess.Popen('~/gam/gam.py user portfolio@lssd.org update drivefile drivefilename "Prototype Folder2" mimetype gfolder', shell=True, stdout=subprocess.PIPE, )
	output=proc.communicate()[0]
	if "No" in output:
		print "Creating a Folder"
		proc1=subprocess.Popen('python ~/gam/gam.py user portfolio@lssd.org add drivefile drivefilename "Prototype Folder2" mimetype gfolder', shell=True, stdout=subprocess.PIPE, )
		output=proc1.communicate()[0].split()
		key = max(output, key=len)
		student='s1@lssd.org'
		bashCommand1 = "python ~/gam/gam.py user portfolio@lssd.org add drivefileacl %s user %s role writer" % (key, teacher)
		bashCommand2 = "python ~/gam/gam.py user portfolio@lssd.org add drivefileacl %s user %s role reader" % (key, student)
		os.system(bashCommand1)
		os.system(bashCommand2)
	else:
		print "Folder already created"


bashCommandQ = 'alias gam="python ~/gam/gam.py"'
os.system(bashCommandQ)
bashCommandX = 'python ~/gam/gam.py print users suspended > userEmails.csv'
os.system(bashCommandX)

#open the csv
with open('userEmails.csv', 'rb') as f:
    reader = csv.reader(f)
    print 'Lets get this party started!'
    for row in reader:
		email = row[0]
		if '@lssd.org' in email and row[1] == "False":
			bashCommandZ = 'python ~/gam/gam.py user %s update photo http://cdn.lssd.org/staff/%s.jpg' % (row[0], row[0])
#			print bashCommandZ
			os.system(bashCommandZ)			
    print 'Sync complete'

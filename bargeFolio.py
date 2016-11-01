import os
import csv
import subprocess

teacher='teacher@school.org'
portfolioAccount='portfolio@school.org'
domain='school.org'

parentFolder = '0123456789abcdefghijklmnopqr' #the id of the parent folder
ou = '/staff/or/student/org' #the OU where your students are
folderPrefix = 'Project_'  #no spaces!!

##Function that makes the folders
def makeFolder (org, parent, folderName, email): 
	proc=subprocess.Popen('~/gam/gam.py user '+portfolioAccount+' update drivefile drivefilename '+folderName+' mimetype gfolder parentid '+parent, shell=True, stdout=subprocess.PIPE, )
	output=proc.communicate()[0]
	print output
	if "No" in output:
		print "Creating a Folder"
		proc1=subprocess.Popen('python ~/gam/gam.py user '+portfolioAccount+' add drivefile drivefilename '+folderName+' mimetype gfolder parentid '+parent, shell=True, stdout=subprocess.PIPE, )
		output=proc1.communicate()[0].split()
		key = max(output, key=len)
		bashCommand1 = "python ~/gam/gam.py user %s add drivefileacl %s user %s role writer" % (portfolioAccount, key, teacher)
		bashCommand2 = "python ~/gam/gam.py user %s add drivefileacl %s user %s role reader" % (portfolioAccount, key, email)
		os.system(bashCommand1)
		os.system(bashCommand2)
	else:
		print "Folder already created"

##Make a list of users
getUsers = 'python ~/gam/gam.py print users ou suspended gal > portfolioData.csv'
os.system(getUsers)

#Loop through the list of users
with open('portfolioData.csv', 'rb') as f:
    reader = csv.reader(f)
    print 'Lets get this party started!'
    for row in reader:
		folderName = folderPrefix+email
		if domain in email and suspended == 'False' and gal == 'True':
			if org == ou                                     ##These two lines can be repeated for as many OUs
				makeFolder(tmp, art1, folderName, email)     ##as you can manage. 
	print 'Whew!'

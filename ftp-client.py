# -*- coding: utf-8 -*-

from ftplib import FTP

ftp = FTP('')
ftp.connect('IPaddress',1026) #use the IP Address you're trying to reach
ftp.login()
ftp.cwd('/home/directory') #replace with your directory
ftp.retrlines('LIST')

def uploadFile():
 filename = 'ftptest.txt' #replace with your file in your home folder
 ftp.storbinary('STOR '+filename, open(filename, 'rb'))
 ftp.quit()

def downloadFile():
 filename = 'dltest.txt' #replace with your file in the directory ('directory_name')
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

uploadFile()
downloadFile()

# -*- coding: utf-8 -*-

from ftplib import FTP

ftp = FTP('')
ftp.connect('127.0.0.1',1026) #the IP Address you're trying to reach
ftp.login()
ftp.cwd('/home') #your directory
ftp.retrlines('LIST')

def uploadFile():
 filename = 'ftptest.txt' #your file in your home folder
 ftp.storbinary('STOR '+filename, open(filename, 'rb'))
 ftp.quit()

def downloadFile():
 filename = 'dltest.txt' #your file in the directory ('directory_name')
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

uploadFile()
downloadFile()

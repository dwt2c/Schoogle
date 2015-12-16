# this is a file that should set up a ssh tunneling instance that we can use to access our database
import subprocess
import time 
import threading

class SSHTunnel(Threading.thread):
	def __init__(self,hostmachine,hostport,remotemachine,remoteport,username = '',pwrd =''):
		self.host = hostmachine + ':' + hostport
		if username != '':
			self.remotemachine = username + '@' + remotemachine + ':' + remoteport
		else:
			self.remotemachine = remotemachine + ':' + remoteport
		self.username = username
		self.pword = pwrd
		self.ispwrd = pword == ''
		self.daemon = True

	def run(self):
		if subprocess.call(['ssh','-N','-f',])

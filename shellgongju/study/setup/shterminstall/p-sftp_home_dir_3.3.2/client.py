# -*- coding:utf-8 -*-

import time
import os, sys
from sftp import  *
from common import *

class SftpClient(object):
	def __init__(self, hostname, charset='utf-8'):
		self.hostname = hostname
		self.peer = SftpPeer(handles)
		self.peer.charset = charset
		self.pid = None

	def connect(self, username, port, passwd=None, keyfile=None):
		if self.pid: self.disconnect()
		self.username = username
		self.port = port

		port = self.port 
		peer = self.peer

		p1 = os.pipe()
		p2 = os.pipe()

		peer.pid = self.pid = os.fork()
		if self.pid < 0: sys.exit(1)
		if self.pid == 0:
			os.close(p1[1])
			os.close(p2[0])
			os.dup2(p1[0], 0)
			os.dup2(p2[1], 1)
			os.close(p1[0])
			os.close(p2[1])

			args = ['qzssh', '-o', 'ChallengeResponseAuthentication=no', '-o', 'GSSAPIAuthentication=no']
			if passwd: args.extend(['--passwd', passwd])
			if keyfile: args.extend(['-i', keyfile])
			args.extend(['-l', self.username, self.hostname, '-p', str(port), '-s', 'sftp'])

			try: os.execv('/usr/bin/qzssh', args)
			except OSError: pass
			#raise SftpError('Failed exec sftp')
			os._exit(1)
		os.close(p1[0])
		os.close(p2[1])
		peer.fd1 = p1[1]
		peer.fd2 = p2[0]
		peer.ipaddr = self.hostname
		peer.user = self.username

		if not peer.handshake():
			self.disconnect()
			return
		
	def disconnect(self):
		if not self.pid: return
		self.peer.disconnect()

	def open(self, filename, flags):
		'''
		先创建文件，然后进行写模式或者读模式
		@filename: file with path
		@flags: SSH_FXF_WRITE, SSH_FXF_READ
		'''
		peer = self.peer

		#Open for create
		req = SftpRequest(SSH_FXP_OPEN, 1)
		req.flags = SSH_FXF_CREAT
		req.attr = FileAttr()
		res = peer.open(req, filename)
		self.close(res.handle)

		#Open for write or read
		req.flags = flags
		res = peer.open(req, filename)

		return res.handle

	def close(self, handle):
		peer = self.peer
		req = SftpRequest(SSH_FXP_CLOSE, handle)
		req.handle = handle

		handle_obj = handles[handle]

		return peer.close(req, handle_obj)

	def read(self, handle, offset, length):
		if not len: return 0

		peer = self.peer
		req = SftpRequest(SSH_FXP_READ, handle)
		req.offset = offset
		req.len = length

		handle_obj = handles[handle]

		res = peer.read(req, handle_obj)

		if hasattr(res, 'data'):
			return len(res.data)
		elif hasattr(res, 'message'):
			if res.message == "End of file":
				return 0

	def write(self, handle, offset, data):
		if not data: return 0

		peer = self.peer
		req = SftpRequest(SSH_FXP_WRITE, handle)
		req.offset = offset
		req.data = data

		handle_obj = handles[handle]

		res = peer.write(req, handle_obj)

		if res.message == 'Success':
			return len(data)

		return 0

	def mkdir(self, path):
		peer = self.peer
		req = SftpRequest(SSH_FXP_MKDIR, 1)
		req.attr = FileAttr()

		return peer.mkdir(req, path)

if __name__ == '__main__':
	'''
	@only for testing
	'''
	username = 'root'
	hostname = '192.168.5.201'
	port = 22
	passwd = 'shterm' 
	dir = '/root/rbcd'
	filename = '/root/aa' 

	#connect
	peer = SftpClient(hostname)
	peer.connect(username, port, passwd)

	#create dir
	res = peer.mkdir(dir)
	offset = 0
	BUFFER_SIZE = 8096

	#open for write
	f = open('test', 'rb')
	handle = peer.open(filename, SSH_FXF_WRITE)
	while True:
		length = peer.write(handle, offset, f.read(BUFFER_SIZE)) 
		offset += BUFFER_SIZE
		if length == 0: break
	peer.close(handle)

	#open for read
	handle = peer.open(filename, SSH_FXF_READ)
	while True:
		length = peer.read(handle, offset, BUFFER_SIZE) 
		offset += BUFFER_SIZE
		if length == 0: break
	f.close()

	peer.close(handle)

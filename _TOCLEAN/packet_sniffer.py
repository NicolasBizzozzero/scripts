import socket

IP = "127.0.0.0"

proto_ftp = {port:21, banner:"FTP"}
proto_ssh = {port:22, banner:"SSH"}
proto_smtp = {port:25, banner:"SMTP"}
proto_http = {port:80, banner:"HTTP"}

array_protocoles = [proto_ftp, proto_ssh, proto_smtp, proto_http]

if __name__ == "__main__":
	socket.setdefaulttimeout(2)
	sock = socket.socket()
	for protocole in array_protocoles:
		answer = None
		print("Sniffing port : " + str(protocole[port]))
		sock.connect(IP, protocole[port])
		answer = sock.recv(1024)
		print(answer)
		#try:
		#	sock.connect(IP, protocole[port])
		#	answer = sock.recv(1024)
		#except Exception e:
		#	print("Error : " + str(e))
		print(answer)

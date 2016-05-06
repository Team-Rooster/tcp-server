# Basic socket tcp server
import socket
import sys
import threading

def main(host='localhost', port=2300):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

		print(host, port)
		s.bind((host, int(port)))

		s.listen(10)

		while 1:
			client, addr = s.accept()
			print('Connection from {}'.format(addr))

			t = threading.Thread(target=handle_client, args=(client, addr))
			t.start()

def handle_client(client, addr):
	while 1:
		try:
			data = client.recv(1024)

			if (len(data) != 0):
				print('Data recv from {}: {}'.format(addr, data))

		except:
			client.close()


if __name__ == '__main__':
	main(*sys.argv[1:])
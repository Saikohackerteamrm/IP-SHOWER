import os
os.system("pip install socket")
os.system("pip install requests")
os.system("pip install colorama")
os.system("pip install time")
os.system("clear")
#_________________.
import requests
import time
import socket
import colorama
from colorama import Fore, init
import sys
#//////

init()

print ("""
\033[36m
//////////////////////////////////////////////////////////////////////////////
//     _______________    __  ___   _____       __  __    ______           //
//    /_  __/ ____/   |  /  |/  /  / ___/      / / / /   /_  __/          //
//     / / / __/ / /| | / /|_/ /   \__ \______/ /_/ /_____/ /            //
//    / / / /___/ ___ |/ /  / /   ___/ /_____/ __  /_____/ /            //
//   /_/ /_____/_/  |_/_/  /_/   /____/     /_/ /_/     /_/            //
//  Telegram  : @SHT7669            IP  Shower                        //
//  Developer : RM Rony Ali         Tools Type: FREE  Version: 0.2   //
//////////////////////////////////////////////////////////////////////

""")
print (Fore.BLUE+"""
Fuck Your System:- 

1 FOR GET IP LOCAL

2 FOR GET IP PUBLIC {Global ip}""")
print("")
print(Fore.GREEN+"")

get = input("""TYPE YOUR METHOD:-  """)

if get == "1":

        hostname = socket.gethostname()

        ip_local = socket.gethostbyname(hostname)
        print (Fore.RED+"PLEASE WAIT ...")
        time.sleep(3.0)
        print (Fore.GREEN+"Your Local IP :",Fore.RED + ip_local)
#.....$.$.$.$..$_..$.$
if get == "2":
        print (Fore.RED+"PLEASE WAIT ...")
        time.sleep(3.0)
        public = requests.get("https://api.ipify.org").text
        print("")
        print("")
        time.sleep(3)
        print (Fore.GREEN+"Your public IP :",Fore.RED + public)
else:
        print (Fore.RED+'[×]'+Fore.YELLOW+' command invalid')
        input ('Press enter for exit')
        sys.exit()
         

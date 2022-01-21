import json

import requests
from colorama import Fore
import os,time
from colorama import Fore
banner = ( Fore.GREEN +""""


,--.::::::::::::::::::::::ip::::::::::::::....:::::::
    )::::::::::::::::::ip::::::::::::::..      ..::::
  _'-. _::::::::::::::ip:::::::::::::..   ,--.   ..::
 (    ) ),--.::::::::::::::ip::::::::.   (    )   .::
             )-._::::::::::ip::::::::..   `--'   ..::
_________________)::::::::::ip:::::::::..      ..::::
:\\\\\:\\\:\:\\\::::::::::::::::::ip::::::....:::::::
::`\`\:::`::\\`\:: PLOCATER RAINING :)   ::ip::::::::
:::\\\`:_o/ :`\\`:::::::::::::::::::::ip:::::::::::::
!:!:!:!: (; !:!:!:!:!:!:!:!:!:!:!:!:ip!:!:!:!:!:!:!:!
!!!!!!!! /\ !!!!!!!!!!!!!ip!!!!!!!!!!!!!!!!!!!!!!!!!!
|!|!|!|!|!|!|!ip|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|
||||||||||||||||||||||ip|||||||||||||||||||||||||||||
I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|Iip|I|I|I|I|I|I|I|I
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIipIIIIIIIIIIIIIIIIIIII


""")
import phonenumbers
print( Fore.GREEN + """   


╔═══╗╔╗               ╔╗        
║╔═╗║║║              ╔╝╚╗       
║╚═╝║║║ ╔══╗╔══╗╔══╗ ╚╗╔╝╔══╗╔═╗
║╔══╝║║ ║╔╗║║╔═╝╚ ╗║  ║║ ║╔╗║║╔╝
║║   ║╚╗║╚╝║║╚═╗║╚╝╚╗ ║╚╗║║═╣║║ 
╚╝   ╚═╝╚══╝╚══╝╚═══╝ ╚═╝╚══╝╚╝ 
                                
----------------------------------------------------------------------------
    Tool is made by vashu tyagi                                             *
   subscribe Now ---                                                        *
    https://www.youtube.com/channel/UCFVvIu8RQnjkloRftg9T3AA                *
                                                                            *
*Tools Is only For Eductaion Purpose*                                       *
--------------------------------------------------------------------------- 
                                
       """)
print(Fore.GREEN+"Login With Victim Number to start tracing")
print(Fore.RED+"Connecting Modules")
from  phonenumbers import  geocoder
number=(input("Enter Victim Number : "))
print("Connecting Mobile")
from phonenumbers import  geocoder
ch_number = phonenumbers.parse(number,"en")
print("Country :",geocoder.description_for_number(ch_number,"en"))
##
from phonenumbers import  carrier
service = phonenumbers.parse(number,"en")
print("carrier",carrier.name_for_number(service,"en"))
##
class whois:
    def __init__(self):
        print(f"{Fore.LIGHTWHITE_EX}{banner}")
        print(f"{Fore.LIGHTGREEN_EX}Hit Enter Key':'Your ipadd' or input someone's ip")
        self.ipadd = (input(Fore.WHITE + "Input IP ~# ")).strip()

        if self.ipadd.startswith("127") or self.ipadd.startswith("192"):
            print(
                f"{Fore.RED} The Input Address is  local host",
                f"\n{Fore.RED} This is not Valid IP Address",
            )
            exit()

    def print_fetched(self):
        response = requests.get(f"http://ip-api.com/json/{self.ipadd}")
        json_response = json.loads(response.text)
        for key, value in json_response.items():
            if value:
                print(
                    Fore.LIGHTWHITE_EX
                    + f"{key.title()}: {Fore.WHITE} {str(value).strip()}"
                )


obj = whois()
obj.print_fetched()
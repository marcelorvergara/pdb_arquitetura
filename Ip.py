import threading,psutil
from tkinter import *

class Ip(threading.Thread):
    def __init__(self,frame_ip):
        super().__init__()
        interfaces = psutil.net_if_addrs()
        Label(frame_ip, text="End. IPv4: " +interfaces["enp1s0f1"][0].address, anchor='w').grid(sticky='w', row=0, column=0)
        Label(frame_ip, text="Máscara. IPv4: " +interfaces["enp1s0f1"][0].netmask, anchor='w').grid(sticky='w', row=1, column=0)
        Label(frame_ip, text="Broadcast. IPv4: " +interfaces["enp1s0f1"][0].broadcast, anchor='w').grid(sticky='w', row=2, column=0)
        Label(frame_ip, text="End. IPv6: " +interfaces["enp1s0f1"][1].address, anchor='w').grid(sticky='w', row=3, column=0)
        Label(frame_ip, text="Máscara. IPv6: " +interfaces["enp1s0f1"][1].netmask, anchor='w').grid(sticky='w', row=4, column=0)
        Label(frame_ip, text="Broadcast. IPv6: " + str(interfaces["enp1s0f1"][1].broadcast), anchor='w').grid(sticky='w', row=5, column=0)

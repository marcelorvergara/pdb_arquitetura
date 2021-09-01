import threading, platform,psutil
from tkinter import *


class Resumo(threading.Thread):
    def __init__(self,frame_resumo):
        super().__init__()
        interfaces = psutil.net_if_addrs()
        disco = psutil.disk_usage(".")
        virt_mem = psutil.virtual_memory()
        total = round(virt_mem.total / pow(2,30),1)
        Label(frame_resumo, text="Nome da máquina: " + platform.node(), anchor='w').grid(sticky='w', row=0, column=0)
        Label(frame_resumo, text="End. IPv4: " +interfaces["enp1s0f1"][0].address, anchor='w').grid(sticky='w', row=1, column=0)
        Label(frame_resumo,text="Total de disco: " + str(round(disco.total/pow(2,30),2)) + " GB", anchor='w').grid(sticky='w', row=2, column=0)
        Label(frame_resumo,text="Total de disco em uso: " + str(round(disco.used/pow(2,30),2)) + " GB", anchor='w').grid(sticky='w', row=3, column=0)
        Label(frame_resumo,text="Total de memória: " + str(total) + " GB", anchor='w').grid(sticky='w', row=4, column=0)
        Label(frame_resumo,text="Memórioa utilizada: " + str(round(virt_mem.used/pow(2,30),1)) + "GB",anchor='w').grid(sticky='w', row=5, column=0)

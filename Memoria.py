import threading
from tkinter import *
import psutil
class Memoria(threading.Thread):
    def __init__(self, frame_mem):
        super().__init__()
        virt_mem = psutil.virtual_memory()
        total = virt_mem[0]
        total = round(virt_mem.total / pow(2,30),1)
        Label(frame_mem,text="Total de memória: " + str(total) + " GB", anchor='w').grid(sticky='w', row=0, column=0)
        disponivel = round(virt_mem.available / pow(2,30),1)
        Label(frame_mem,text="Memória disponível: " + str(disponivel) + "GB",anchor='w').grid(sticky='w', row=1, column=0)
        Label(frame_mem,text="Percentual de mem. utilizado: " + str(virt_mem.percent) + "%",anchor='w').grid(sticky='w', row=2, column=0)
        Label(frame_mem,text="Memórioa utilizada: " + str(round(virt_mem.used/pow(2,30),1)) + "GB",anchor='w').grid(sticky='w', row=3, column=0)
        Label(frame_mem,text="Memórioa livre: " + str(round(virt_mem.free/pow(2,30),1)) + "GB",anchor='w').grid(sticky='w', row=4, column=0)


import time
from threading import Thread

import Cpu
from tkinter import *
from tkinter import ttk

from CpuInfos import CpuInfos
from Disco import Disco
from Memoria import Memoria
from Ip import Ip
from Resumo import Resumo

root = Tk()
root.title("Teste de Performance 3 - TP3")

notebook = ttk.Notebook(root)
notebook.grid()

frame_bars = ttk.LabelFrame(root, text='CPUs')
frame_bars.grid()
frame_bars.config(relief=RIDGE)

frame_cpu = ttk.LabelFrame(root, text='Infos')
frame_cpu.grid()

frame_mem = ttk.LabelFrame(root, text='Memória')
frame_mem.grid()

frame_disco = ttk.LabelFrame(root, text='Disco')
frame_disco.grid()

frame_ip = ttk.LabelFrame(root, text='IP')
frame_ip.grid()

frame_resumo = ttk.LabelFrame(root, text='Resumo')
frame_resumo.grid()

notebook.add(frame_bars, text='Uso de CPU')
notebook.add(frame_cpu, text='Infos CPU')
notebook.add(frame_mem, text='Infos Memória')
notebook.add(frame_disco, text='Infos Disco')
notebook.add(frame_ip, text='Infos IP')
notebook.add(frame_resumo, text='Resumo Infos')

def call_cpu_bars():
    Cpu.CpuBars(frame_bars)

cpu_infos = CpuInfos(frame_cpu)
cpu_infos.start()
mem_infos = Memoria(frame_mem)
mem_infos.start()
disco_infos = Disco(frame_disco)
disco_infos.start()
ip_infos = Ip(frame_ip)
ip_infos.start()
resumo_infos = Resumo(frame_resumo)
resumo_infos.start()

Button(frame_bars, text='Update', command=call_cpu_bars).grid(sticky='w',row=0,column=0)
root.update()
root.mainloop()

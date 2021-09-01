import threading
from tkinter import *

import cpuinfo, psutil
import platform


class CpuInfos(threading.Thread):
    def __init__(self, frame_cpu):
        super().__init__()
        Label(frame_cpu, text="Nome da máquina: " + platform.node()).grid(sticky='w', row=0, column=0)
        Label(frame_cpu, text="Marca do processador: " + cpuinfo.get_cpu_info()['vendor_id_raw']).grid(sticky='w', row=1, column=0)
        Label(frame_cpu, text="Arquitetura: " + cpuinfo.get_cpu_info()['arch_string_raw']).grid(sticky='w', row=2, column=0)
        Label(frame_cpu, text="Sistema Operacional: "+ platform.system()).grid(sticky='w',row=3,column=0)
        Label(frame_cpu, text=platform.platform()).grid(sticky='w', row=4, column=0)
        Label(frame_cpu, text="Palavra: " + str(cpuinfo.get_cpu_info()['bits']) + " bits").grid(sticky='w',row=5,column=0)
        Label(frame_cpu, text="Percentual de uso de CPU: " + str(psutil.cpu_times_percent().user) + " %").grid(sticky='w',row=6,column=0)
        Label(frame_cpu, text="Frequência máx. de CPU: " + str(psutil.cpu_freq().max) + " MHz").grid(sticky='w',row=7,column=0)
        Label(frame_cpu, text="Total de cores lógicos: " + str(psutil.cpu_count())).grid(sticky='w',row=8,column=0)
        Label(frame_cpu, text="Total de cores físicos: " + str(psutil.cpu_count(logical=False))).grid(sticky='w',row=9,column=0)

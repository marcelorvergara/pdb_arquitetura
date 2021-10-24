import threading
from tkinter import *
import psutil


class Disco(threading.Thread):
    def __init__(self, disco_frame):
        super().__init__()
        disco = psutil.disk_usage(".")
        Label(disco_frame, text="Total de disco: " + str(round(disco.total / pow(2, 30), 2)) + " GB", anchor='w').grid(
            sticky='w', row=0, column=0)
        Label(disco_frame, text="Total de disco em uso: " + str(round(disco.used / pow(2, 30), 2)) + " GB",
              anchor='w').grid(sticky='w', row=1, column=0)
        Label(disco_frame, text="Total de disco livre: " + str(round(disco.free / pow(2, 30), 2)) + " GB",
              anchor='w').grid(sticky='w', row=2, column=0)
        Label(disco_frame, text="Percentual de disco em uso: " + str(disco.percent) + " %", anchor='w').grid(sticky='w',
                                                                                                             row=3,
                                                                                                             column=0)

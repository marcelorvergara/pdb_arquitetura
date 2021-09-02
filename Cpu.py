from tkinter import DoubleVar, ttk
from tkinter.ttk import Style

import psutil
import threading


class CpuBars(threading.Thread):
    def __init__(self, frame_bars):
        super().__init__()
        cpus_proc = psutil.cpu_percent(percpu=True, interval=0.1)
        row = 1
        for p in cpus_proc:
            print(p)
            var_proc = DoubleVar()
            var_proc.set(p)
            s = Style()
            s.theme_use("default")
            s.configure("TProgressbar", background='lightgrey', thickness=10)
            ttk.Progressbar(frame_bars, variable=var_proc, style="TProgressbar", length=500).grid(row=row, column=0, columnspan=2, padx=5, pady=5)
            row += 1


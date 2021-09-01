from tkinter import DoubleVar, ttk
from tkinter.ttk import Style

import psutil,threading


class CpuBars(threading.Thread):
    def __init__(self, frame_bars, root):
        super().__init__()
        cpus_proc = psutil.cpu_percent(percpu=True, interval=0.2)
        num = 0
        row = 0
        for p in cpus_proc:
            num += 1
            var_proc = DoubleVar()
            var_proc.set(p * 5.0)
            s = Style()
            s.theme_use("default")
            s.configure("TProgressbar", background='lightgrey', thickness=10)
            ttk.Progressbar(frame_bars, variable=var_proc, style="TProgressbar", length=500).grid(row=row, column=0, columnspan=2, padx=5, pady=5)
            row += 1


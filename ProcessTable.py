import threading
import time
from tkinter import *

import psutil


def criar_titulo():
    titulo = ["PID", "# threads", "Criação", "T. Usu.", "T. Sis.", "Mem. (%)", "RSS", "VMS", "Executável"]
    return titulo


def mostra_info(pid):
    try:
        txt = []
        p = psutil.Process(pid)
        txt.append(pid)
        txt.append(p.num_threads())
        txt.append(time.ctime(p.create_time()))
        txt.append(p.cpu_times().user)
        txt.append(round(p.cpu_times().system, 2))
        txt.append(round(p.memory_percent(), 2))
        rss = round((p.memory_info().rss / (2 ** 20)), 2)
        txt.append(rss)
        vms = round((p.memory_info().vms / (2 ** 20)), 2)
        txt.append(vms)
        txt.append(p.exe())
        return txt
    except:
        pass


class ProcessTable(threading.Thread):

    def __init__(self, root):
        super().__init__()
        self.procs_window = Toplevel(root)
        self.procs_window.title('Tabela de Processos')

        self.tabela = []
        self.tabela_tit = criar_titulo()
        self.tabela.append(self.tabela_tit)

        lista_pids = psutil.pids()
        for pid in lista_pids:
            texto = mostra_info(pid)
            if texto is not None:
                self.tabela.append(texto)

        #criando a self.tabela
        total_rows = len(self.tabela)
        total_columns = len(self.tabela[0])

        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Label(self.procs_window, width=32, fg='blue', font=('Arial', 8, 'bold'))
                self.e.grid(sticky=W,row=i, column=j)
                self.e.configure(text=self.tabela[i][j])
                self.procs_window.update()
        print('terminou')

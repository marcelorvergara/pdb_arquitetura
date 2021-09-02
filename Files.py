import threading,os,time
from tkinter import *
from tkinter import ttk


class Files(threading.Thread):
    global entry

    def busca_arquivos(self,dir):
        soma = 0
        total_arq = 0
        total_dir = 0
        lista_dir = []
        lista_dir.append(dir)
        while lista_dir:
            dir_atual = lista_dir[0]
            time.sleep(0.1)
            l = []
            try:
                l = os.listdir(dir_atual)
            except:
                pass
            for i in l:
                arq = os.path.join(dir_atual, i)
                if os.path.isfile(arq):
                    soma += os.stat(arq).st_size
                    total_arq += 1
                else:
                    lista_dir.append(arq)
                    total_dir += 1
            lista_dir.remove(dir_atual)
        return soma, total_arq, total_dir

    def get_text(self):
        soma, total_arq, total_dir = self.busca_arquivos(self.entry.get())
        self.lbl_soma.configure(text='Total de bytes: ' + str(soma))
        self.lbl_tot_mb.configure(text='Total de MB: ' + str(round(soma/2**20,2)))
        self.lbl_tot_arq.configure(text='Total de arquivos: ' + str(total_arq))
        self.lbl_tot_dir.configure(text='Total de dir: ' + str(total_dir))

    def __init__(self, root):
        super().__init__()
        files_window = Toplevel(root)
        files_window.title('Arquivos e Diretórios')
        Label(files_window, text='Entre com o diretório:').pack(anchor=W,padx=5,pady=2)
        self.entry = ttk.Entry(files_window,width=30)
        self.entry.pack(padx=10,pady=5)
        Button(files_window, text='Ok', command=self.get_text).pack(anchor=E,padx=10,pady=5)
        self.soma = StringVar()
        self.total_arq = StringVar()
        self.total_dir = StringVar()
        self.lbl_soma = Label(files_window, text='Total de bytes:')
        self.lbl_soma.pack(anchor=W,padx=5,pady=2)
        self.lbl_tot_mb = Label(files_window, text='Total de MB:')
        self.lbl_tot_mb.pack(anchor=W,padx=5,pady=2)
        self.lbl_tot_arq = Label(files_window, text='Total de arquivos:')
        self.lbl_tot_arq.pack(anchor=W,padx=5,pady=2)
        self.lbl_tot_dir = Label(files_window, text='Total de dir:')
        self.lbl_tot_dir.pack(anchor=W,padx=5,pady=2)


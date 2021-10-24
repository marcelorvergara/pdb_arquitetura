import threading
from tkinter import *
import os, subprocess, platform, nmap
from tkinter.ttk import Progressbar


def retorna_codigo_ping(host):
    plataforma = platform.system()
    if plataforma == "Windows":
        args = ["ping", "-n", "1", "-1", "-w", "100", host]
    else:
        args = ["ping", "-c", "1", "-W", "1", host]
    return subprocess.call(args, stdout=open(os.devnull, "w"), stderr=open(os.devnull, "w"))


def verifica_host(base):
    host_validos = []
    for i in range(45, 57):
        if (i % 5) == 0:
            print(".", end="")
        ip = base + str(i)
        retorno = retorna_codigo_ping(ip)
        if retorno == 0:
            host_validos.append(ip)
    return host_validos


def obter_hostnames(host):
    print("host:", host)
    nm = nmap.PortScanner()
    try:
        nm.scan(host, '22-443')
        return "IP", host, " possui o nome", nm[host].hostname()
    except:
        print("Erro:", host)
        pass


def scan_host(hst):
    nm = nmap.PortScanner()
    nm.scan(hst)
    print(nm[hst].hostname())
    for proto in nm[hst].all_protocols():
        print('-----------------')
        print("Protocolo:", proto)
        lport = nm[hst][proto].keys()
        for port in lport:
            return "Porta", port, "Estado", nm[hst][proto][port]["state"]


class NetInfos(threading.Thread):

    def __init__(self, root):
        super().__init__()
        self.net_window = Toplevel(root)
        self.net_window.title('Informações sobre a rede local')
        self.ip_string = "192.168.0.6"
        self.ip_lista = self.ip_string.split(".")
        self.base_ip = ".".join(self.ip_lista[0:3]) + "."
        self.tit = Label(self.net_window, width=90, fg='blue', font=('Arial', 12, 'bold'))
        self.tit.grid(sticky=W, row=0, column=0, padx=4, pady=6)
        self.text_concat = "Testar a subrede: " + self.base_ip + "0"
        self.tit.configure(text=self.text_concat)
        self.host_validos_final = verifica_host(self.base_ip)
        self.sub_tit = Label(self.net_window, width=90, fg='blue', font=('Arial', 12, 'bold'))
        self.sub_tit.grid(sticky=W, row=1, column=0, padx=4, pady=6)
        self.text_concat_2 = "Host válidos: " + str(self.host_validos_final)
        self.sub_tit.configure(text=self.text_concat_2)
        linha = 2
        for ho in self.host_validos_final:
            self.hn = obter_hostnames(ho)
            self.hn_lbl = Label(self.net_window, width=90, fg='blue', font=('Arial', 10, 'bold'))
            self.hn_lbl.grid(sticky=W)
            self.hn_lbl.configure(text=self.hn)
            self.sh = scan_host(ho)
            linha += 1
            self.sh_lbl = Label(self.net_window, width=90, fg='blue', font=('Arial', 10, 'bold'))
            self.sh_lbl.grid(sticky=W)
            self.sh_lbl.configure(text=self.sh)
        print("Fim")


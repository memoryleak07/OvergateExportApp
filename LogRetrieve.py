import os
import json
import subprocess
import shutil
import time
from datetime import datetime
import tempfile
import ftplib


class LogRetrieve:

    data = ""
    temp = "/home/ml/Downloads/OvergateExportApp-main/"
    # temp = tempfile.TemporaryDirectory(dir=maindir)
    today = datetime.today().strftime('%Y%m%d%H%M%S')

    def __init__(self) -> None:
        try:
            with open("m.json") as jsondata:
                self.data = json.load(jsondata)
        except (ValueError, Exception) as err:
            print("[X] JSON file is not valid:", err)
            return False


    def recuperoNumeroCasse(self, numfiliale):
        casse = []
        for val in self.data["filiali"][numfiliale]["cassa"]:
            casse += val
        return casse
   
   
    def recuperoFiliali(self):
        filiali = []
        for val in self.data:
            filiali += self.data[val]
        return filiali


    def recuperoIndirizzo(self, numfiliale, numerocassa):
        ip = self.data["filiali"][numfiliale]["cassa"][numerocassa][0]
        print("Filiale numero: ", numfiliale, "|  Cassa numero: ", numerocassa, "| Indirizzo IP: ", ip)
        return ip


    def connessioneCartellaCondivisa(self, ip):
        pathtodrive = os.path.join(r"\\", ip, "c-drive")
        print("\n[+] Provo ad accedere a:", pathtodrive, "...")
        cmd = 'NET USE ' + pathtodrive + ' /User:' + "ditronpos" + ' ' + "sopnortid"
        subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        if not os.path.exists(pathtodrive):
            print("[X] Il percorso non esiste!")
            return False    
        print("[+] Il percorso esiste!")
        return True


    def dateRange(self, createddate, startdate, enddate):
        #Ritorna True se si trova nel range di date
        createddate = datetime.strptime(createddate, '%a %b %d %H:%M:%S %Y')
        startdate = datetime.strptime(startdate, '%d/%m/%Y')
        enddate = datetime.strptime(enddate, '%d/%m/%Y').replace(hour=23, minute=59, second=59)
        return startdate < createddate < enddate


    def recuperoPPOS(self, dir, ip, start, end):
        print((self, dir, ip, start, end))
        # ovgpath= os.path.join(ip+dir)
        # for filename in os.listdir(ovgpath):
        #     files = os.path.join(ovgpath+"\\"+filename)
        #     created = time.ctime(os.path.getmtime(files))
        #     if dateRange(created, start, end):
        #         try:
        #             shutil.copy2(files, temp)
        #             print("[<<] File transferred " + filename + created, " ")
        #         except (os.error, Exception) as err:
        #             print("[X] File not transferred " + filename, err)
        #     else:
        #         pass
        #         #print("[+] File not transferred " + filename + created)
        # print("[+] Task complete")


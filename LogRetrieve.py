import os
import json
import subprocess
import shutil
import time
from datetime import datetime
import tempfile
import ftplib
import threading


class LogRetrieve:

    data = ""
    tempdir = r"C:\temp"
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
        # cmd = 'NET USE ' + pathtodrive + ' /User:' + "ditronpos" + ' ' + "sopnortid"
        # subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        # LOCAL TEST:
        pathtodrive = r"C:\temp"
        if not os.path.exists(pathtodrive):
            print("[X] Il percorso non esiste!")
            return False    
        print("[+] Il percorso esiste!")
        return True


    def dateRange(self, createddate, startdate, enddate):
        #Ritorna True se si trova nel range di date
        createddate = datetime.strptime(createddate, '%a %b %d %H:%M:%S %Y')
        startdate = datetime.strptime(startdate, "%Y-%m-%d")
        enddate = datetime.strptime(enddate,"%Y-%m-%d").replace(hour=23, minute=59, second=59)
        return startdate < createddate < enddate


    def recuperoPPOS(self, dir, ip, start, end):
        #ovgpath= os.path.join(ip+dir)
        found = False
        ovgpath= os.path.join(self.tempdir + dir)
        for filename in os.listdir(ovgpath):
            files = os.path.join(ovgpath+"\\"+filename)
            created = time.ctime(os.path.getmtime(files))
            if self.dateRange(created, start, end):
                try:
                    shutil.copy2(files, self.tempdir)
                    print("File transferred " + filename + created, " ")
                    found = True
                except (os.error, Exception) as err:
                    print("File not transferred " + filename, err)
            else:
                pass
                #print("[+] File not transferred " + filename + created)
        if found:
            return True
        


    def recuperoFiles(self, dir, ip, name, ext, start, end):
        ovgpath= os.path.join(self.tempdir + dir)
        found = False
        for filename in os.listdir(ovgpath):
            files = os.path.join(ovgpath+"\\"+filename)
            created = time.ctime(os.path.getmtime(files))
            if self.dateRange(created, start, end) and filename.startswith(name) and filename.endswith(ext):
                try:
                    shutil.copy2(files, self.tempdir)
                    print("File transferred " + filename + created, " ")
                    found = True
                except (os.error, Exception) as err:
                    print("File not transferred " + filename, err)
            else:
                pass

        if found:
            return True


    # def checker(self, src, dstdir, fname):
    #     time.sleep(.01)
    #     dst = os.path.join(dstdir+"\\"+fname)
    #     print(src, dst)
    #     #Making sure the destination path exists
    #     while not os.path.exists(dst):
    #         print ("not exists")
    #         time.sleep(.01)

    #     # # Keep checking the file size till it's the same as source file
    #     while os.path.getsize(src) != os.path.getsize(dst):
    #         if os.path.getsize(src) and os.path.getsize(dst) != 0:
    #             percentage = int((float(os.path.getsize(dst))/float(os.path.getsize(src))) * 100)
    #             return percentage
    #     return 100
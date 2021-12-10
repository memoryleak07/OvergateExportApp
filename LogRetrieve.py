import os
import json
import subprocess


class LogRetrieve:

    data = ""

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

        pathtodrive = os.path.join(r"\\", ip, "c-drive")
        print("\n[+] Provo ad accedere a:", pathtodrive, "...")

        cmd = 'NET USE ' + pathtodrive + ' /User:' + "ditronpos" + ' ' + "sopnortid"
        subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

        if not os.path.exists(pathtodrive):
            print("[X] Il percorso non esiste!")
            return False
        
        print("[+] Il percorso esiste!")

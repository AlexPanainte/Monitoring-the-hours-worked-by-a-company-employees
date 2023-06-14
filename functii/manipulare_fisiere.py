import os
import time
import datetime
import shutil
import csv

#Clasa generala pentru fisiere
class Fisiere():

    #Calea catre folderul unde se inregistreaza intrarile si iesirile utilizatorilor
    path="PROIECT_Final/Intrari/"

    #Numele fisierului din folderul Intrari Ex: "Poarta1_DATA"
    nume_fisier="Poarta1_"+ str(datetime.date.today())

    #1- Functie care verifica daca au fost adaugate fisiere noi in folderul Intrari
    def verifica_fisier_noi(self):     
            oldFile=[]
            while True:
                file=os.listdir(self.path)
                if len(oldFile) == len(file):
                    print("we don't have new files")
                else:
                    for fisier_nou in file:
                        if  fisier_nou not in oldFile:
                            print(fisier_nou)
                oldFile=file                 
                time.sleep(3)

    #2-Functie care muta             
    def muta_in_backup(self):
        path=f"PROIECT_Final/Intrari/{self.nume_fisier}"
        destination="PROIECT_Final/Backup_Intrari/"
        shutil.move(path,destination)


class Fisiere_TXT(Fisiere):

    #1- Functie care creaza un fisier nou .txt care este gol sub numele de Ex:"Poarta1_DATA" 
    def scrie_txt(self):
        with open(f"{self.path}{self.nume_fisier}" ,"w") as file:  
            print("Fisierul "+ self.nume_fisier +" a fost creat")

    #2- Functie care citeste si returneaza continutul fisierelor din folderul intrari sub forma de lista de liste
    def citeste_txt(self):
        lista_continut=[]
        with open(f"{self.path}{self.nume_fisier}" ,"r") as file:
            reader=file.readlines()
            for line in reader:
                linie_split=line.split(",")
                lista_continut.append(linie_split)
            for i in lista_continut:
                print(i)

class Fisiere_CSV(Fisiere):
    
    #1 Functie care citeste fisiere CSV
    def citeste_csv(self):
        with open(f"{self.path}{self.nume_fisier}" ,"r") as file:
            reader=csv.reader(file)
            for row in reader:
                print(row)

    

fis=Fisiere_TXT()
fis.scrie_txt()   






            



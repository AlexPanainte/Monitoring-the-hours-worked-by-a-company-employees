import os
import shutil
import csv
import functii.constante as c

              
class Fisiere_TXT():

    # #2- Functie care citeste si returneaza continutul fisierelor din folderul intrari sub forma de lista de liste
    def citeste_txt(self):
        lista_continut=[]
        with open(f"{c.path}Poarta1.txt" ,"r") as file:
            reader=file.readlines()
            for line in reader:
                linie_split=line.split(",")
                lista_continut.append(linie_split)

    def move_and_rename_in_backup_TXT(self):
        os.rename(c.nume_initial_TXT,c.nume_final_TXT)
        shutil.move(c.nume_final_TXT,c.destination)


class Fisiere_CSV():
    
    #1 Functie care citeste fisiere CSV
    def citeste_csv(self):
        with open(f"{c.path}Poarta2.csv" ,"r") as file:
            reader=csv.reader(file)
            for row in reader:
                return(row)
    
    def rename_and_move_in_backup_CSV(self):
        os.rename(c.nume_initial_CSV,c.nume_final_CSV)
        shutil.move(c.nume_final_CSV,c.destination)



    


            



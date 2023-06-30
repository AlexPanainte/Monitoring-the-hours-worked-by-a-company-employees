import os
import shutil
import csv
import functii.constante as c
import mysql.connector


class Fisiere():
    def __init__(self):
        self.connect_mysql=mysql.connector.connect(host="localhost",user="root",password="Afd3ufy250137@",database="users")
        self.cursor_mysql=self.connect_mysql.cursor()


class Fisiere_TXT(Fisiere):
    
    def read_txt(self):
        lista_continut=[]

        with open(f"{c.path}Poarta1.txt" ,"r") as file:
            reader=file.readlines()
                        
            for line in reader:
                linie_strip=line.strip("\n ;")
                linie_split=linie_strip.split(",")
                lista_continut.append(linie_split)

            for i in lista_continut:
                ID=i[0]
                DATA=i[1] 
                SENS=i[2]
                self.cursor_mysql.execute(f"INSERT INTO ACCES_PORTI VALUES ('{ID}','{DATA}','{SENS}','Poarta1');")                
                self.connect_mysql.commit()
            print("Fisierul TXT a fost adaugat cu succes in baza de date")

    def move_and_rename_in_backup_TXT(self):
        os.rename(c.nume_initial_TXT,c.nume_final_TXT)
        shutil.move(c.nume_final_TXT,c.destination)
        self.cursor_mysql.close()
        self.connect_mysql.close()

class Fisiere_CSV(Fisiere):
    
    #1 Functie care citeste fisiere CSV
    def read_csv(self):
        with open(f"{c.path}Poarta2.csv","r") as file:
            fisier=csv.reader(file)
            next(fisier)
            for line in fisier:
                ID=line[0]
                DATA=line[1] 
                SENS=line[2]
                self.cursor_mysql.execute(f"INSERT INTO ACCES_PORTI VALUES ('{ID}','{DATA}','{SENS}','Poarta2');")                        
                self.connect_mysql.commit()           
            print("Fisierul CSV a fost adaugat cu succes in baza de date")
    
    def rename_and_move_in_backup_CSV(self):
        os.rename(c.nume_initial_CSV,c.nume_final_CSV)
        shutil.move(c.nume_final_CSV,c.destination)

        self.cursor_mysql.close()
        self.connect_mysql.close()

    


            



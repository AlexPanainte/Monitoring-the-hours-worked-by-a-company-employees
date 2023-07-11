import os
import shutil
import csv
import functii.constante as c
import mysql.connector

class Fisiere():
    #Se defineste conexiunea cu baza de date
    #Define database connection
    def __init__(self):
        self.connect_mysql=mysql.connector.connect(host="localhost",user="root",password="Afd3ufy250137@",database="users")
        self.cursor_mysql=self.connect_mysql.cursor()

class Fisiere_TXT(Fisiere):
   
    def read_txt(self):

    # 1.Se defineste o lista goala pe numele content_list
    # 2.Se deschide fisierul Poarta1.txt introdus in folderul Intrari,se itereaza si se formateaza continutul  si se adauga in lista content_list
    # 3.Se intereaza prin continutul listei content_list se creaza variabile cu ID DATA SI SENS apoi se introduc in baza de date

        content_list=[]
        with open(f"{c.path}Poarta1.txt" ,"r") as file:
            reader=file.readlines()
                        
            for line in reader:
                line_strip=line.strip("\n ;")
                line_split=line_strip.split(",")
                content_list.append(line_split)

            for content in content_list:
                ID=content[0]
                DATA=content[1] 
                SENS=content[2]
                self.cursor_mysql.execute(f"INSERT INTO ACCES_PORTI VALUES ('{ID}','{DATA}','{SENS}','Poarta1');")                
                self.connect_mysql.commit()
            print("TXT file successfully added to the database")

    def move_and_rename_in_backup_TXT(self):

    # 1.Se redenumeste fisierul POARTA1.txt din folderul INTRARI,adaugandu-se data zilei in care a fost procesat
    # 2.Fisierul redenumit este mutat in fisierul BACKUP_INTRARI

        try:
            os.rename(c.nume_initial_TXT,c.nume_final_TXT)
            shutil.move(c.nume_final_TXT,c.destination)
            self.cursor_mysql.close()
            self.connect_mysql.close()
        except shutil.Error:
            print("This file already exists")

class Fisiere_CSV(Fisiere):
    
    def read_csv(self):
        
    # 1.Se deschide fisierul Poarta2.csv introdus in folderul Intrari
    # 2.Se intereaza prin continutul fisierului  se creaza variabile cu ID DATA SI SENS apoi se introduc in baza de date

        with open(f"{c.path}Poarta2.csv","r") as file:
            fisier=csv.reader(file)
            next(fisier)
            for line in fisier:
                ID=line[0]
                DATA=line[1] 
                SENS=line[2]
                self.cursor_mysql.execute(f"INSERT INTO ACCES_PORTI VALUES ('{ID}','{DATA}','{SENS}','Poarta2');")                        
                self.connect_mysql.commit()           
            print("CSV file successfully added to the database")
    
    def rename_and_move_in_backup_CSV(self):

    # 1.Se redenumeste fisierul POARTA1.txt din folderul INTRARI,adaugandu-se data zilei in care a fost procesat
    # 2.Fisierul redenumit este mutat in fisierul BACKUP_INTRARI

        try:
            os.rename(c.nume_initial_CSV,c.nume_final_CSV)
            shutil.move(c.nume_final_CSV,c.destination)

            self.cursor_mysql.close()
            self.connect_mysql.close()
        except shutil.Error:
            print("This file already exists")

    


            



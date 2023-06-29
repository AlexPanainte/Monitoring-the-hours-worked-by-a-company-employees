import os
import csv

import schedule
import time
from datetime import datetime

import functii.constante as c
import functii.file as f
import functii.users as u

import mysql.connector
connect=mysql.connector.connect(host="localhost",user="root",password="Afd3ufy250137@",database="users")
cursor=connect.cursor()


def calcul_ore():
        cursor.execute("SELECT * FROM users.ore_lucrate ORDER BY ID_PERSOANA")
        rows = cursor.fetchall()
        index = []
        angajat_cu_mai_putin_de_8ore_lucrate = []

        for i in rows:
            if i[0] not in index:
                index.append(i[0])

        for id in index:
            ID = id
            intrari = []
            iesiri = []

            for i in rows:
                if i[2] == 'in' and i[0] == ID:
                    intrari.append(i[1])
                elif i[2] == 'out' and i[0] == ID:
                    iesiri.append(i[1])

            if len(intrari) != len(iesiri):
                raise ValueError("Numărul de intrări și ieșiri trebuie să fie același.")

            numar_ore = 0
            numar_minute = 0

            for intrare, iesire in zip(intrari, iesiri):
                try:
                    intrare = datetime.strptime(intrare, '%Y-%m-%dT%H:%M:%S.%fZ')
                    iesire = datetime.strptime(iesire, '%Y-%m-%dT%H:%M:%S.%fZ')

                    diferenta = iesire - intrare
                    diferenta_totala_secunde = diferenta.total_seconds()
                    diferenta_ore = int(diferenta_totala_secunde) // 3600
                    diferenta_minute = int(diferenta_totala_secunde % 3600) // 60

                    numar_ore += diferenta_ore
                    numar_minute += diferenta_minute
                except ValueError:
                    print("Formatul datelor de intrare sau ieșire este incorect.")
            
            total_minute = numar_ore * 60 + numar_minute
            if total_minute < 480:  # 8 ore reprezintă 480 de minute
                angajat = {'ID': ID, 'Ore': numar_ore, 'Minute': numar_minute}
                angajat_cu_mai_putin_de_8ore_lucrate.append(angajat)
            else:
                print(f"Timpul total de lucru pentru angajatul cu ID-ul {ID} este {numar_ore} ore și {numar_minute} minute.")
        
        if angajat_cu_mai_putin_de_8ore_lucrate:
            user=u.User()
            user.send_email(angajat_cu_mai_putin_de_8ore_lucrate)
        # cursor.execute("Truncate ore_lucrate")
           

def verifica_fisier_noi():
    schedule.every().day.at('17:52').do(calcul_ore)     
    old_files = []


    while True:
        files = os.listdir(c.path)
        if len(old_files) != len(files):
            for new_files in files:  
                #Citeste si introduce in baza de date ACCES_POARTA1 Continutul fisierelor Poarta1.txt
                if new_files =="Poarta1.txt":
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
                            cursor.execute(f"INSERT INTO ACCES_POARTA1 VALUES ('{ID}','{DATA}','{SENS}');")
                            cursor.execute(f"INSERT INTO ORE_LUCRATE VALUES ('{ID}','{DATA}','{SENS}','Poarta1');")
                            connect.commit()
                        print("Fisierul TXT a fost adaugat cu succes in baza de date")
                #Se adauga data curenta la fisierelu Poarta1.txt si este mutat in folderul BACKUP_INTRARI
                    fTXT=f.Fisiere_TXT()
                    fTXT.move_and_rename_in_backup_TXT()

                #Citeste si introduce in baza de date ACCES_POARTA1 Continutul fisierelor Poarta.csv    
                if new_files == "Poarta2.csv":
                    with open(f"{c.path}Poarta2.csv","r") as file:
                        fisier=csv.reader(file)
                        next(fisier)

                        for line in fisier:
                            ID=line[0]
                            DATA=line[1] 
                            SENS=line[2]
                            cursor.execute(f"INSERT INTO ACCES_POARTA2 VALUES ('{ID}','{DATA}','{SENS}');")
                            cursor.execute(f"INSERT INTO ORE_LUCRATE VALUES ('{ID}','{DATA}','{SENS}','Poarta2');")
                            connect.commit()            
                        print("Fisierul CSV a fost adaugat cu succes in baza de date")
                #Se adauga data curenta la fisierelu Poarta1.txt si este mutat in folderul BACKUP_INTRARI
                    fCSV=f.Fisiere_CSV()
                    fCSV.rename_and_move_in_backup_CSV()

            # Actualizează lista de fișiere inițiale
            old_files = files    
        else:
            print("Nu există fișiere noi.")
        schedule.run_pending()    
        time.sleep(3)
        
          
verifica_fisier_noi()

connect.close()
cursor.close()


    





    



















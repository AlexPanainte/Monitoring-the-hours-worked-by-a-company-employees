import os

import schedule
import time

import functii.constante as c
import functii.file as f
import functii.users as u

def verifica_fisier_noi():
    users=u.User()       
    schedule.every().day.at('11:27').do(users.calcul_ore)
    users.calcul_ore()   

    old_files = []
    while True:
        files = os.listdir(c.path)
        if len(old_files) != len(files):
            for new_files in files:  
                #Citeste si introduce in baza de date ACCES_Porti Continutul fisierului Poarta1.txt
                if new_files =="Poarta1.txt":
                    txt_file=f.Fisiere_TXT()
                    txt_file.read_txt()
                    txt_file.move_and_rename_in_backup_TXT()

                #Citeste si introduce in baza de date ACCES_PORTI Continutul fisierelor Poarta.csv    
                if new_files == "Poarta2.csv":
                    csv_file=f.Fisiere_CSV()
                    csv_file.read_csv()
                    csv_file.rename_and_move_in_backup_CSV()
            # Actualizează lista de fișiere inițiale
            old_files = files    
        else:
            print("Nu există fișiere noi.")

        schedule.run_pending()    
        time.sleep(3)

verifica_fisier_noi()   


          





    





    



















import os
import subprocess
import threading

import schedule
import time

import functii.constante as c
import functii.file as f
import functii.users as u

def main():
    users=u.User()       
    schedule.every().day.at('20:00').do(users.calcul_ore)
       
    old_files = []
    while True:
        files = os.listdir(c.path)
        if len(old_files) != len(files):
            for new_files in files:  
                
                if new_files =="Poarta1.txt":
                    txt_file=f.Fisiere_TXT()
                    txt_file.read_txt()
                    txt_file.move_and_rename_in_backup_TXT()

               
                if new_files == "Poarta2.csv":
                    csv_file=f.Fisiere_CSV()
                    csv_file.read_csv()
                    csv_file.rename_and_move_in_backup_CSV()
            
            old_files = files    
        else:
            print("Nu există fișiere noi.")

        schedule.run_pending()    
        time.sleep(3)

def server():
        subprocess.Popen(["python", "D:\phyton\PROIECT_FINAL\server.py"], bufsize=-1)


t1 = threading.Thread(target=server)
t2 = threading.Thread(target=main)
t1.start()
t2.start()



          





    





    



















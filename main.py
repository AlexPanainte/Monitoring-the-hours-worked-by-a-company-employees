import functii.manipulare_fisiere as fisiere
import functii.manipulare_utilizatori as user
import mysql.connector
import datetime
connect=mysql.connector.connect(host="localhost",user="root",password="Afd3ufy250137@",database="users")
cursor=connect.cursor()

utilizator=user.User()
file=fisiere.Fisiere_TXT()
path="PROIECT_Final/Intrari/"
nume_fisier="Poarta1_"+ str(datetime.date.today())



def muta_in_acces_poarta1():

        lista_continut=[]
        with open(f"{path}{nume_fisier}" ,"r") as file:
            reader=file.readlines()
            for line in reader:
                linie_split=line.split(",")
                lista_continut.append(linie_split)
            for i in lista_continut:
                ID=i[0]
                DATA=i[1]
                SENS=i[2]
                cursor.execute(f"INSERT INTO ACCES_POARTA1 VALUES ('{ID}','{DATA}','{SENS}');")
                connect.commit()
                print("Intrare inregistrata")


# Aici am un bug care inloc sa imi inregistreze intrarile si iesirile imi creaza prima data un fisier nou de fiecare data 
# in fisierul manipulare utilizator unde este functia scrisa merge corect 

# utilizator.inregistrare_intrari_Poarta1(1)
# utilizator.inregistrare_iesiri_Poarta1(1)


def poarta1():
    # 1-citeste fisierul Poarta1.txt si il returneaza / aceasta functie nu este neaprat necesara aici
    file.citeste_txt()
    #2 -Citeste fisierul Poarta1.txt si adauga toate intrarile utilizatorilor in baza de date acces
    muta_in_acces_poarta1()
    #3 -Dupa ce au fost adaugate fisierele din Poarta1.txt fisierul este mutat in folderul Backup
    file.muta_in_backup()
    #4 -Dupa mutarea fisierului din ziua respectiva se creaza un nou fisier cu data din ziua urmatoare
    file.scrie_txt()
poarta1()

     
connect.close()
cursor.close()








    



















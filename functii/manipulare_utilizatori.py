import mysql.connector
import datetime

connect=mysql.connector.connect(host="localhost",user="root",password="Afd3ufy250137@",database="users")
cursor=connect.cursor()

class User():
    path="PROIECT_Final/Intrari/"
    nume_fisier="Poarta1_"+ str(datetime.date.today())
    #1-Functie care inregistreaza utilizatori in baza de date registered_users
    def user_registration(self,nume,prenume,nume_companie,id_manager):

        self.nume=nume
        self.prenume=prenume
        self.nume_companie=nume_companie
        self.id_manager=id_manager
        cursor.execute(f"INSERT INTO REGISTERED_USERS VALUES (null,'{self.nume}','{self.prenume}','{self.nume_companie}','{self.id_manager}');")
        connect.commit()
        print("Utilizator inregistrat")

    #2- Functie care arata toti utilizatorii inregistrati in baza de date registered_users
    def show_users(self):

        select_users="SELECT * FROM REGISTERED_USERS;"
        cursor.execute(select_users)
        user=cursor.fetchall()
        for list in user:
            print(list)

    #3- Functie care inregistreaza intrarea pe Poarta1.txt a utilizatorilor in functie de ID 
    def inregistrare_intrari_Poarta1(self,ID_ANGAJAT):

        timp=datetime.datetime.now()
        intrare=(f"{str(ID_ANGAJAT)},{str(timp)},in"+"\n")
        with open(f"PROIECT_FINAL/Intrari/{self.nume_fisier}","a") as file:
                file.write(intrare)
                print("Acces permis")

    #4- Functie care inregistreaza intrarea pe Poarta1.txt a utilizatorilor in functie de ID 
    def inregistrare_iesiri_Poarta1(self,ID_ANGAJAT):

        timp=datetime.datetime.now()
        intrare=(f"{str(ID_ANGAJAT)},{str(timp)},out"+"\n")
        with open(f"PROIECT_FINAL/Intrari/{self.nume_fisier}","a") as file:
                file.write(intrare)
                print("Acces permis")
   
    #5- Functie care citeste fisierul Poarta1.txt si muta continutul acestuia in baza de date acces_poarta1
    def muta_in_acces_poarta1(self):

        lista_continut=[]
        with open(f"{self.path}{self.nume_fisier}" ,"r") as file:
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
                print("Intrare inregistrat")
    

    
        
a=User()
a.inregistrare_intrari_Poarta1(2)
a.inregistrare_iesiri_Poarta1(1)



connect.close()
cursor.close()


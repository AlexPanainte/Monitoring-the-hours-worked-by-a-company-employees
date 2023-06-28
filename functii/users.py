import mysql.connector
import datetime

connect=mysql.connector.connect(host="localhost",user="root",password="Afd3ufy250137@",database="users")
cursor=connect.cursor()

path="PROIECT_Final/Intrari/"
nume_fisier="Poarta1_"+ str(datetime.date.today())

class User():
   
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

    def calcul_ore(self):
        cursor.execute("SELECT * FROM users.ore_lucrate order by ID_PERSOANA")
        rows=cursor.fetchall()
        index=[]
        for i in rows:
            if i[0] not in index:
                index.append(i[0])

        for id in index:
            ID=id
            intrari=[]
            iesiri=[]

            for i in rows:
                if i[2]=='in' and i[0]==ID:      
                    intrari.append(i[1])
            for i in rows:
                if i[2]=='out' and i[0]==ID:      
                    iesiri.append(i[1])

            if len(intrari) != len(iesiri):
                raise ValueError("Numărul de intrări și ieșiri trebuie să fie același.")

            numar_ore = 0
            numar_minute = 0

            for intrare, iesire in zip(intrari, iesiri):
                try:
                    intrare = datetime.strptime(intrare, '%Y-%m-%dT%H:%M:%S.%fZ')
                    iesire = datetime.strptime(iesire, '%Y-%m-%dT%H:%M:%S.%fZ')
                    diferență = iesire - intrare
                    diferență_totală_secunde = diferență.total_seconds()
                    diferență_ore = int(diferență_totală_secunde) // 3600
                    diferență_minute = int(diferență_totală_secunde % 3600) // 60

                    numar_ore += diferență_ore
                    numar_minute += diferență_minute
                except ValueError:
                    print("Formatul datelor de intrare sau ieșire este incorect.")

            print (f"Timpul total de lucru pentru angajatul cu ID-UL:{ID} este {(numar_ore)} ore si {numar_minute} minute ")

            # functiie de trimis email
            cursor.execute("TRUNCATE ORE_LUCRATE;")


connect.close()
cursor.close()


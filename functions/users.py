import mysql.connector
import smtplib, ssl
from email.message import EmailMessage
from datetime import datetime
import functions.constante as c




class User():
    def __init__(self):
        self.connect=mysql.connector.connect(host="localhost",user="root",password="Afd3ufy250137@",database="users")
        self.cursor=self.connect.cursor()
        
    def send_email(self,angajati):
        sender_mail = "alexvasluigaming@gmail.com"
        email_password = c.password
        email_reciever = c.email
        
        subject = "SALUT"
        body = "Următorii angajați nu au lucrat 8 ore:\n\n"
        for angajat in angajati:
            body += f"ID: {angajat['ID']}, Ore: {angajat['Ore']}, Minute: {angajat['Minute']}, De recuperat: {angajat['Recuperare']}\n"

        em = EmailMessage()
        em['From'] = sender_mail
        em['To'] = email_reciever
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_mail, email_password)
            server.send_message(em)
            server.quit()
        print("Email Sent")

    def calcul_ore(self):
        self.cursor.execute("SELECT * FROM users.acces_porti  WHERE CAST(users.acces_porti.data as date) = curdate() ORDER BY ID_PERSOANA")
        rows = self.cursor.fetchall()
        index = []
        angajat_cu_mai_putin_de_8ore_lucrate = []

        for angajat in rows:
            if angajat[0] not in index:
                index.append(angajat[0])

        for id in index:
            ID = id
            intrari = []
            iesiri = []

            for persoana in rows:
                if persoana[2] == 'in' and persoana[0] == ID:
                    intrari.append(persoana[1])
                elif persoana[2] == 'out' and persoana[0] == ID:
                    iesiri.append(persoana[1])

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
                ore_ramase = (480 - total_minute) // 60
                minute_ramase = (480 - total_minute) % 60

                angajat = {
                    'ID': ID,
                    'Ore': numar_ore,
                    'Minute': numar_minute,
                    'Recuperare': f"{ore_ramase} ore și {minute_ramase} minute"
                }
                angajat_cu_mai_putin_de_8ore_lucrate.append(angajat)
                print(f"Timpul total de lucru pentru angajatul cu ID-ul {ID} este {numar_ore} ore și {numar_minute} minute.")
            else:
                print(f"Timpul total de lucru pentru angajatul cu ID-ul {ID} este {numar_ore} ore și {numar_minute} minute.")
            
        if angajat_cu_mai_putin_de_8ore_lucrate:
            user=User()
            user.send_email(angajat_cu_mai_putin_de_8ore_lucrate)
        
        self.connect.close()
        self.cursor.close()


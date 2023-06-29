import mysql.connector
import smtplib, ssl
from email.message import EmailMessage

connect=mysql.connector.connect(host="localhost",user="root",password="Afd3ufy250137@",database="users")
cursor=connect.cursor()


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
    def send_email(self,angajati):
        sender_mail = "alexvasluigaming@gmail.com"
        email_password = "hdlkekhytlzipsqq"
        email_reciever = "dragosarama595@gmail.com"

        subject = "SALUT"
        body = "Următorii angajați nu au lucrat 8 ore:\n\n"
        for angajat in angajati:
            body += f"ID: {angajat['ID']}, Ore: {angajat['Ore']}, Minute: {angajat['Minute']}\n"

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

    



connect.close()
cursor.close()


import mysql.connector
import datetime
try:
    connect=mysql.connector.connect(host="localhost",user="root",password="Afd3ufy250137@",database="users")
    cursor=connect.cursor()
    print("Connected to SQL")
except Exception as error:
    print(error)

class SQL_info():

    def user_registration(self):
        lista_angajati=[]
        print("USER REGISTRATION")
        NUME=input("Adaugati numele:")
        PRENUME=input("Adaugati prenumele:")
        NUME_COMPANIE=input("Adaugati numele companiei:")
        ID_MANAGER=int(input("Adaugati ID_Manager:"))

        cursor.execute(f"INSERT INTO REGISTERED_USERS VALUES(null,'{NUME}','{PRENUME}','{NUME_COMPANIE}','{ID_MANAGER}');")
        connect.commit()

    def show_users(self):
        select_users="SELECT * FROM REGISTERED_USERS"
        cursor.execute(select_users)
        user=cursor.fetchall()
        for list in user:
            print(list)
sql=SQL_info()
# sql.user_registration()
sql.show_users()

# def poarta1():
#     select_users="SELECT * FROM REGISTERED_USERS"
#     cursor.execute(select_users)
#     user=cursor.fetchall()
#     for list in user:
#         print(list[0])

    
    




#inchid cursor si conexiune
connect.close()
cursor.close()






data_ora_curenta = datetime.datetime.now()







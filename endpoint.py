from flask import Flask,request
import mysql.connector



app = Flask(__name__)
connect=mysql.connector.connect(host="localhost",user="root",password="Afd3ufy250137@",database="users")
cursor=connect.cursor()

@app.route("/")
def home():
    return("Hello world ")

@app.route("/trecere",methods=["POST"]) #create

def trecere():
    data=request.get_json()
    ID=data["idPersoana"]
    DATA=(data["data"])
    SENS=(data["sens"])
    POARTA=(data["idPoarta"])
    
    intare=f"INSERT INTO USERS.ACCES_PORTI values ('{ID}','{DATA}','{SENS}','{POARTA}');"
    print(intare)
    cursor.execute(intare)
    connect.commit()
    return "Trecere inregistrata cu succes"


@app.route("/register", methods=["POST"])
def inregistrare():
    data = request.get_json()
    nume = data["nume"]
    prenume = data["prenume"]
    nume_companie = data["nume_companie"]
    id_manager = data["id_manager"]

    inregistrare=(f"INSERT INTO REGISTERED_USERS VALUES (null,'{nume}','{prenume}','{nume_companie}','{id_manager}');")
    print(inregistrare)

    cursor.execute(inregistrare)
    connect.commit()

    return("Utilizator inregistrat")


if __name__ == '__main__':
    app.run(debug=True)

cursor.close()
connect.close()



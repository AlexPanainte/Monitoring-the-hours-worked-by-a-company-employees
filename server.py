from flask import Flask,request,render_template
import mysql.connector



app = Flask(__name__)
connect=mysql.connector.connect(host="localhost",user="root",password="Afd3ufy250137@",database="users")
cursor=connect.cursor()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/formular")
def meniu():
    return render_template("formular.html")


@app.route("/trecere",methods=["POST"])

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


@app.route("/register", methods=["POST","GET"])
def inregistrare():

    if request.method=="POST":
        
        nume = request.form["nume"]
        prenume = request.form["prenume"]
        nume_companie = request.form["nume_companie"]
        id_manager = request.form["id_manager"]

        inregistrare=(f"INSERT INTO REGISTERED_USERS VALUES (null,'{nume}','{prenume}','{nume_companie}','{id_manager}');")
        cursor.execute(inregistrare)
        connect.commit()

        persoana=nume +" "+ prenume

    return render_template('formular.html',utilizator=persoana)

@app.route("/users",methods=["POST","GET"])
def users():

    select_users="SELECT * FROM REGISTERED_USERS;"
    cursor.execute(select_users)
    lista_angajati=cursor.fetchall()

    return render_template('lista_angajati.html',angajati=lista_angajati)


if __name__ == '__main__':
    app.run(debug=True)

cursor.close()
connect.close()



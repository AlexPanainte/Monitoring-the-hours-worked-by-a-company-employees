from flask import Flask,request
import mysql.connector



app = Flask(__name__)
connect=mysql.connector.connect(host="localhost",user="root",password="Afd3ufy250137@",database="users")
cursor=connect.cursor()

@app.route("/")
def home():
    return("Hello world from curs27")

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


if __name__ == '__main__':
    app.run(debug=True)

cursor.close()
connect.close()



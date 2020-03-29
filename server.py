from flask import Flask, jsonify, request
app = Flask(__name__)
import sqlite3
import random
import time
import datetime


@app.route('/')
def hello():
    return "Hello World!"

@app.route("/sehirler")
def add_city():
    con = sqlite3.connect("bolgeler.db")
    cursor = con.cursor()

    bolge = request.args.get("bolge")
    sehir = request.args.get("sehir")
    cursor.execute("INSERT INTO Places_to_Visit VALUES(?,?)",(bolge, sehir))
    con.commit()
    con.close()

    return jsonify({sehir})

@app.route('/bolgeler')
def get_bolgeler():
    con = sqlite3.connect("bolgeler.db")


    cursor = con.cursor()

    cursor.execute("SELECT * from Places_to_Visit")
    rows = cursor.fetchall()

    result = []
    for item in rows:
        result.append({"bolge":item[0],"sehir":item[1]})
    con.commit()
    con.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
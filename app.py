from flask import Flask, Response, url_for, render_template, request, jsonify
import json
import pymysql
app = Flask(__name__, static_folder = "/")
# app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/aboutUs")
def aboutUs():
    return render_template("About-us.html")

@app.route("/finding")
def finding():
    #  資料庫連結 ＱＵＥＲＹ出來
    return render_template("finding.html")

@app.route("/passdata")
def find():
    db = pymysql.connect(host="localhost", user= "root", password = "", database = "missthing")
    cursor = db.cursor()
    sql_select = "SELECT * FROM `item` WHERE 1"
    cursor.execute(sql_select) 
    variable_1 = cursor.fetchall()
    # print(variable_1[0])
    # for i in variable_1:
    #     print(i)
    db.commit()
    db.close()
    return jsonify(variable_1)

@app.route("/publish")
def publish():
    return render_template("publish.html")

@app.route("/search",methods=["POST"])
def search():
    keyword = request.form.get("keyword")
    db = pymysql.connect(host="localhost", user= "root", password = "", database = "missthing")
    cursor = db.cursor()
    sql_select = "SELECT * FROM `item` WHERE 1"
    cursor.execute(sql_select) 
    variable_1 = cursor.fetchall()
    db.commit()
    db.close()
    result = []
    for item in variable_1:
        for i in range(1,6):
            if not item[i].find(keyword)==-1 :
                result.append(item)
                break
    temp = ""
    for item in result:
        for i in range(1,6):
            temp += item[i]+"-"
    if not len(result)  == 0:
        return temp
    else:
        return "搜尋不到!"

@app.route("/form", methods = ["POST"])
def form():
    item = request.form.get("item")
    location = request.form.get("location")
    location2 = request.form.get("location2")
    name = request.form.get("name")
    studentID = request.form.get("studentID")
    number = request.form.get("number")
        
    
    db = pymysql.connect(host="localhost", user= "root", password = "", database = "missthing")
    cursor = db.cursor()
    sql_insert = "INSERT INTO item(`item_name`,`pick_loc`,`picker_name`,`picker_phone`,`picker_stID`,`put_loc`)\
    VALUES('%s','%s','%s','%s','%s','%s')"\
        %(item,location,location2,name,studentID,number)
    cursor.execute(sql_insert)
    db.commit()
    db.close()
    
    return render_template("suc_upload.html")
    #return render_template("publish.html")
    # mysql connection
    # sql 語法存入

# @app.route("/index")
# def index():
#     return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8090, debug = True)
from flask import Flask,request,jsonify
from flask_cors import CORS
import mysql.connector

app=Flask(__name__)
CORS(app)

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password="1234",
    database='student'
)
cursor=conn.cursor()

@app.route('/stdinfoo',methods=['POST'])
def add_std():
    data=request.json
    id=data['id']
    name=data['name']
    email=data['email']
    age=data['age']
    gender=data['gender']
    phno=data['phno']
    dept=data['dept']
    cgpa=data['cgpa']
    cursor.execute("insert into stdinfoo(id,name,email,age,gender,phno,dept,cgpa) values (%s,%s,%s,%s,%s,%s,%s,%s)",(id,name,email,age,gender,phno,dept,cgpa))
    conn.commit()
    return jsonify({"message":"added succesfully"}),201

@app.route('/stdinfoo/<int:id>',methods=['GET'])
def get_std_byid(id):
    cursor.execute('select * from stdinfoo where id =%s',(id,))
    student=cursor.fetchone()
    if student:
        return jsonify(student)
    return jsonify({"message":"user not found"}),404
@app.route('/stdinfoo/<int:id>',methods=['PUT'])
def update_std(id):
    data=request.json
    
    name=data['name']
    email=data['email']
    age=data['age']
    gender=data['gender']
    phno=data['phno']
    dept=data['dept']
    cgpa=data['cgpa']
    cursor.execute("update stdinfoo set name=%s,email=%s,age=%s,gender=%s,phno=%s,dept=%s,cgpa=%s where id =%s",(name,email,age,gender,phno,dept,cgpa,id))
    conn.commit()
    return jsonify({"message":"updated succesfully"})
@app.route('/stdinfoo/<int:id>',methods=['DELETE'])
def delete_std(id):
    cursor.execute('delete from stdinfoo where id = %s',(id,))
    conn.commit()
    return jsonify({"message":"deleted successfully"})

@app.route('/stdinfoo',methods=['GET'])
def get_std_g():
    dept=request.args.get('dept')
    

    gender=request.args.get('gender')
    if gender:
        cursor.execute('select * from stdinfoo where gender=%s',(gender,))
    elif dept:
        cursor.execute('select * from stdinfoo where dept=%s',(dept,) )
    else:
        cursor.execute('select*from stdinfoo')
    student=cursor.fetchall()
    return jsonify(student)
app.run(debug=True,port=5001)


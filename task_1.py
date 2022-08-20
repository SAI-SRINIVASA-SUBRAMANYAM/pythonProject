from flask import Flask, request, jsonify
from mysql.connector import connect

app = Flask(__name__)

#create table if not exists employes (id int, name varchar(100), age int);
#create database if not exists ineuron;

@app.route('/add_employee/mysql', methods=['POST'])
def add_employee_mysql ():
    id = int(request.json['id'])
    name = request.json['name']
    age = int(request.json['age'])

    try:
        con = connect(host="localhost", user="root", password="root", database="ineuron")
        cur = con.cursor()
        cur.execute('insert into employes (id, name, age) values (%s, %s, %s)', (id, name, age))
        con.commit()
        con.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify({"message": "successfully inserted data"})

@app.route('/update_employee/mysql', methods=['POST'])
def update_employee_mysql ():
    id = int(request.json['id'])
    name = request.json['name']
    age = int(request.json['age'])
    try:
        con = connect(host="localhost", user="root", password="root", database="ineuron")
        cur = con.cursor()
        cur.execute('update employes set name = %s, age = %s where id = %s', (name, age, id))
        if cur.rowcount == 0:
            raise Exception(f"Unable update an employe with id: {id}")
        con.commit()
        con.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify({"message": "successfully updated data"})


@app.route('/delete_employee/mysql', methods=['POST'])
def delete_employee_mysql ():
    id = int(request.json['id'])
    try:
        con = connect(host="localhost", user="root", password="root", database="ineuron")
        cur = con.cursor()
        cur.execute('delete from employes where id = %s', (id, ))
        if cur.rowcount == 0:
            raise Exception(f"Unable delete an employe with id: {id}")
        con.commit()
        con.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify({"message": "successfully deleted data"})

@app.route('/get_employees/mysql', methods=['GET'])
def get_employees():
    data = dict()
    try:
        con = connect(host="localhost", user="root", password="root", database="ineuron")
        cur = con.cursor(dictionary=True)
        cur.execute('select * from employes')
        # if cur.rowcount == 0:
        #     raise Exception(f"No data found at table employe table")
        data = cur.fetchall()
        con.commit()
        con.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)


if __name__ == '__main__':
    app.run()

from flask import Flask, request, jsonify
from mysql.connector import connect
import os


app = Flask(__name__)

@app.route('/get_summary')
def read_file():
    file_name = request.args.get('file_name')
    try:
        file_path = r'E:\ml-dataset\AUG-22\Week3\Day2'
        file_path = file_path + '\\'+file_name
        if not os.path.exists(file_path):
            return jsonify({"error": f"File '{file_path}', not found" })
        data = []
        with open(file_path) as fp:
            data = fp.readlines()
        return jsonify(data)
    except Exception as e:
        return jsonify(str(e))

@app.route('/test_args')
def test_req_args():
    first_name = request.args.get('fname')
    last_name = request.args.get('lname')
    return jsonify(f"Hello {last_name}, {first_name}")

@app.route('/get_data')
def get_data_from():
    db = request.args.get('db')
    tn = request.args.get('tn')
    try:
        con = connect(host="localhost", user="root", password="root", database=db)
        cur = con.cursor(dictionary=True)
        cur.execute(f'select * from {tn}')
        data = cur.fetchall()
        con.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=9008)

from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

@app.route('/add_employee/mongo', methods=['POST'])
def add_employee_mongo ():
    id = int(request.json['id'])
    name = request.json['name']
    age = int(request.json['age'])
    response = ""
    try:
        uname = "vasu"
        password = "your_password"
        cluster = "cluster0"
        url = f"mongodb+srv://{uname}:{password}@{cluster}.34cpv.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(url)
        database = client['my_database']
        collection = database['employee']
        response = collection.insert_one({"id": id, "name": name, "age": age})
    except Exception as e:
        return jsonify(str(e))
    return jsonify(f"Inserted successfully with id: {response.inserted_id}")

@app.route('/update_employee/mongo', methods=['POST'])
def update_employee_mongo ():
    id = int(request.json['id'])
    name = request.json['name']
    age = int(request.json['age'])
    response = ""
    try:
        uname = "vasu"
        password = "your_password"
        cluster = "cluster0"
        url = f"mongodb+srv://{uname}:{password}@{cluster}.34cpv.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(url)
        database = client['my_database']
        collection = database['employee']
        response = collection.find_one_and_update({"id": id}, {'$set': {"name": name, "age": age}}, return_document=pymongo.ReturnDocument.AFTER)
    except Exception as e:
        return jsonify(str(e))
    return jsonify(f"Updated successfully with id: {str(response)}")

@app.route('/delete_employee/mongo', methods=['DELETE'])
def delete_employee_mongo ():
    id = int(request.json['id'])
    response = ""
    try:
        uname = "vasu"
        password = "your_password"
        cluster = "cluster0"
        url = f"mongodb+srv://{uname}:{password}@{cluster}.34cpv.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(url)
        database = client['my_database']
        collection = database['employee']
        response = collection.delete_many({"id": id})
    except Exception as e:
        return jsonify(str(e))
    return jsonify(f"Deleted successfully with id: {str(response)}")

@app.route('/get_employees/mongo', methods=['GET'])
def get_employee_mongo ():
    response = []
    try:
        uname = "vasu"
        password = "your_password"
        cluster = "cluster0"
        url = f"mongodb+srv://{uname}:{password}@{cluster}.34cpv.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(url)
        database = client['my_database']
        collection = database['employee']
        employees = list(collection.find({}, {"id": 1, "name": 1, "age": 1}))
        for e in employees:
            response.append({"id": e.get("id"), "name": e.get("name"), "age": e.get("age")})
    except Exception as e:
        return jsonify(str(e))
    return response

if __name__ == '__main__':
    app.run()
from database import readyDatabase, insertOne, updateOne, removeOne, findOne, findAll
from flask import Flask, url_for, request, json, jsonify

app = Flask(__name__)

@app.route('/')
def api_root():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Wrong-End Point'

@app.route('/articles', methods = ['GET', 'POST'])
def api_articles():
    if request.method == 'GET':
        return jsonify(findAll()) 
    elif request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            isInserted = insertOne(request.json['title'], request.json['content'])
            if isInserted == True:
                resp = {'success': True, 'msg': 'Data Inserted Into Database.'}
                return jsonify(resp)
            else:
                print(isInserted)
                resp = {'success': False, 'msg': 'Insert Error'}
                return jsonify(resp)

@app.route('/articles/<id>', methods = ['GET', 'PUT', 'DELETE'])
def api_article(id):
    if request.method == 'GET':
        if request.headers['Content-Type'] == 'application/json':
            data = json.dumps(request.json)
            # return findOne()

    elif request.method == 'PUT':
        if request.header['Content-Type'] == 'application/json':
            pass
            # return updateOne()

    elif request.method == 'DELETE':
        if request.header['Content-Type'] == 'application/json':
            pass
            # return removeOne()

if __name__ == '__main__':
    readyDatabase()
    app.run()
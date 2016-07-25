

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(host='ec2-54-173-3-167.compute-1.amazonaws.com')

mobileDB = client.get_database('mobile')

users = mobileDB.get_collection('users')



@app.route('/')
def home():
    return '<h1>Halla</h1>'

@app.route('/<name>')
def user(name):
    user = users.find({'name':name})

    return user.next()['mobile']

if __name__ == '__main__':
    app.run(debug=True,port=8181)

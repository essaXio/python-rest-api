

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(host='ec2-54-173-3-167.compute-1.amazonaws.com')

mobileDB = client.get_database('mobile')

users = mobileDB.get_collection('users')

myname = 'Essa'

# Hi this is the new changes


@app.route('/hi/<name>')
def test(name):
    myname = 'Ali'
    myname = 'Mohammed'
    
    return "<h1>Hi, "+name+"</h1>"


@app.route('/')
def home():
    return '<h1>Halla</h1>'

@app.route('/users/<name>')
def user(name):
    user = users.find_one({'name':name})
    if user:
        return user['mobile']
    else:
        return "Sorry"   

if __name__ == '__main__':
    app.run(debug=True,port=8181)


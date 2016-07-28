

from flask import Flask, request
from pymongo import MongoClient


app = Flask(__name__)

<<<<<<< HEAD
client = MongoClient(host='localhost')
=======
client = MongoClient(host='localhost')
>>>>>>> 6d3a6f19522c3cf7074aadbdb2026016e06615d8

mobileDB = client.get_database('mobile')

users = mobileDB.get_collection('users')


# Hi this is the new changes


@app.route('/hi/<name>')
def test(name=None):
    myname = 'Ali'
    myname = 'Mohammed'
    
    return "<h1>Hi, "+name+"</h1>"

@app.route('/hi/')
def noneHi():
    return test()

@app.route("/json", methods=['POST'])
def json():
    
    #app.logger.debug("JSON received...")
    #app.logger.debug(request.json)
    
    
    if request.get_json():
        mydata = request.get_json() # will be 
        users.insert({'name':mydata.get("name"), 'mobile':mydata.get("mobile")})
        return "Thank"

    else:
        return "no json received"

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


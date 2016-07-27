

from flask import Flask, request
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient(host='ec2-54-173-3-167.compute-1.amazonaws.com')

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


from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT , jwt_required
from security import authenticate,identity
from user import UserRegister
app = Flask(__name__)
app.secret_key = 'rajat'

#to add resources
api = Api(app)

jwt = JWT(app , authenticate , identity) #/auth , we send a username and passowrd ten jwt sends it

items = []


#which inherits from resource class , copy of resource class not exact
#this is resource
class Item(Resource):
    @jwt_required()
    def get(self,name):
        item = next(filter(lambda x : x['name'] == name , items),None) #if filter doesnt find any match it returns None
        return {'item' : item}, 200 if item  else 404




    def post(self,name):
        if next(filter(lambda x : x['name'] == name , items),None) is not None :
            return {'message': "An item with name '{}' already exists".format(name)},400 #bad request




        data = request.get_json()#to get json fields , payload

        item = {'name': name,'price': data['price']}
        items.append(item)
        return item, 201

#    def delete(self,name) :
#	global items
       # items = list(filter(lambda x : x['name']!= name , items))
       # return {'message': 'deleted'}


class Item_list(Resource):
    def get(self):
        return {'items':items}


#thsi api can access this resource now
api.add_resource(Item, '/Item/<string:name>') #http://127.0.0.1:5000/student/Rolf
api.add_resource(Item_list, '/Items')
api.add_resource(UserRegister, '/register')
app.run(port=5000 , debug =True)

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
app = Flask(__name__)
api = Api(app)
app.secret_key = "soroush"
jwt = JWT(app, authenticate, identity)
items = []

class Item(Resource):
    @jwt_required()
    def get(self,name):
        item = next(filter(lambda item: item["name"]== name , items), None)
        return {"item":item} ,200 if item else 404

    def post(self, name):
        if next(filter(lambda item: item["name"]== name , items), None):
            return {"message":"Item exists already"}, 400
        request_data = request.get_json()
        items.append({"name":name , "price":request_data["price"]})
        return {"name":name , "price" :request_data["price"]}, 201
    def delete(self,name):
        # for item in items:
        #     if item["name"] == name :
        #         items.remove(item)
        #         return({"message": "the item '{}' was deleted" .format(name)})
        # return({"message":"Item does not exist."})
        global items
        items = list(filter(lambda item: item["name"] != name , items))
        return({"message": "The '{}' item was deleted." .format(name)})
    def put(self, name):
        request_data = request.get_json()
        # for item in items:
        #     if item["name"] == name :
        #         item["price"] = request_data["price"]
        #         return({"message":"The item '{}' was updated." .format(name)})
        # items.append({"name":name, "price":request_data["price"]})
        # return({"message": "The item '{}' was added." .format(name)})
        item = next(filter(lambda item: item["name"] == name , items), None)
        if item is None:
            item = {"name": name , "price": request_data["price"]}
            items.append(item)
        else :
            item.update(request_data)
        return item

class Items(Resource):
    def get(self):
        return {"items":items}
api.add_resource(Item , '/item/<string:name>')
api.add_resource(Items , '/items')
app.run( port = 5000, debug = True )

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self,name):
        # for item in items:
        #     if item["name"]== name :
        #         return(jsonify(item))
        # return(list(filter(lambda item: item["name"]== name , items)))
        chosen_items = [item for item in items if item["name"] == name]
        if chosen_items == []:
            return({"message":"item not found"}), 404
        else:
            return chosen_items[0], 200

    def post(self, name):
        items.append({"name":name , "price":12})
        return {"name":name , "price" :12}, 201

class Items(Resource):
    def get(self):
        return {"items":items}


api.add_resource(Item , '/item/<string:name>')

api.add_resource(Items , '/items')

app.run( port = 5000 )

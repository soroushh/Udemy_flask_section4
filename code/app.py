from flask import Flask, request, jsonify
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self,name):
        item = next(filter(lambda item: item["name"]== name , items), None)
        return {"item":item} ,200 if item else 404

    def post(self, name):
        if next(filter(lambda item: item["name"]== name , items), None):
            return {"message":"Item exists already"}, 400
        request_data = request.get_json()
        items.append({"name":name , "price":request_data["price"]})
        return {"name":name , "price" :request_data["price"]}, 201

class Items(Resource):
    def get(self):
        return {"items":items}


api.add_resource(Item , '/item/<string:name>')

api.add_resource(Items , '/items')

app.run( port = 5000 )

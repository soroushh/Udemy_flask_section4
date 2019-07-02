from flask import Flask, request, jsonify
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)

class Student(Resource):
    students = []
    def get(self,name):
        return {'student':name}
    def post(self):
        data = request.get_json()
        self.students.append({"name":data["name"]})
        return(jsonify({"student":self.students}))


api.add_resource(Student , '/student/<string:name>', '/student')

app.run( port = 5000 )

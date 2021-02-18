# pip install Flask Flask-Restful
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

class CodeList(Resource):
    def get(self):
        pass

class Code(Resource):
    def get(self, code):
        pass

class Price(Resource):
    def get(self, code):
        pass

class OrderList(Resource):
    def get(self):
        pass

api.add_resource(CodeList, "/codes", endpoint="codes")
api.add_resource(Code, "/codes/<string:code>", endpoint="code")
api.add_resource(Price, "/codes/<string:code>/price", endpoint="price")
api.add_resource(OrderList, "/orders", endpoint="orders")

if __name__ == '__main__':
    app.run(debug=True)
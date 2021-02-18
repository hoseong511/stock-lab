# pip install Flask Flask-Restful
from flask import Flask
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
import datetime
from stocklab.db_handler.mongodb_handler import MongoDBHandler

app = Flask(__name__)
CORS(app)
api = Api(app)

code_hname_to_eng = {
    "안축코드": "code",
    "확장코드": "extend_code",
    "종목명": "name",
    "시장구분": "marke",
    "ETF구분": "is_etf",
    "주문수량단위": "memedan",
    "기업인수목적회사여부":"is_spac"
}

code_field = {
    "code": fields.String,
    "extend_code": fields.String,
    "name": fields.String,
    "memedan": fields.Integer,
    "market": fields.String,
    "is_etf": fields.String,
    "is_spac": fields.String,
    "uri": fields.Url("code")
}

code_list_short_fields = {
    "code": fields.String,
    "name": fields.String
}

code_list_fields = {
    "count": fields.Integer,
    "code_list": fields.List(fields.Nested(code_field)),
    "uri": fields.Url("code")
}

mongodb = MongoDBHandler()

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
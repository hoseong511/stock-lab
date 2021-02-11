import unittest, inspect
from stocklab.db_handler.mongodb_handler import MongoDBHandler
from pprint import pprint
import pymongo

class MongoDBHandlerTestCase(unittest.TestCase):

    def setUp(self):
        self.mongodb = MongoDBHandler()
        self.mongodb._client["stocklab_test"]["corp_info"].drop()
        docs =[
            { "item": "SamSung SDS", "related": "SamSung", "qty": 25,
                "tags": ["blank", "red"], "account": [ 14, 21] },
            {"item": "LG CNS", "related": "LG", "qty": 50,
             "tags": ["red", "blank"], "account": [14, 21]},
            {"item": "SK Telecom", "related": "SK", "qty": 100,
             "tags": ["red", "blank"], "account": [14, 21]},
            {"item": "HYUNDAI MOBIS", "related": "HYNDAI", "qty": 75,
             "tags": ["blank", "red"], "account": [22.85, 30]},
            {"item": "SamSung SDI", "related": "SamSung", "qty": 25,
             "tags": ["blank", "red"], "account": [14, 21]},
            {"item": "LG Telecom", "related": "LG", "qty": 50,
             "tags": ["red", "blank"], "account": [14, 21]},
            {"item": "SK Innovation", "related": "SK", "qty": 50,
             "tags": ["red", "blank"], "account": [14, 21]},
        ]
        self.mongodb._client["stocklab_test"]["corp_info"].insert_many(docs)

    def test_insert_item(self):

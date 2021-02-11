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
        print(inspect.stack()[0][3])
        doc = { "item": "SamSung Card", "related": "SamSung", "qty": 25,
               "tags": ["green", "red"], "account": [10, 11] }
        _id = self.mongodb.insert_item(doc, "stocklab_test", "corp_info")
        assert _id
        print(_id)

    def test_insert_items(self):
        print(inspect.stack()[0][3])
        docs = [ {"item": "LG", "related": "LG", "qty": 25, "tags": ["red"], "account": [14, 21]},
                 {"item": "LG 화학", "related": "LG", "qty": 25, "tags": ["green", "red"], "account": [14, 21]}
        ]
        ids = self.mongodb.insrt_items(docs, "stocklab_test", "corp_info")
        assert ids
        print(ids)

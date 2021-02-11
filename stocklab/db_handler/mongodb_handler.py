from pymongo import MongoClient
from pymongo.cursor import CursorType
import configparser

class MongoDBHandler:
    def __init__(self):
        """
        MongoDBHandler __init__
        config.ini 파일에서 MongoDB 접속 정보를 로딩함.
        접속정보를 이용해 MongoDB 젒고에 사용할 _client를 생성
        """
        config = configparser.ConfigParser()
        config.read('conf/config.ini')
        host = config['MONGODB']['host']
        port = config['MONGODB']['port']

        self._client = MongoClient(host, int(port))

    def insert_item(self, data, db_name=None, collection_name=None):
        """
        MongoDB에 하나의 문서(document)를 입력하기 위한 메서드다.
        :param data: dict 문서를 받는다.
        :param db_name: str Mong
        :param collection_name:
        :return:
        """
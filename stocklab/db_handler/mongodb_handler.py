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
        :param db_name: str MongoDB에서 데이터베이스에 해당하는 이름을 받습니다.
        :param collection_name: str 데이터베이스에 속하는 컬렉션 이름을 받습니다.
        :return:str 입력 완료된 문서의 ObjectId를 반환합니다.
        :raises Exception: 매개변수 db_name과 collection_name이 없으면 예외(Exception)를 발생시킵니다.
        """
        if not isinstance(data, dict):
            raise Exception("data type should be dict")
        if db_name is None or collection_name is None:
            raise Exception("Need to param db_name, collection_name")
        return self._client[db_name][collection_name].insert_one(data).inserted_id

    def insert_items(self, datas, db_name=None, collection_name=None):
        """
        MongoDB에 여러 개의 문서(document)를 입력하기 위한 메서드이다.
        :param datas: list 문서의 리스트를 받는다.
        :param db_name: str MongoDB에서 데이터베이스에 해당하는 이름을 받는다
        :param collection_name: str 데이터베이스에 속하는 컬렉션 이름을 받는다.
        :return: 입력 완료된 문서의 ObjectId list를 반환
        :raise Exception: 매개변수 db_name과 collection_name 이 없으면 예외(Exception)를 발생시킨
        """
        if not isinstance(datas, list):
            raise Exception("datas type should be list")
        if db_name is None or collection_name is None:
            raise Exception("Need to param db_name, collection_name")
        return self._client[db_name][collection_name].insert_many(datas).inserted_ids

    def find_item(self, conditon=None, db_name=None, collection_name=None):
        """
        하나의 문서(document)를 검색하기 위한 메서드
        :param conditon: dict 검색 조건을 딕셔너리 형태로 받는다.
        :param db_name: 데이터베이스에 해당하는 이름을 받는다.
        :param collection_name: 컬렉션 이름을 받는다.
        :return: 검색된 문서가 있으면 문서의 내용을 반환
        :raise Exception: 매개변수 db_name과 collection_name이 없으면 예외를 발생
        """
        if conditon is None or not isinstance(conditon, dict):
            condition = {}
        if db_name is None or collection_name is None:
            raise Exception("Need to param db_name, collection_name")
        return self._client[db_name][collection_name].find_one(condition)

    def find_items(self, condition=None, db_name=None, collection_name=None):
        """
        여려 개의 문서(document)를 검색하기 위한 메서드
        :param condition: dict 검색 조건을 딕셔너리 형태로 받는다
        :param db_name: str 데이터베이스에 해당하는 이름을 받는다.
        :param collection_name: str 데이터베이스에 컬렉션 이름을 받는다.
        :return: 커서를 반환
        :raises Exception: 매개변수 db_name과 collection_name이 없으면 예외를 발생
        """
        if condition is None or not isinstance(condition, dict):
            condition ={}
        if db_name is None or collection_name is None:
            raise Exception("Need to param db_name, collection_name")
        return self._client[db_name][collection_name].find(condition, no_cursor_timeout=True, cursor_type=CursorType.EXHAUST)

    def delete_items(self, condition=None, db_name=None, collection_name=None):
        """
        여러 개의 문서를 삭제하기 위한 메서드
        :param condition:
        :param db_name:
        :param collection_name:
        :return:
        """
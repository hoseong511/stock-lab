## MongoDB
MongoDB의 명령어 연습    
insert, update, find, delete
```
use stocklab # DB 접속   
show collections # 콜렉션 검색 -> sql로 하면 테이블인듯함.
db.price_info.insertOne({"code":"1", "name":"SAMSUNG","price":123,"time":new Timestamp()}) #insertOne 테스트   
db.price_info.insertMany([{"code": "2", "name": "LG", "price":234, "time" : new Timestamp() } , {"code":"3", "name": "SK", "price": 345, "time" : new Timestamp() } ]) # insertMany 테스트   
db.price_info.find() # 전체 조회(select)
db.price_info.find({price:{$gt:300}}) # price의 값이 300보다 큰 문서를 찾는 경우
db.price_info.find({code:"1"}) # code의 값이 "1"인 문서를 찾는 경우
db.price_info.finde({ price: { $in: [ 123, 345 ] } }, {_id :0} ) # price의 값이 123이나 345인 문서를 찾고, _id 필드는 출력하지 않는 경우

```
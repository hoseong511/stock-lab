## MongoDB
MongoDB의 명령어 연습    
insert, update, find, delete
```
use stocklab # DB 접속   
show collections # 콜렉션 검색 -> sql에서의 테이블인듯함.

db.price_info.insertOne({"code":"1", "name":"SAMSUNG","price":123,"time":new Timestamp()}) #insertOne 테스트   
db.price_info.insertMany([{"code": "2", "name": "LG", "price":234, "time" : new Timestamp() } , {"code":"3", "name": "SK", "price": 345, "time" : new Timestamp() } ]) # insertMany 테스트
   
db.price_info.find() # 전체 조회(select)
db.price_info.find({price:{$gt:300}}) # price의 값이 300보다 큰 문서를 찾는 경우
db.price_info.find({code:"1"}) # code의 값이 "1"인 문서를 찾는 경우
db.price_info.find({ price: { $in: [ 123, 345 ] } }, {_id :0} ) # price의 값이 123이나 345인 문서를 찾고, _id 필드는 출력하지 않는 경우

db.price_info.updateOne({code:"2"}, {$set:{price:456}}) # code가 "2"인 문서의 price 필드의 값을 456으로 변경
db.price_info.updateMany({$or: [ {code:"2"}, {code:"3"} ]}, { $set : {price: 111 } }) # code가 "2"나 "3 인 모든 문서의 price 필드 값을 111로 업데이트

db.price_info.deleteOne( { code: "3" } ) # code가 3인 문서 1개를 삭제
db.price_info.deleteMany( { "price": 111 } ) # price가 123인 문서 여러 개를 삭제

```
```
db.corp_info.insertMany([
    { item: "SamSung SDS", related:"SamSung", qty: 25, tags: ["blank", "red"], accout: [14, 21]},
    { item: "LG CNS", related:"LG", qty: 50, tags: ["red", "blank"], accout: [14, 21]},
    { item: "SK Telecom", related:"SK", qty: 100, tags: ["red", "blank", "plain"], accout: [14, 21]},
    { item: "HYUNDAI MOBIS", related:"HYUNDAI", qty: 75, tags: ["blank", "red"], accout: [22.85, 30]},
    { item: "SamSung SDI", related:"SamSung", qty: 25, tags: ["blank", "red"], accout: [14, 21]},
    { item: "LG Telecom", related:"LG", qty: 50, tags: ["red", "blank"], accout: [14, 21]},
    { item: "SK Innovation", related:"SK", qty: 50, tags: ["red", "blank"], accout: [14, 21]}
    ]}
db.corp_info.find({ tags: ["red", "blank"] })
db.corp_info.find({ tags: "red" })
db.corp_info.find({ account: {$gt: 15, $lt: 20}})
db.corp_info.find({ account: {
    

```
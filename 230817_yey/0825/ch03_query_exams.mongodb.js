//전체 실행 단축키 : ctrl + alt + r
//문장 실행 단축키 : ctrl + alt + s

use("car_accident");
//_id -> 기본값이고(별개), 따로 설정 없으면 무조건 보이고, 따로 flase 또는 (=0)
//"교차로내.accident_count" 하나 보여주고, 나머지 전부 다 안볼거예요.
db.by_road_type.find(
    {county:"강릉시"},
    {"교차로내.accident_count":1}
);

db.by_road_type.find(
    {county:"강릉시"}
);


use("car_accident");
// 하나 문서의 갯수를 구하는 함수 예제
db.by_road_type.countDocuments(
    {county:"강릉시"}
);

use("car_accident");
db.by_road_type.find(
    {"기타단일로.death_toll":0},
    {_id:false, city_or_province:true, county:1} //보고 싶은 열
);

use("car_accident");
db.by_road_type.find(
    {"횡단보도부근.death_toll":0},
    {_id:false, city_or_province:true, county:1} //보고 싶은 열
)

use("car_accident");
db.inventory.insertMany([ 
    { item: "journal", qty: 25, tags: ["blank", "red"] }, 
    { item: "notebook", qty: 50, tags: ["red", "blank"] }, 
    { item: "paper", qty: 100, tags: ["white"]}, 
    { item: "planner", qty: 75, tags: ["blank", "red"] }, 
    { item: "postcard", qty: 45, tags: ["blue"] } 
]);

use("car_accident");
db.inventory.find();

//문법
// db.inventory.find(
//     {  <filter> : { <operator> : <value> }      }
//       )
use("car_accident");
db.inventory.find({ item: { $eq: "journal" } });
use("car_accident");
db.inventory.find({ item: "journal" });
// in
db.inventory.find({ tags: { $in: ["red"] } });
use("car_accident");
db.inventory.countDocuments(
    {tags : {$in:["red"]}}
);


// $regex 연산자
// {<field> : { $regex : /pattern/, $options : '<options>'}}
// {<field> : { $regex : 'pattern', $options : '<options>'}}
// {<field> : { $regex : /pattern/<options>}}

//시작은 알파벳으로 시작이고 갯수 0문자 이상, 끝나는 문자 d로 끝나는 문자열 검색
use("car_accident");
db.inventory.find({ tags: { $in: [/^[a-z]*d/] } });
db.inventory.find({ tags: { $in: [/^b/] } });
db.inventory.find({ tags: { $in: [/^g/] } });
use("car_accident");
db.inventory.find({ item: /^p/i });
//nin
db.inventory.find({ tags: { $nin: ["blank", "blue"] } }); //없음
db.inventory.find({ tags: { $nin: ["blank"] } }); //1개
// gt, lte - 초과 / 이하
use("car_accident");
db.inventory.find({ qty: { $not: { $gt: 50 } } });
db.inventory.find({ qty: { $lte: 50 } });
//수량 구하기.
use("car_accident");
db.inventory.countDocuments({ qty: { $lte: 50 } });
//논리 연산자
use("car_accident");
db.inventory.find({ $or: [{ qty: { $gt: 90 } }, { qty: { $lt: 50 } }] });
db.inventory.find({ $and: [{ qty: { $gt: 50 } }, { qty: { $lt: 90 } }] });
db.inventory.find({ qty: { $gt: 50, $lt: 90 } });
// tags에 red가 들어간 도큐먼트 전부 출력
db.inventory.find({ tags: "red" });
// tags가 "red", "blank" 둘 다 주어진 순서대로 가진 도큐먼트 전부 출력
use("car_accident");
db.inventory.find({ tags: ["red", "blank"] });
use("car_accident");
db.inventory.find({ tags: ["blank", "red"] });
// 순서 확인 위해서, blank, red 부분 삭제하고 다시 조회
use("car_accident");
db.inventory.deleteOne({item: "notebook"});
//원래대로 복구
use("car_accident");
db.inventory.insertOne([ 
    { item: "notebook", qty: 50, tags: ["red", "blank"] }
]);
use("car_accident");
db.inventory.find()


//실습3
//insertMany({요소1}, {요소2}, {요소3})
use("car_accident");
db.stores.insertMany([
    // _id 생략시, ObjectID 자동 생성
    // id : 1, 값을 명시, 그 값으로 생성됨. 
    // 주의사항 -> 유니크 부분이 잘 지켜지는지. 여부
  { _id: 1, name: "Java Hut", description: "Coffee and cakes" },
  { _id: 2, name: "Burger Buns", description: "Gourmet hamburgers" },
  { _id: 3, name: "Coffee Shop", description: "Just coffee" },
  { _id: 4, name: "Clothes Clothes Clothes", description: "Discount clothing" },
  { _id: 5, name: "Java Shopping", description: "Indonesian goods" },
]);
use("car_accident");
db.stores.find()

//Text index -> 4장 인덱스
// 인데스 부분, 검색시 속도를 향상 시키기 위한 기법.
// 보통 기본 PK에 대해서 인덱스 설정이 기본으로 됨.
// 주의 사항) 복합키 인뎃스 설정을 할 때, 너무 많은 조건을 설정하게 되면,
// 조건을 맞추는 자원 소모가 더 큼
// 검색을 하는 자원 소모보다, 조건을 맞추는 부분이 더 힘들어짐.
// 결과 -> 성능이 떨어짐. -> 튜닝 부분이 어려움.
// 기본 인덱스 이용하되, 만약 복합키를 사용한다면, 2개~3개정도 사용하되.
// 꼭 확인 후 설정 적용하길 권장
// b-tree 구조(자료구조) 
db.stores.createIndex({ name: "text", description: "text" });
//$text Operation -> 문자열 검색
db.stores.find({ $text: { $search: "java coffee shop" } });
db.stores.find({ $text: { $search: "shopping" } });
//exact Phrase : 정확하게 일치하는 문서 찾기
db.stores.find({ $text: { $search: '"coffee shop"' } });
// Term Exclustion : "-"연산자를 사용하여 검색에 제외할 텀을 지정
db.stores.find({ $text: { $search: "java shop -coffee" } });
db.stores.find({ $text: { $search: "java -shop -coffee" } });
db.stores.find({ $text: { $search: "java -shop" } });
db.stores.find({ $text: { $search: "Gourmet" } });

// ******* 
db.stores
  .find(
    { $text: { $search: "java coffee shop" } },
    //$meta 연산자를 사용하는 score 필드를 포함. 이 필드에는 각 문서의 텍스트 검색 점수가 보관됩니다.
    { score: { $meta: "textScore" } }
    //score 필드(텍스트 검색 점수)를 기준으로 내림차순으로 결과를 정렬
  )
  .sort({ score: { $meta: "textScore" } });

//  $all 순서와 상관없이 있으면 선택
//  $elemMatch 조건과 맞는 배열 속 요소를 가진 것을 선택
//  $size 해당 배열의 크기와 같은 것 선택
db.inventory.find({ tags: { $gt: 10, $lt: 5 } });
db.inventory.find({ tags: { $elemMatch: { $gt: 50, $lt: 80 } } });
db.by_month.find({
  $and: [
    { month_data: { $elemMatch: { month: "01월", heavy_injury: 0 } } },
    { month_data: { $elemMatch: { month: "02월", death_toll: 0 } } },
  ],
});
//$size
db.inventory.find({ tags: { $size: 3 } }); //배열 lenth가 3인 문서
//  프로젝션 연산자의 역할
// 특정 필드만 가져옴
// $slice : 배열 필드에 주어진 범위 $elemMatch 배열 필드의 조건에 맞는 것만
// $ 첫번째 요소만
use("car_accident");
db.people.insertMany([
  { name: { first: "철수", last: "김" } },
  { name: { first: "영희", last: "김" } },
  { name: { first: "수영", last: "박" } },
  { name: { first: "희영", last: "이" } },
]);
db.people.insertOne({ name: { first: "철수", last: "김" } });
db.people.deleteOne({ "name.first": "철수" });
db.people.find({}, { "name.first": 1 });
// {item: "book", tags: ["red", "blank"]}
// 잘못됨. tags의 첫번째 인자[0]가 아니라 tags 배열의 0이란 원소를 출력하라는 의미
db.inventory.find({}, { "tags.0": 1 });
// tags 배열의 [0], [1]을 출력하라 (앞에서 부터 2개를 출력하라)
db.inventory.find({}, { tags: { $slice: 2 } });
// tags 배열의 [2:3] 을 출력하라, 끝자리 미포함,
db.inventory.find({}, { tags: { $slice: [1, 3] } });
// $elemMatch
//  $ 연산자
// #특정 조건에 부합하는 필드만 출력하라
db.inventory.find({}, { tags: { $elemMatch: { $regex: /^b/ } } });
//#특정 조건에 부합하는 첫번째 데이터만 출력하라
// 방금 검색한 필드의 값중 "red"를 갖는 도큐먼트를 찾음.
db.inventory.find({ tags: "red" }, { _id: false, item: false, qty: false });
//tags.$ : 먼저 검색한 결과를 기준으로 검색.
db.inventory.find({ tags: "red" }, { "tags.$": true });


// $or: [{death_toll : 0}, {heavy_injury :0}]
db.by_road_type.find({ $or:[{"교량위치.accident_count": 0},
                            {"터널안.death_toll" : 0}]},
                      {_id:false, city_or_province:true, county:true });









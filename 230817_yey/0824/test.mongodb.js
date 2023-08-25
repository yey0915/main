
use("testDB");

db.createCollection("cappedC", {capped:true, size: 1000});

use("testDB");
db.cappedC.insertOne({x:1});

//전체 조회
use("test")
db.cappedC.find();

//상태 조회
use("test");
db.cappedC.stats();

//반복문, 여러 데이터 입력해서, 전체 용량을 초과시키고
//오래된 데이터가 삭제되는 부분 확인하고, 넘어가기.
use("test");
for(i=0; i<1000; i++){
    db.cappedC.insertOne({x:i});
}

use("test");

//프로젝션 확인, -> 보고 싶은 열을 선택하는 옵션
//db.users.find({<쿼리(where)>}, {<프로젝션(=보고 싶은 컬럼)>});


db.test.find(
    //_id, false 아닐 경우를 제외하고 항상 표시
    //"_id" : false 의미, 이거 빼고 다 보여주세요.
    // _id : false
    // id  항상 표시
    

);











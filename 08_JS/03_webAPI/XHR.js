const DOMAIN = 'https://jsonplaceholder.typicode.com/';
const RESOURCE = 'posts/';
const QUERY_STRING = '';

const URL = DOMAIN + RESOURCE + QUERY_STRING;

// req 대리인 XHR 객체 생성
const XHR = new XMLHttpRequest();
XHR.open('POST', URL);

// 보내는 데이터의 정보
XHR.setRequestHeader(
    'Content-type',
    'application/json;charset=UTF-8'
);

// XHR 요청 발사!
XHR.send(
    // body 부분 json 을 보낸다.
    JSON.stringify({"title": "NewPost", "body": "This is New post", "userId": 1}) // serializing 직렬화
);

XHR.addEventListener('load', e => {
    const parseData = JSON.parse(e.target.response);
    console.log(parseData);
});
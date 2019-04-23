// 1. 함수 키워드 정의
function add(num1, num2) {
    return num1 + num2;
}

// 2. 변수에 함수 로직 할당
const sub = function (num1, num2) {
    return num1 - num2;
};

// 3. 함수 표현식 2가지

let mul = function (num1, num2) {
    return num1 * num2;
};

/*
    step 1 : function 키워드를 없앤다
    step 2 :  () 와 {} 사이에 => 를 넣는다.
 */

mul = (num1, num2) => {
    return num1 * num2;
};

/*
    추가 refactoring
    step 1 : 인자가 단 하나라면, ()가 생략 가능하다.
    step 2 : 함수 블록 안에 코드 return 문 한 줄이라면, {} & return 키워드 삭제 가능
 */

let square = function (num) {
    return num ** 2;
}

square = (num) => {
    return num ** 2;
};

square = num => num ** 2;
square(3)


let noArgs = () => {
    return 'nothing';
};

noArgs = () => 'nothing';
oneArgs = a => 'one';
manyArgs = (a, b, c, d, e) => 'wow';

// Default Args
function sayHello (name) {
    return `hi ${name}!`;
}

const sayHello = (name='ssafy') => `hi ${name}!`;

sayHello(); // 'hi ssafy'
sayHello('jun'); // 'hi jun'


(num => num ** 2)(4); // 익명함수 실행


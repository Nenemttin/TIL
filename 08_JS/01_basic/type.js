typeof 1 // "number"
typeof (() => {}) // "function"
typeof (function () {}) // "function"
typeof NaN // "number"
NaN // 'a'/ 100 === NaN  but 'a' + 100 === "a100"
'123' * 1 // 123
'123' * 0 // 0
100 / 0 // NaN
const aa = { a: 1, b: 2};
aa.c // undefined
typeof undefined // "undefined" 몰라요 없어요
typeof null // object
typeof {} // object
typeof [] // object


// typeof 의 결과값은 string ex) typeof (typeof 1)

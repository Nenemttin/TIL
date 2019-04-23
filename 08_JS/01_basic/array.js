const numbers = [1, 2, 3, 4];

numbers[0];
numbers[-1]; // undefined
numbers[4]; // undefined

numbers.length; // 4

/* 원본이 달라지는 methods */
numbers.reverse(); // [4, 3, 2, 1]
numbers; // [4, 3, 2, 1]
numbers.reverse(); // [1, 2, 3, 4]

numbers.push('a'); // 5 new length
numbers; // [1, 2, 3, 4, 'a']

numbers.pop(); //  'a'
numbers; // [1, 2, 3, 4]

numbers.unshift('a'); // 5 - new length
numbers // ['a', 1, 2, 3, 4]

numbers.shift(); // 'a'

/* Copy, 다른 결과 return */
numbers.includes(1); // true
numbers.includes(0); // false

numbers.push('a', 'a'); // test

numbers.indexOf('a'); // 4 처음 나오는 인덱스
numbers.indexOf('b'); // -1 없다

numbers.join('-'); // '1-2-3-4-a-a'
numbers.join(); // '1,2,3,4,a,a'
numbers.join(''); // '1234aa'


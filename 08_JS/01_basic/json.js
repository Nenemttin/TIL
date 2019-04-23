const myObjects = {
    coffee: 'Americano',
    iceCream: 'Cherry blossom',
};

const jsonData = JSON.stringify(myObjects); // key value 이뤄진 표기법
console.log(typeof jsonData) // string

const parseData = JSON.parse(jsonData);
console.log(typeof parseData); // object / parseData.coffee 접근 가능


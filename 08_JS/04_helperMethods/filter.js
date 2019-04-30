// ES5 for loop
// var products = [
//     { name: 'cucumber', type: 'vege', },
//     { name: 'banana', type: 'fruit', },
//     { name: 'carrot', type: 'vege', },
//     { name: 'tomato', type: 'fruit', },
// ];
//
// var fruits = [];
//
// for (var i = 0; i < products.length ; i++) {
//     if (products[i].type === 'fruit')
//         fruits.push(products[i])
// }
//
// console.log(fruits);

// ES6+
// const products = [
//     { name: 'cucumber', type: 'vege', },
//     { name: 'banana', type: 'fruit', },
//     { name: 'carrot', type: 'vege', },
//     { name: 'tomato', type: 'fruit', },
// ];
//
// const fruits = products.filter(product => {
//     // 해당 조건문에서 true 가 나오면, return 된다
//     return product.type === 'fruit'
// });

const users = [
    { id: 1, admin: true },
    { id: 2, admin: false },
    { id: 3, admin: false },
    { id: 4, admin: true },
    { id: 5, admin: false },
];

const adminUsers = users.filter(user => user.admin);

console.log(adminUsers);
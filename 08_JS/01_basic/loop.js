let i = 0
// while loop
while (i < 10) {
    console.log(i);
    i++;
}

// for loop
for (let j = 0; j < 10; j++) {
    console.log(j);
}

// for - of loop
let sum = 0;
for (const number of [1, 2, 3]) {
    sum += number;
}
console.log(sum);

for (const char of 'Happy') {
    console.log(char);
}
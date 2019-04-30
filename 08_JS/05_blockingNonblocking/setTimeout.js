function sleep_3S () {
    console.log('Invoke');
    setTimeout(() => {
        console.log('Wake up!')
    }, 3000)
}


//
// const logEnd = () => {
//     console.log('END');
// };
// console.log('start');
// setTimeout(logEnd, 3000);


console.log('Start Sleeping');
sleep_3S();
console.log('End of Program');
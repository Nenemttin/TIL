// This is Comment
const concat = (str1, str2) => `${str1} - ${str2}`;

const checkLongStr = string => {
    return string.length > 10;
};
//
// if (checkLongStr(concat('Happy', 'Hacking'))) {
//     console.log('LONG STRING');
// } else {
//     console.log('SHORT STRING');
// }

checkLongStr(concat('Happy', 'Hacking')) ? console.log('LONG STRING') : console.log('SHORT STRING');
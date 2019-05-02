module.exports = {
    addAll (numbers=[]) {
        let sum = 0;
        numbers.forEach(number => sum += number);
        return sum;
    },
    subAll (numbers=[]) {
        let sum = 0;
        numbers.forEach(number => sum -= number);
        return sum;
    },
    mulAll () {

    },

    name: 'jun',
};

phoneNumber = '01012341234';
module.exports.phoneNumber = phoneNumber;

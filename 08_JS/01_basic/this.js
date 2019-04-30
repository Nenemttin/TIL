function hi () {

}

const bye = () => {

};

const me = {
    name: 'jun',
    phone: '01012345678',
    email: 'abcd@gmail.com',
    intro: function () {
        return `Hi my name is ${this.name}.`
    }
};
console.log(me.intro());

const name = 'hello2389423498';

const you = {
    name: 'seok',
    phone: '01012345678',
    email: 'abcd@gmail.com',
    intro: () => {
        return `Hi my name is ${this.name}.`
    },
    wait: function () {
        setTimeout(() => {
            console.log(this.email)
        }, 1000)
    },

};

console.log(you.intro());
console.log(you.wait());
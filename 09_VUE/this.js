const A = {
    a: 'hi', // lv.1
    b: 'bye', // lv.1
    data: {
        msg: 'Hi',
    },
    methods: {
        greet: function () {
            return this.msg;
        }
    },
};

console.log(A.d);
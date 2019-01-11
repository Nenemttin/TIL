import random
from flask import Flask, jsonify # flask 패키지에서 Flask class를 호출

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi'

@app.route('/pick_lotto') # @ - decorator 밑에 정의되어 있는 함수를 실행해라 라는 의미가 포함되어 있음.
def pick_lotto():
    numbers = random.sample(range(1, 46), 6)
    return jsonify(numbers)

@app.route('/hi/<string:name>') #variable routing
def hi(name):
    return (f'hi {name}!')

@app.route('/dictionary/<string:word>')
def dictionary(word):
    my_dict = {
        'apple': '사과',
        'banana': '바나나',
        'melon': '멜론'
    }
    if word in my_dict:
        return f'{word}은(는) {my_dict[word]}!'
    else:
        return f'{word}은(는) 나만의 단어장에는 없는 단어입니다.'


if __name__ == '__main__':
    app.run(debug=True)
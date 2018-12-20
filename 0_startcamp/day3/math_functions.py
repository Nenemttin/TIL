print(__name__) # 예약변수 __name__ 

def average(numbers):
    return sum(numbers) / len(numbers) # 함수 안에서 다른 함수 사용 가능

def cube(x):
    return x * x * x

def main():
    my_score = [69, 59, 39, 50]
    print(my_score)
    print('평균:', average(my_score))
    print(cube(3))

if __name__ == '__main__':
    main()
    

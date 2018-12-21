print('!', __name__)

#다른데서 만든 함수 호출하는 법 'import' 이용하기 
#확장자(.py) 파일명 import
    #import math_functions
#만들어 놓은 함수가 너무 많은데 그 중에 몇 개만 골라서 사용하고 싶을 때
from math_functions import cube, average

print('=' * 10)
print(cube(5))
print(average([1, 2, 3, 4, 5, 6]))
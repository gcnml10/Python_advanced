#일급함수(일급 객체)
# 파이썬 함수 특징
#1. 런타임 초기화 가능
#2. 변수 등에 할당 가능
#3. 함수 인수 전달 가능
#4. 함수 결과로 반환 가능 return funcs


# 함수 객체 예제

def factorial(n):
    '''Factorial Function -> n:int'''
    if n == 1: #n < 2
        return 1
    return n * factorial(n-1)

class A:
    pass

print('EX1-1 -', factorial(5))

print('EX1-2 -', factorial.__doc__)
print('EX1-3 -', type(factorial), type(A))
print('EX1-4 -', sorted(set(dir(factorial))-set(dir(A))))
print('EX1-5 -', factorial.__name__)
print('EX1-6 -', factorial.__code__)

print()
print()

# 변수 할당
var_func = factorial

print('EX2-1 -', var_func)
print('EX2-1 -', var_func(5))
print('EX2-3 -', map(var_func, range(1,6)))
print('EX2-3 -', list(map(var_func, range(1,6))))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order Function)

print('EX3-1 -', list(map(var_func, filter(lambda x: x % 2, range(1,6)))))
print('EX3-2 -', [var_func(i) for i in range(1,6) if i % 2])

print()
# reduce()

from functools import reduce
from operator import add

print('EX3-3 -', reduce(add, range(1,11)))
print('EX3-4 -', sum(range(1,11)))

# 익명함수(lambda)
# 가급적 주석 사용
# 가급적 함수 사용
# 일반 함수 형태로 리팩토링 권장

print('EX3-5 -', reduce(lambda x, t: x + t, range(1,11)))
print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인


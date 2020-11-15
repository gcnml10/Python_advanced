# 일급함수(일급 객체)
# 파이썬 함수 특징
# Decorator & Closure

# 파이썬 변수 범위 (global)

#예제 1
def func_v1(a):
    print(a)
    print(b)

# 예외
# func_v1(5)

#예제 2
b = 10

def func_v2(a):
    print(a)
    print(b)

func_v2(5)

#예제 3
b = 10

# def func_v3(a):
#     print(a)
#     print(b)
#     b = 5

# func_v3(5)

from dis import dis

# print('EX1-1 -')
# print(dis(func_v3))

# Closure(클로저)
# 반환되는 내부 함수에 대해서 선언된 연결 정보를 가지고 참조하는 방식
# 반환 당시 함수 유효범위를 벗어난 변수 또는 메소드에 직접 접근이 가능하다.

a = 10

print('EX1-1 -', a + 10)
print('EX2-2 -', a + 100)

#결과를 누적 할 수 없을까?
print('EX2-3 -', sum(range(1,50)))
print('EX2-3 -', sum(range(51,101))) 

print()
print()

# 클래스 이용
class Averager():
    def __init__(self):
        self._series = []
    
    def __call__(self, v):
        self._series.append(v)
        print('class >>>>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성
avg_cls = Averager()

# 누적 확인
print('EX3-1 - ', avg_cls(15))
print('EX3-1 - ', avg_cls(35))
print('EX3-1 - ', avg_cls(40))

print()
print()

# 클로저(Closure) 사용
# 전역변수 사용 감소
# 디자인 패턴 적용

def closure_avg1():
    # Free variable
    series = []
    # 클로저 영역
    def averager(v):
        # series = [] # Check
        series.append(v)
        print('class >>>>> {} / {}'.format(series, len(series)))
        return sum(series) / len (series)
    return averager

avg_closure1 = closure_avg1()

print('EX4-1 -', avg_closure1(15))
print('EX4-1 -', avg_closure1(35))
print('EX4-1 -', avg_closure1(40))

print()
print()

print('EX5-1 -', dir(avg_closure1))
print()
print('EX5-2 -', dir(avg_closure1.__code__))
print()
print('EX5-2 -', avg_closure1.__code__.co_freevars)
print()
print('EX5-2 -', dir(avg_closure1.__closure__[0]))
print()
print('EX5-2 -', dir(avg_closure1.__closure__[0].cell_contents))

print()
print()

#잘못된 클로저 사용 예

def closure_avg2():
    # Free variable
    cnt = 0
    total = 0
    #클로저영역
    def averager(v):
        nonlocal cnt, total  #############
        cnt += 1
        total += v
        print('def2 >>>>> {} / {}'.format(total, cnt))
        return total / cnt
    return averager

avg_closure2 = closure_avg2()
print('EX5-5', avg_closure2(15))
print('EX5-5', avg_closure2(35))
print('EX5-5', avg_closure2(40))


# 데코레이터 실습
# 1. 중복 제거, 코드 간결
# 2. 클로저 보다 문법 간결
# 3. 조합해서 사용 용이

# 단점
# 1. 디버깅 어려움
# 2. 에러의 모호함

import time

def perf_clock(func):
    def perf_clocked(*args):
        # 시작 시간
        st = time.perf_counter()
        result = func(*args)
        # 종료 시간
        et = time.perf_counter() -st
        # 함수명
        name = func.__name__
        # 매개변수
        arg_str = ','.join(repr(arg) for arg in args)
        #출력
        print('Result : [%0.5fs] %s(%s) - > %r' % (et, name, arg_str, result))
        return result
    return perf_clocked

@perf_clock
def time_func(seconds):
    time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
    return sum(numbers)

@perf_clock
def fact_func(n):
    return 1 if n < 2 else n * fact_func(n-1)

# 데코레이터 미사용

non_deco1 = perf_clock(time_func)
non_deco2 = perf_clock(sum_func)
non_deco3 = perf_clock(fact_func)

# print('EX7-1 -', non_deco1, non_deco1.__code__.co_freevars)
# print('EX7-1 -', non_deco1, non_deco2.__code__.co_freevars)
# print('EX7-1 -', non_deco1, non_deco3.__code__.co_freevars)

# print('*'*40, "Called Non Deco -> time_func")
# print('EX7-4')
# non_deco1(2)
# print('EX7-4')
# non_deco2(100, 200)
# print('EX7-4')
# non_deco3(20)

print()
print()
print()

print('*'*40, "Called Deco -> time_func")
print('EX7-4')
time_func(2)
print('*'*40, "Called Deco -> sum_func")
print('EX7-4')
sum_func(10,20,30,40,50)
print('*'*40, "Called Deco -> fact_func")
print('EX7-4')
fact_func(15)
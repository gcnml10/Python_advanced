#파이썬 클래스 특별 메소드 심화 활용 및 상속
# Class ABC

# class 선언
class VectorP(object):
    def __init__(self, x, y):
        self.__x = float(x)
        if y <  30:
            raise ValueError('y below 30 not possible')
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y)) #Generator 데이터가 많을 때는 요거

    @property
    def x(self):
        print('Called Propery X')
        return self.__x

    @x.setter
    def x(self, v):
        print('Called Setter X')
        self.__x = float(v)

    @property
    def y(self):
        print('Called Propery y')
        return self.__y

    @y.setter
    def y(self, v):
        if v < 30:
            raise ValueError('30 Below is not possible')
        print('Called Setter y')
        self.__y = float(v)



# 객체 선언
v = VectorP(20,40)


# print('EX1-1 -', v.__x,v.__y)

# Getter, Setter
# print(v.x)
# v.x = 10

print('EX1-2 -', dir(v), v.__dict__)
print('EX1-3 -', v.x, v.y)

# v.y = 20

# Iter 확인 
for val in v:
    print('EX1-2 -', val)

#__slot__
# 파이썬 인터프리터에게 통보
# 해당 클래스가 가지는 속성을 제한
# __dict__ 속성 최적화 -> 다수 객체 생성시 -> 메모리 사용공간 대폭 감소
# 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 Set 형태를 사용

class TestA(object):
    __slots__ = ('a',)

class TestB(object):
    pass

use_slot = TestA()
no_slot = TestB()

print('EX2-1 -', use_slot)
# print('EX2-1 -', use_slot.__dict__)
print('EX2-1 -', no_slot)
print('EX2-1 -', no_slot.__dict__)

# 메모리 사용량 비교
import timeit

# 측정을 위한 함수 선언
def repeat_outer(obj):
    def repeat_inner():
        obj.a = 'TEST'
        del obj.a
    return repeat_inner

# print(min(timeit.repeat(repeat_outer(use_slot), number=100000)))
# print(min(timeit.repeat(repeat_outer(no_slot), number=100000)))

print()
print()

# 객체 슬라이싱

class ObjectS:
    def __init__(self):
        self._numbers = [n for n in range(1,10000,3)]

    def __len__(self):
        return len(self._numbers)

    def __getitem__(self, idx):
        return self._numbers[idx]

s = ObjectS()

# print('EX3-1 -', s.__dict__)
print('EX3-2 -', len(s))
print('EX3-2 -', len(s._numbers))
print('EX3-4 -', s[1:100])
print('EX3-4 -', s[-1])
print('EX3-4 -', s[::10])

print()
print()

# 파이썬 추상 메소드

# 자체적으로 객체 생성 불가
# 상속을 통해서 자직 클래스에서 인스턴스를 생성해야 함
# 개발과 관련된 공통된 내용(필드, 메소드) 추출 및 통합해서 공통된 내용으로 작성하게 하는 것

# Sequence 상속 받지 않았지만, 자동으로 기능 작동 __iter__, __contain__(in 연산자) 기능 작동
# 객체 전체를 자동으로 조사 -> 시퀀스 프로토콜

class IterTestA():
    def __getitem__(self, idx):
        return range(1,50,2)[idx] 

i1 = IterTestA()

print('EX4-1 -', i1[4])
print('EX4-1 -', i1[4:10])
print('EX4-1 -', 3 in i1[1:10])
# print('EX4-4 -', [i for i in i1[:]])

print()
print()

# Sequence 상소
# 요구사항인 추상 메소드를 모두 구현해야 동장

from collections.abc import Sequence
class IterTestB(Sequence):          #FM 대로 상속을 받았으니까 FM대로 구현해줘야함
    def __getitem__(self, idx):
        return range(1,50,2)[idx] 
        
    def __len__(self):
        return len(range(1,10,2))

i2 = IterTestB()
print('EX4-1 -', i2[4])
print('EX4-1 -', i2[4:10])
print('EX4-1 -', 3 in i2[1:10])

print()
print()

# abc 활용 예제
import abc

class RandomMachine(abc.ABC):  # metaclass = abc.ABCMeta(3.4 이하)
    # __metaclass__ = abc.ABCMeta

    # 추상 메소드
    @abc.abstractmethod
    def load(self, iterobj):
        '''Iterable 항목 추가'''
    
    #추상 메소드
    @abc.abstractmethod
    def pick(self):
        '''무작위 항목 뽑기'''

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
            return tuple(sorted(items))

import random

class CraneMachine(RandomMachine):
    def __init__(self,items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Empty Crane Box')

    def __call__(self):
        return self.pick()

# 서브 클래스 확인
print('EX5-1 -', issubclass(RandomMachine, CraneMachine))
print('EX5-1 -', issubclass(CraneMachine, RandomMachine))

# 상속 구조 확인
print('EX5-3 -', CraneMachine.__mro__)

cm = CraneMachine(range(1,100)) # 추상 메소드 구현 안하면 에러

print('EX5-4 -', cm._items)
print('EX5-5 -', cm.pick())
print('EX5-5 -', cm())
print('EX5-5 -', cm.inspect())
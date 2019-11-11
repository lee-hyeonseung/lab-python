"""
파이썬에서 함수는 1급 객체(first-class object)
- 함수를 변수에 저장할 수 있음
- 매개변수(parameter)에 함수를 전달할 수 있음
- 함수가 다른 함수를 리턴할 수 있음
- 함수 내부에서 다른 함수를 정의할 수 있음
"""


def twice(x):
    return 2*x


result = twice(100)    # 함수 호출 -> 함수의 리턴값 저장
print(result)

double = twice  # 함수를 변수에 저장
print(double)

print(result)


def plus(x,y):
    return x+y


def minus(x,y):
    return x-y


def calculate(x, y, operator):
    return operator(x,y)


result = calculate(1, 2, plus)   # plus 뒤에는 괄호 없어야 한다
print(result)

result = calculate(1, 2, minus)
print(result)


def decorate(func):
    print('decorate 함수 내부: ', func.__name__)
    # decorate 함수 내부에서 wrapper_function 함수를 정의
    def wrapper_function(*args):
        print('다음 함수를 실행: ', func.__name__)
        return func(*args)
    return wrapper_function

wrapper = decorate(print)
wrapper('a', 'b', 'c')
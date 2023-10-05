def preFunc():
    print('전처리')

def aftFunc():
    print('후처리')

def myFunc():
    #전처리
    preFunc()
    #my Func
    print('my Func1')
    #후처리
    aftFunc()

def myFunc2():
    #전처리
    preFunc()
    #my Func
    print('my Func2')
    #후처리
    aftFunc()

# 전처리, 후처리 코드가 너무 중복되는데
# 없애는 방법은?
# -> 데코레이터

#데코레이터 함수
# 메인로직(func함수)을 감싸주는 새로운 함수를 만든다.
is_logined = False
def my_decorator(func):
    def wrapper():
        if not is_logined:
            print('로그인해라')
            return
        print("전처리")
        func()
        print("후처리")
    return wrapper

@my_decorator
def myFunc3():
    print('myfunc3')

myFunc()
print()
myFunc2()
print()
myFunc3()